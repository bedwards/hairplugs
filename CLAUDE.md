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
├── scripts/              # Python scripts for plugin hacking
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

## File Locations
- AU Components: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/Components/
- VST: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST/
- VST3: /Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3/
- Sugar Bytes data: ~/Documents/Sugar Bytes/
- Kontakt libraries (external): /Volumes/External/kontakt_libraries/
- Kontakt libraries (internal): /Users/Shared/Session Guitarist-*, /Users/Shared/Scarbee*
- M-Tron Pro libraries: /Volumes/External/M-Tron Pro Library/
