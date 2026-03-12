# Hairplugs - Audio Plugin Knowledge Base & Hacking Toolkit

## Project Purpose
Organized reference and CLI hacking toolkit for Brian's audio plugin collection, optimized for Bitwig Studio workflow.

## Directory Structure
```
├── instruments/          # MIDI → Audio (synths, samplers, drum machines)
├── note-generators/      # Nothing → MIDI (arpeggiators, sequencers, chord generators)
├── note-fx/              # MIDI → MIDI (note effects, MIDI processors)
├── audio-fx-tone/        # Audio → Audio, non-time-based (EQ, compression, saturation, filtering, dynamics)
├── audio-fx-time/        # Audio → Audio, time-based (reverb, delay, chorus, flanger, phaser)
├── master-chain/         # Mastering tools (limiters, maximizers, metering, loudness, analysis)
├── research/             # Raw research data
│   ├── manuals/          # PDF manuals converted to markdown (pymupdf4llm)
│   ├── youtube/          # ytinfo JSON transcripts + markdown summaries
│   └── genre-guides/     # Per-genre setup guides
├── presets/              # plugctl preset storage (JSON params + binary blobs)
│   └── <vendor>/<plugin>/  # e.g. sugar-bytes/wow2/
├── scripts/              # Python scripts for plugin hacking
│   └── plugctl.py        # CLI for VST3 preset management
└── experiments/          # Quick-start experiment setups
```

## Signal Flow Mental Model
```
[Note Generator] → [Note FX] → [Instrument] → [Tone FX] → [Time FX] → [Master Chain]
```

## Key Conventions
- One entry per plugin regardless of install format (AU/VST/VST3)
- Flat hierarchy: top-level dirs are the five camps + master-chain
- Each plugin gets a markdown file in its camp directory
- No secrets/serial numbers/license keys committed
- DAW context: Bitwig Studio
- Use pedalboard (Python) for CLI plugin hacking - most VST3 plugins load headlessly

## Brian's Musical Context
- Primary: acoustic guitar, banjo, mandolin (folk / new folk / modern folk)
- Folk rock: + drums, electric bass
- Alt country: + electric guitar
- Folktronica: + electronic elements
- Pure electronic: chill vibes, experimental
- Classic rock: + Hammond organ
- Indie rock: + electric guitar + electronic elements

## Plugin Hacking
- `pedalboard` Python package can load VST3 plugins and expose all parameters
- Sugar Bytes presets are binary format (.sbd, .sbcy, .sbb, .sbep, .wow) in ~/Documents/Sugar Bytes/
- Kontakt library database: ~/Library/Application Support/Native Instruments/Kontakt 8/komplete.db3
- Most Sugar Bytes plugins have standalone apps at /Volumes/Macintosh HD/Applications/Sugar Bytes/

## plugctl — VST3 Preset CLI
```
plugctl ls                                # List all VST3 plugins
plugctl ls <plugin>                       # List saved presets
plugctl scan <plugin> [-j|--json]         # Show params + values
plugctl init <plugin>                     # Save default state as _init
plugctl snap <plugin> <name> [-m "msg"]   # Save current state
plugctl load <plugin> <name>              # Restore state from preset
plugctl diff <plugin> <a> <b>             # Compare two presets
plugctl tweak <plugin> <src> <dst> p=v .. # Fork + modify params
plugctl export <plugin> <name|-a|--all>   # Export to plugin preset browser
```
- Installed at `~/.local/bin/plugctl` (symlink to `scripts/plugctl.py`)
- Plugin names are short (`WOW2`, `Thesys`), resolved case-insensitively
- Presets stored as `.json` (version-controlled params) + `.blob` (gitignored binary state)
- Export copies blob to `~/Library/Audio/Presets/<Vendor>/<Plugin>/` for plugin's own preset browser
- Export does NOT work for Sugar Bytes plugins — they use proprietary formats (.scg/.sbc/.sbs) in `~/Documents/Sugar Bytes/<plugin>/`
- Sugar Bytes presets are useful as plugctl snapshots only (`plugctl load`)
- DrumComputer crashes in pedalboard — use in DAW only

## File Locations
- AU Components: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/Components/
- VST: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST/
- VST3: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3/
- Sugar Bytes data: ~/Documents/Sugar Bytes/
- Kontakt libraries (external): /Volumes/External/kontakt_libraries/
- Kontakt libraries (internal): /Users/Shared/Session Guitarist-*, /Users/Shared/Scarbee*
- M-Tron Pro libraries: /Volumes/External/M-Tron Pro Library/
