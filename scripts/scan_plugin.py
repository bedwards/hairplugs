#!/usr/bin/env python3
"""Scan a VST3 plugin and dump all parameters with current values."""

import sys
import json
from pedalboard import load_plugin

VST3_DIR = "/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3"

def scan_plugin(name_or_path):
    if name_or_path.endswith('.vst3'):
        path = name_or_path
    else:
        path = f"{VST3_DIR}/{name_or_path}.vst3"

    plugin = load_plugin(path)
    params = {}
    for key in plugin.parameters:
        if key.startswith('midi_cc_') or key in ('aftertouch', 'pitchbend', 'midi_program_change'):
            continue
        val = getattr(plugin, key, None)
        params[key] = val

    return {
        "name": str(plugin),
        "path": path,
        "param_count": len(params),
        "parameters": params
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scan_plugin.py <PluginName|path.vst3> [--json]")
        sys.exit(1)

    result = scan_plugin(sys.argv[1])

    if "--json" in sys.argv:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"{result['name']} — {result['param_count']} parameters\n")
        for k, v in result['parameters'].items():
            print(f"  {k}: {v}")
