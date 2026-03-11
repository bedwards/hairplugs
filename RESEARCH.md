# Research Notes

## Plugin Hackability Summary

### Pedalboard (Python) — CLI Plugin Control

The `pedalboard` Python package (by Spotify) can load VST3 plugins headlessly and expose all parameters for reading/writing. This enables CLI-based preset creation, audio processing, and parameter automation without a DAW.

**Confirmed working (with param counts):**
| Plugin | Params | Status |
|--------|--------|--------|
| WOW2 | 86 | Full control |
| Aparillo | 162 | Full control |
| Artillery2 | 1025 | Full control |
| Cyclop | 146 | Full control |
| Effectrix | 118 | Full control |
| Egoist | 61 | Full control |
| Factory | 231 | Full control |
| Guitarist | 81 | Full control |
| Looperator | 116 | Full control |
| Obscurium | 130 | Full control |
| Thesys | 47 | Full control |
| Turnado | 253 | Full control |
| Unique | 155 | Full control |
| Consequence | 88 | Full control |
| Comeback Kid | 23 | Full control |
| DynOne3 | 114 | Full control |
| ValhallaRoom | 23 | Full control |
| bx_greenscreamer | 5 | Full control |
| soothe2 | 56 | Full control |
| Surge XT | 775 | Full control |
| Surge XT Effects | 13 | Full control |
| M-Tron Pro IV | 116 | Full control |
| DecentSampler | 1 | Bypass only |

**Not working via pedalboard:**
- DrumComputer — crashes (use in DAW only)
- Kontakt — too complex, requires GUI
- iZotope plugins — require iLok/authorization in headless mode
- Waves plugins — WaveShell architecture, not directly loadable

### Sugar Bytes Preset Format

All Sugar Bytes presets use binary formats:
- `.sbd` — Aparillo
- `.sbcy` — Cyclop
- `.sbb` — DrumComputer
- `.sbep` — Factory
- `.wow` — WOW2
- `.gpp/.gpc/.gps/.gpg` — Guitarist (patterns/chords/sounds/global)

Common header pattern: Little-endian size (4 bytes), version? (4 bytes), then `0000 f042 0044 2c47` or similar magic bytes.

These are not easily human-editable but could be reverse-engineered with enough samples.

### File System Locations

**Sugar Bytes user data:** `~/Documents/Sugar Bytes/[PluginName]/`
- Each plugin has Presets/ and saved.chunk
- Some have additional: CC Maps, Samples, Wavetables, Midi Prg List
- Guitarist has: Patterns/ (11 genres), Chords/ (12 categories), Sounds/ (11 genres), Global Presets/

**Plugin binaries:**
- AU: `/Volumes/Macintosh HD/Library/Audio/Plug-Ins/Components/`
- VST: `/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST/`
- VST3: `/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3/`

**Standalone apps:** `/Volumes/Macintosh HD/Applications/Sugar Bytes/[PluginName]/[PluginName].app`

**Kontakt database:** `~/Library/Application Support/Native Instruments/Kontakt 8/komplete.db3` (SQLite)

### Kontakt Libraries (from database)

Internal:
- `/Users/Shared/Scarbee Rickenbacker Bass Library`
- `/Users/Shared/Session Guitarist - Electric Sunburst Deluxe Library`
- `/Users/Shared/Session Guitarist - Picked Acoustic Library`
- `/Users/Shared/Session Guitarist - Strummed Acoustic Library`
- `/Users/Shared/Session Guitarist - Strummed Acoustic 2 Library`

External:
- `/Volumes/External/kontakt_libraries/MOJO 2 Horn Section 2.0`
- `/Volumes/External/kontakt_libraries/Pedal Steel`
- `/Volumes/External/kontakt_libraries/Spitfire/*` (4 libraries)
- Plus 30+ more in `/Volumes/External/kontakt_libraries/`

### Guitarist Deep Dive

Guitarist has the richest preset library of any Sugar Bytes plugin:
- **186 patterns** across 11 genres (Ballad, Blues, Funky, Hard, Indie, Jazzy, Picking, Pop, Rock, Spacy, User)
- **65 chord sets** matching the pattern genres
- **186 sound presets** matching patterns
- **13 global presets** (one per genre + default)

Pattern files (.gpp), chord files (.gpc), and sound files (.gps) are binary but small (~2-5KB each).

The Picking category (26 patterns) is most relevant for folk/acoustic work.
The Indie category (18 patterns) bridges folk and rock.
The Rock category (28 patterns) is the largest.

### DAW Integration (Bitwig)

Bitwig supports:
- VST2, VST3, and AU plugins
- MIDI routing between tracks (for note generators → instruments)
- Note FX chains (for Consequence/Thesys before instruments)
- Modulation of plugin parameters via Bitwig modulators
- Plugin parameter automation
- FX chains with send/return routing

All Sugar Bytes plugins support MIDI CC mapping, meaning Bitwig modulators can control any parameter.

### Pedalboard CLI Workflow

```bash
# Scan a plugin's parameters
python scripts/scan_plugin.py WOW2

# Process audio through a plugin chain
python scripts/process_audio.py input.wav output.wav WOW2 cutoff=0.5 -- ValhallaRoom mix=0.3

# Explore Guitarist presets
python scripts/guitarist_explorer.py
```

## Research Sources
- PDF manuals: research/manuals/ (converted from Sugar Bytes app bundles)
- YouTube transcripts: research/youtube/ (downloaded via ytinfo)
- Genre guides: research/genre-guides/
