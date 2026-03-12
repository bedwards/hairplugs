#!/usr/bin/env python3
"""plugctl — CLI tool for VST3 preset management.

Usage:
    plugctl plugins                              # List all VST3 plugins
    plugctl scan <plugin> [--json]               # Show all parameters + values
    plugctl snap <plugin> <name> [--comment ""]  # Save state snapshot
    plugctl presets <plugin>                      # List saved presets
    plugctl load <plugin> <name>                  # Restore state from preset
    plugctl diff <plugin> <a> <b>                 # Compare two presets
    plugctl tweak <plugin> <name> --save-as <new> param=val ...
    plugctl export-vst3 <plugin> <name> [--all]   # Export to ~/Library/Audio/Presets/
    plugctl export-bwpreset <plugin> <name> [--all]  # Export to Bitwig library
    plugctl init <plugin>                         # Save default state as "_init"
"""

import argparse
import hashlib
import io
import json
import plistlib
import re
import struct
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path

VST3_DIR = Path("/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3")
PRESETS_DIR = Path(__file__).resolve().parent.parent / "presets"
VST3_PRESETS_DIR = Path.home() / "Library" / "Audio" / "Presets"
BITWIG_LIBRARY = Path.home() / "Documents" / "Bitwig Studio" / "Library"

SKIP_PARAMS = frozenset({'aftertouch', 'pitchbend', 'midi_program_change'})


# ── Helpers ──────────────────────────────────────────────────────────────────

def get_vst3_plugins():
    """List all .vst3 bundles, including nested ones (e.g. Soundtoys/)."""
    plugins = []
    for item in sorted(VST3_DIR.iterdir()):
        if item.suffix == '.vst3':
            plugins.append(item)
        elif item.is_dir() and not item.suffix:
            for sub in sorted(item.iterdir()):
                if sub.suffix == '.vst3':
                    plugins.append(sub)
    return plugins


def read_plist(vst3_path):
    """Read Info.plist from a .vst3 bundle."""
    plist_path = vst3_path / "Contents" / "Info.plist"
    if plist_path.exists():
        with open(plist_path, 'rb') as f:
            return plistlib.load(f)
    return {}


def vendor_slug(plist):
    """Extract filesystem-safe vendor slug from bundle identifier."""
    bundle_id = plist.get('CFBundleIdentifier', '')
    parts = bundle_id.split('.')
    if len(parts) >= 2 and parts[0] == 'com':
        return parts[1].lower()
    return 'unknown'


def vendor_display(plist):
    """Extract human-readable vendor name from copyright strings."""
    for key in ('NSHumanReadableCopyright', 'CFBundleGetInfoString'):
        text = plist.get(key, '')
        if not text:
            continue
        # Strip leading version (e.g. "11.3.0, ")
        text = re.sub(r'^[\d.]+,\s*', '', text)
        m = re.search(
            r'(?:Copyright\s*(?:©|\(c\))?\s*|©\s*)'
            r'(?:\d{4}(?:\s*-\s*\d{4})?\s*[,]?\s*)?'
            r'([\w][\w\s]*?)(?:\s*(?:\.|,\s|All\s|Inc|LLC|$))',
            text, re.I,
        )
        if m:
            return m.group(1).strip()
    return vendor_slug(plist)


def export_vendor_dir(plist):
    """Determine vendor directory name for VST3 preset export.

    Matches existing ~/Library/Audio/Presets/ dirs when possible.
    """
    slug = vendor_slug(plist)
    display = vendor_display(plist)

    if not VST3_PRESETS_DIR.exists():
        return display

    existing = {d.name.lower(): d.name
                for d in VST3_PRESETS_DIR.iterdir() if d.is_dir()}

    # Exact slug match (e.g. izotope → iZotope)
    if slug in existing:
        return existing[slug]
    # Display name match
    if display.lower() in existing:
        return existing[display.lower()]

    return display


def resolve_plugin(name):
    """Resolve short plugin name to .vst3 path."""
    exact = VST3_DIR / f"{name}.vst3"
    if exact.exists():
        return exact

    name_lower = name.lower()
    all_plugins = get_vst3_plugins()

    for p in all_plugins:
        if p.stem.lower() == name_lower:
            return p

    matches = [p for p in all_plugins if name_lower in p.stem.lower()]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        print(f"Ambiguous name '{name}', matches:", file=sys.stderr)
        for m in matches:
            print(f"  {m.stem}", file=sys.stderr)
        sys.exit(1)

    print(f"Plugin not found: {name}", file=sys.stderr)
    sys.exit(1)


def preset_dir(vst3_path):
    """Get preset storage directory for a plugin."""
    plist = read_plist(vst3_path)
    slug = vendor_slug(plist)
    plugin_name = vst3_path.stem.lower().replace(' ', '-')
    return PRESETS_DIR / slug / plugin_name


def filter_params(plugin):
    """Get plugin parameters, filtering MIDI CCs and standard controls."""
    params = {}
    for key in plugin.parameters:
        if key.startswith('midi_cc_') or key in SKIP_PARAMS:
            continue
        params[key] = getattr(plugin, key, None)
    return params


def save_preset(vst3_path, plugin, name, comment=''):
    """Save plugin state as JSON metadata + binary blob."""
    pdir = preset_dir(vst3_path)
    pdir.mkdir(parents=True, exist_ok=True)

    params = filter_params(plugin)
    plist = read_plist(vst3_path)

    meta = {
        'name': name,
        'plugin': vst3_path.stem,
        'plugin_path': str(vst3_path),
        'vendor': vendor_display(plist),
        'vendor_slug': vendor_slug(plist),
        'comment': comment,
        'param_count': len(params),
        'created': datetime.now(timezone.utc).isoformat(),
        'parameters': {k: v for k, v in params.items()},
    }

    json_path = pdir / f"{name}.json"
    blob_path = pdir / f"{name}.blob"

    with open(json_path, 'w') as f:
        json.dump(meta, f, indent=2, default=str)

    with open(blob_path, 'wb') as f:
        f.write(plugin.preset_data)

    return json_path, blob_path


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_plugins(args):
    """List all VST3 plugins."""
    plugins = get_vst3_plugins()
    for p in plugins:
        plist = read_plist(p)
        vendor = vendor_display(plist)
        version_parts = plist.get('CFBundleShortVersionString', '').split()
        version = version_parts[0] if version_parts else ''
        name = p.stem
        if p.parent != VST3_DIR:
            name = f"{p.parent.name}/{name}"
        print(f"  {name:<40} {vendor:<25} {version}")
    print(f"\n{len(plugins)} plugins")


def cmd_scan(args):
    """Show all parameters + values."""
    from pedalboard import load_plugin

    vst3_path = resolve_plugin(args.plugin)
    plugin = load_plugin(str(vst3_path))
    params = filter_params(plugin)

    if args.json:
        result = {
            'name': str(plugin),
            'path': str(vst3_path),
            'param_count': len(params),
            'parameters': params,
        }
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"{plugin} — {len(params)} parameters\n")
        for k, v in params.items():
            print(f"  {k}: {v}")


def cmd_snap(args):
    """Save plugin state as preset."""
    from pedalboard import load_plugin

    vst3_path = resolve_plugin(args.plugin)
    plugin = load_plugin(str(vst3_path))

    json_path, blob_path = save_preset(
        vst3_path, plugin, args.name, args.comment,
    )
    print(f"Saved {json_path.relative_to(PRESETS_DIR.parent)}")
    print(f"  + {blob_path.relative_to(PRESETS_DIR.parent)}"
          f" ({blob_path.stat().st_size} bytes)")


def cmd_presets(args):
    """List saved presets for a plugin."""
    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)

    if not pdir.exists():
        print(f"No presets for {vst3_path.stem}")
        return

    json_files = sorted(pdir.glob("*.json"))
    if not json_files:
        print(f"No presets for {vst3_path.stem}")
        return

    print(f"{vst3_path.stem} presets ({pdir.relative_to(PRESETS_DIR.parent)}):\n")
    for jf in json_files:
        with open(jf) as f:
            meta = json.load(f)
        name = meta['name']
        comment = meta.get('comment', '')
        created = meta.get('created', '')[:10]
        blob_exists = (pdir / f"{name}.blob").exists()
        status = "●" if blob_exists else "○"
        line = f"  {status} {name:<30} {created}"
        if comment:
            line += f"  # {comment}"
        print(line)

    print(f"\n{len(json_files)} presets (● = blob present, ○ = json only)")


def cmd_init(args):
    """Save default plugin state as _init."""
    from pedalboard import load_plugin

    vst3_path = resolve_plugin(args.plugin)
    plugin = load_plugin(str(vst3_path))

    json_path, _ = save_preset(
        vst3_path, plugin, '_init', 'Default plugin state',
    )
    print(f"Saved default state: {json_path.relative_to(PRESETS_DIR.parent)}")


def cmd_load(args):
    """Restore state from saved preset."""
    from pedalboard import load_plugin

    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)
    blob_path = pdir / f"{args.name}.blob"
    json_path = pdir / f"{args.name}.json"

    if not blob_path.exists():
        if not json_path.exists():
            print(f"Preset not found: {args.name}", file=sys.stderr)
        else:
            print(f"Blob missing for {args.name} (json-only preset)",
                  file=sys.stderr)
        sys.exit(1)

    plugin = load_plugin(str(vst3_path))

    with open(blob_path, 'rb') as f:
        plugin.preset_data = f.read()

    # Verify by comparing params to saved JSON
    params = filter_params(plugin)

    with open(json_path) as f:
        meta = json.load(f)

    saved_params = meta.get('parameters', {})
    mismatches = 0
    for k, v in saved_params.items():
        current = params.get(k)
        if (current is not None
                and isinstance(v, (int, float))
                and isinstance(current, (int, float))
                and abs(float(v) - float(current)) > 0.001):
            mismatches += 1

    print(f"Loaded {args.name} into {vst3_path.stem}")
    print(f"  {len(params)} parameters restored")
    if mismatches:
        print(f"  ⚠ {mismatches} params differ"
              " (blob may contain hidden state)")
    else:
        print(f"  All parameters match saved values")


def cmd_diff(args):
    """Compare two presets (param-level)."""
    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)

    json_a = pdir / f"{args.a}.json"
    json_b = pdir / f"{args.b}.json"

    for path, name in ((json_a, args.a), (json_b, args.b)):
        if not path.exists():
            print(f"Preset not found: {name}", file=sys.stderr)
            sys.exit(1)

    with open(json_a) as f:
        params_a = json.load(f).get('parameters', {})
    with open(json_b) as f:
        params_b = json.load(f).get('parameters', {})

    all_keys = sorted(set(params_a) | set(params_b))

    diffs = []
    for k in all_keys:
        va = params_a.get(k)
        vb = params_b.get(k)
        if va != vb:
            diffs.append((k, va, vb))

    print(f"Diff: {args.a} → {args.b} ({vst3_path.stem})\n")

    if not diffs:
        print("  No parameter differences")
        return

    for k, va, vb in diffs:
        if isinstance(va, float) and isinstance(vb, float):
            print(f"  {k}: {va:.4f} → {vb:.4f}")
        else:
            print(f"  {k}: {va} → {vb}")

    print(f"\n{len(diffs)} differences / {len(all_keys)} total parameters")


def cmd_tweak(args):
    """Fork a preset with parameter modifications."""
    from pedalboard import load_plugin

    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)
    blob_path = pdir / f"{args.name}.blob"

    if not blob_path.exists():
        print(f"Preset not found: {args.name}", file=sys.stderr)
        sys.exit(1)

    plugin = load_plugin(str(vst3_path))

    with open(blob_path, 'rb') as f:
        plugin.preset_data = f.read()

    # Apply tweaks
    tweaks = {}
    for spec in args.params:
        if '=' not in spec:
            print(f"Invalid param spec (need param=val): {spec}",
                  file=sys.stderr)
            sys.exit(1)
        key, val_str = spec.split('=', 1)
        try:
            val = float(val_str)
        except ValueError:
            val = val_str.lower() in ('true', '1', 'yes')
        setattr(plugin, key, val)
        tweaks[key] = val

    comment = (f"Tweaked from {args.name}: "
               + ', '.join(f'{k}={v}' for k, v in tweaks.items()))
    json_path, _ = save_preset(vst3_path, plugin, args.save_as, comment)

    print(f"Saved {args.save_as} (tweaked from {args.name})")
    for k, v in tweaks.items():
        print(f"  {k} = {v}")


def cmd_export_vst3(args):
    """Export preset(s) to ~/Library/Audio/Presets/ for plugin browser."""
    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)
    plist = read_plist(vst3_path)

    vendor_dir_name = export_vendor_dir(plist)
    plugin_name = vst3_path.stem
    export_dir = VST3_PRESETS_DIR / vendor_dir_name / plugin_name

    if args.all:
        names = [jf.stem for jf in sorted(pdir.glob("*.json"))]
    elif args.name:
        names = [args.name]
    else:
        print("Error: provide a preset name or --all", file=sys.stderr)
        sys.exit(1)

    exported = 0
    for name in names:
        blob_path = pdir / f"{name}.blob"
        if not blob_path.exists():
            print(f"  Skipping {name} (no blob)", file=sys.stderr)
            continue

        export_dir.mkdir(parents=True, exist_ok=True)
        dest = export_dir / f"{name}.vstpreset"

        with open(blob_path, 'rb') as f:
            data = f.read()
        with open(dest, 'wb') as f:
            f.write(data)

        print(f"  {name} → {dest}")
        exported += 1

    print(f"\nExported {exported} preset(s) to {export_dir}")


# ── Bitwig .bwpreset format ──────────────────────────────────────────────────

# Plugin classification for Bitwig device_type / device_category.
# Instruments = note_to_audio / Synth; Effects = audio_to_audio / Effect.
EFFECT_PLUGINS = frozenset({
    'Artillery2', 'Effectrix', 'Looperator', 'Turnado', 'WOW2',
    'bx_greenscreamer', 'DynOne3', 'soothe2', 'ValhallaRoom',
    'Comeback Kid', 'Decapitator',
    'Insight 2',  # metering
    # Ozone, RX, WaveShell are also effects
})
EFFECT_PREFIXES = ('Ozone', 'RX 10', 'WaveShell')


def is_effect_plugin(plugin_name):
    """Determine if a plugin is an audio effect (vs instrument)."""
    if plugin_name in EFFECT_PLUGINS:
        return True
    return any(plugin_name.startswith(p) for p in EFFECT_PREFIXES)


def extract_class_id(blob):
    """Extract 32-char hex VST3 class ID from preset blob."""
    if blob[:4] != b'VST3':
        return None
    return blob[8:40].decode('ascii')


def bwpreset_meta_bytes(entries):
    """Encode metadata key-value pairs in Bitwig binary format.

    Format per entry: [u32 marker=1] [u32 key_len] [key] [u8 type] [u32 val_len] [val]
    Type tags: 0x08=string, 0x19=bytes, 0x03=u32
    """
    buf = io.BytesIO()

    # Section header: two u32s (4, 4) + "meta"
    buf.write(struct.pack('>II', 4, 4))
    buf.write(b'meta')

    for key, val in entries:
        buf.write(struct.pack('>I', 1))  # marker
        key_bytes = key.encode('utf-8')
        buf.write(struct.pack('>I', len(key_bytes)))
        buf.write(key_bytes)

        if isinstance(val, int):
            buf.write(b'\x03')
            buf.write(struct.pack('>I', val))
        elif isinstance(val, bytes):
            buf.write(b'\x19')
            buf.write(struct.pack('>I', len(val)))
            buf.write(val)
        else:  # string
            val_bytes = val.encode('utf-8')
            buf.write(b'\x08')
            buf.write(struct.pack('>I', len(val_bytes)))
            buf.write(val_bytes)

    return buf.getvalue()


def build_bwpreset(blob, plugin_name, vendor_name, version,
                   comment='', preset_category='', tags=''):
    """Build a .bwpreset binary from a VST3 preset blob.

    Format: BtWg ASCII header (42 bytes) + meta section + ZIP section.
    The ZIP contains plugin-states/<uuid>.vstpreset.
    """
    class_id = extract_class_id(blob)
    if not class_id:
        raise ValueError("Blob is not a valid VST3 preset")

    device_type = 'audio_to_audio' if is_effect_plugin(plugin_name) else 'note_to_audio'
    device_category = 'Effect' if device_type == 'audio_to_audio' else 'Synth'
    device_id = f"vst3:{class_id}:{version}"
    preset_uuid = str(uuid.uuid4())
    revision_id = hashlib.sha1(blob).hexdigest()

    # Build meta entries (order matches Bitwig's output)
    meta_entries = [
        ('application_version_name', '5.2'),
        ('branch', 'releases'),
        ('comment', comment),
        ('creator', ''),
        ('device_category', device_category),
        ('device_creator', vendor_name),
        ('device_id', device_id),
        ('device_name', plugin_name),
        ('device_type', device_type),
        ('preset_category', preset_category),
        ('referenced_device_ids', b''),
        ('referenced_modulator_ids', b''),
        ('referenced_module_ids', b''),
        ('referenced_packaged_file_ids', b''),
        ('revision_id', revision_id),
        ('revision_no', 0),
        ('tags', tags),
        ('type', 'application/bitwig-preset'),
    ]

    meta_data = bwpreset_meta_bytes(meta_entries)

    # Build ZIP containing the vstpreset
    zip_buf = io.BytesIO()
    with zipfile.ZipFile(zip_buf, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(f'plugin-states/{preset_uuid}.vstpreset', blob)
    zip_data = zip_buf.getvalue()

    # Calculate offsets (from start of file)
    header_len = 42  # "BtWg" + 38 hex chars
    meta_offset = header_len
    zip_offset = meta_offset + len(meta_data)
    # Field4 = body offset (no body section, point to zip)
    body_offset = zip_offset

    # Build ASCII hex header (42 bytes: "BtWg" + 38 hex chars)
    header = (
        'BtWg'
        f'0003'           # version
        f'0002'           # type
        f'00ba'           # field3 (constant)
        f'{body_offset:08x}'   # field4: body offset
        f'00000000'       # field5: zero
        f'{zip_offset:08x}'    # field6: zip offset
        f'00'             # field7
    ).encode('ascii')

    return header + meta_data + zip_data


def cmd_export_bwpreset(args):
    """Export preset(s) to Bitwig library as .bwpreset."""
    vst3_path = resolve_plugin(args.plugin)
    pdir = preset_dir(vst3_path)
    plist = read_plist(vst3_path)

    plugin_name = vst3_path.stem
    vendor_name = vendor_display(plist)
    version_parts = plist.get('CFBundleShortVersionString', '0').split()
    version = version_parts[0] if version_parts else '0'

    export_dir = BITWIG_LIBRARY / "Presets" / plugin_name

    if args.all:
        names = [jf.stem for jf in sorted(pdir.glob("*.json"))]
    elif args.name:
        names = [args.name]
    else:
        print("Error: provide a preset name or --all", file=sys.stderr)
        sys.exit(1)

    exported = 0
    for name in names:
        blob_path = pdir / f"{name}.blob"
        json_path = pdir / f"{name}.json"
        if not blob_path.exists():
            print(f"  Skipping {name} (no blob)", file=sys.stderr)
            continue

        with open(blob_path, 'rb') as f:
            blob = f.read()

        # Read comment from JSON metadata
        comment = ''
        if json_path.exists():
            with open(json_path) as f:
                meta = json.load(f)
            comment = meta.get('comment', '')

        bwpreset = build_bwpreset(
            blob, plugin_name, vendor_name, version,
            comment=comment,
        )

        export_dir.mkdir(parents=True, exist_ok=True)
        dest = export_dir / f"{name}.bwpreset"
        with open(dest, 'wb') as f:
            f.write(bwpreset)

        print(f"  {name} → {dest}")
        exported += 1

    print(f"\nExported {exported} bwpreset(s) to {export_dir}")
    print("Open Bitwig and check if preset appears in browser.")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog='plugctl',
        description='VST3 preset management CLI',
    )
    sub = parser.add_subparsers(dest='command')

    sub.add_parser('plugins', help='List all VST3 plugins')

    p = sub.add_parser('scan', help='Show parameters + values')
    p.add_argument('plugin')
    p.add_argument('--json', action='store_true')

    p = sub.add_parser('snap', help='Save plugin state')
    p.add_argument('plugin')
    p.add_argument('name')
    p.add_argument('--comment', default='')

    p = sub.add_parser('presets', help='List saved presets')
    p.add_argument('plugin')

    p = sub.add_parser('load', help='Restore state from preset')
    p.add_argument('plugin')
    p.add_argument('name')

    p = sub.add_parser('diff', help='Compare two presets')
    p.add_argument('plugin')
    p.add_argument('a')
    p.add_argument('b')

    p = sub.add_parser('tweak', help='Fork + modify preset')
    p.add_argument('plugin')
    p.add_argument('name')
    p.add_argument('--save-as', required=True)
    p.add_argument('params', nargs='*')

    p = sub.add_parser('init', help='Save default state as _init')
    p.add_argument('plugin')

    p = sub.add_parser('export-vst3', help='Export to VST3 preset location')
    p.add_argument('plugin')
    p.add_argument('name', nargs='?')
    p.add_argument('--all', action='store_true')

    p = sub.add_parser('export-bwpreset', help='Export to Bitwig library')
    p.add_argument('plugin')
    p.add_argument('name', nargs='?')
    p.add_argument('--all', action='store_true')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'plugins': cmd_plugins,
        'scan': cmd_scan,
        'snap': cmd_snap,
        'presets': cmd_presets,
        'load': cmd_load,
        'diff': cmd_diff,
        'tweak': cmd_tweak,
        'init': cmd_init,
        'export-vst3': cmd_export_vst3,
        'export-bwpreset': cmd_export_bwpreset,
    }
    commands[args.command](args)


if __name__ == '__main__':
    main()
