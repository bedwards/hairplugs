# Non-Sugar Bytes Plugin Catalog

All installed plugins (excluding Sugar Bytes) categorized and documented.

## Categorization Key

| Category | Description |
|---|---|
| `instruments` | Turns MIDI notes into audio (synths, samplers, drum machines) |
| `note-generators` | Generate MIDI/notes from nothing (arpeggiators, chord generators, sequencers) |
| `note-fx` | Transform MIDI notes (MIDI processors, note effects) |
| `audio-fx-tone` | Non-time-based audio effects (EQ, compression, saturation, distortion, filtering, dynamics) |
| `audio-fx-time` | Time-based audio effects (reverb, delay, chorus, flanger, phaser) |
| `master-chain` | Mastering tools (limiters, maximizers, metering, loudness) |

---

## Plugin Catalog

```json
{
  "instruments": [
    {
      "name": "AEBJ (Ample Ethno Banjo)",
      "developer": "Ample Sound",
      "standalone": true,
      "description": "Sampled virtual banjo instrument based on a Deering Sierra banjo with 9 articulations and 3.9 GB sample library."
    },
    {
      "name": "Bitspeek",
      "developer": "Sonic Charge",
      "standalone": false,
      "description": "Real-time pitch-excited linear prediction codec effect that resynthesizes audio through a simple oscillator/noise/filter architecture; responds to MIDI for pitched playback."
    },
    {
      "name": "DecentSampler",
      "developer": "Decent Samples",
      "standalone": true,
      "description": "Free sampler plugin and standalone app that plays sample libraries in the DecentSampler format (.dspreset/.dslibrary); now also supports built-in oscillators."
    },
    {
      "name": "HaNon B70",
      "developer": "LostIn70s",
      "standalone": true,
      "description": "Free Hammond B3 organ emulation with physical modeling of 91 tone wheels and Leslie 122 rotating speaker cabinet."
    },
    {
      "name": "Kontakt 7",
      "developer": "Native Instruments",
      "standalone": true,
      "description": "Industry-standard software sampler platform hosting thousands of sample libraries; previous major version."
    },
    {
      "name": "Kontakt 8",
      "developer": "Native Instruments",
      "standalone": true,
      "description": "Latest version of the industry-standard sampler with 900+ factory instruments, new Leap loop engine, Chords and Phrases tools."
    },
    {
      "name": "M-Tron Pro IV",
      "developer": "GForce Software",
      "standalone": true,
      "description": "Mellotron M400 emulation with 3.5 GB library, 200+ tape banks, 800+ presets, amp sim, and polyphonic aftertouch."
    },
    {
      "name": "Microtonic",
      "developer": "Sonic Charge",
      "standalone": false,
      "description": "100% synthetic drum and percussion synthesizer with 8 channels and built-in pattern-based drum machine engine; very low CPU."
    },
    {
      "name": "Play (Native Instruments)",
      "developer": "Native Instruments",
      "standalone": false,
      "description": "Series of easy-to-use sample-based instruments with curated presets and focused controls; various themed sound packs."
    },
    {
      "name": "Surge XT",
      "developer": "Surge Synth Team",
      "standalone": true,
      "description": "Free open-source hybrid synthesizer with 12 oscillator algorithms, extensive modulation, MPE/microtuning support, and built-in effects."
    },
    {
      "name": "Synplant",
      "developer": "Sonic Charge",
      "standalone": false,
      "description": "Genetic/organic synthesizer where sounds evolve like plants; Synplant 2 adds Genopatch machine-learning patch creation from audio samples."
    },
    {
      "name": "Synthesizer V Studio 2 Pro",
      "developer": "Dreamtonics",
      "standalone": true,
      "description": "AI vocal synthesis instrument that generates realistic singing voices from note and lyric input; runs fully offline with commercial-use licensed voices."
    }
  ],

  "note-generators": [
    {
      "name": "Captain Beat",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Drum machine with hundreds of rhythms and sounds; generates drum patterns and exports audio or MIDI per-channel."
    },
    {
      "name": "Captain Beat Epic",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Updated version of Captain Beat with expanded rhythm library and pattern generation."
    },
    {
      "name": "Captain Chords",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Chord progression generator that creates inspiring progressions with drag-and-drop MIDI export."
    },
    {
      "name": "Captain Chords Epic",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Updated chord progression generator with expanded features and integration with the Captain plugin suite."
    },
    {
      "name": "Captain Deep",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Bassline generator that creates bass patterns locked to your chord progression."
    },
    {
      "name": "Captain Deep Epic",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Updated bassline generator with expanded pattern library."
    },
    {
      "name": "Captain Melody",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Melody generator that writes melodies harmonically matched to your chord progressions."
    },
    {
      "name": "Captain Melody Epic",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Updated melody generator with expanded capabilities."
    },
    {
      "name": "Captain Play",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Real-time performance tool letting you play chords and melodies via computer or MIDI keyboard in any key."
    },
    {
      "name": "Captain Play Epic",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Updated real-time chord/melody performance tool."
    },
    {
      "name": "Pilot Arpeggio",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Knob-to-MIDI arpeggio generator for interactive, dynamic arpeggio pattern creation."
    },
    {
      "name": "Pilot Bass",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Knob-to-MIDI bassline generator for spontaneous bass pattern creation."
    },
    {
      "name": "Pilot Chords",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Knob-to-MIDI chord generator for interactive chord progression creation."
    },
    {
      "name": "Pilot Melody",
      "developer": "Mixed In Key",
      "standalone": false,
      "description": "Knob-to-MIDI melody generator for spontaneous melody creation."
    }
  ],

  "note-fx": [],

  "audio-fx-tone": [
    {
      "name": "BassDeluxe1 (Bass Deluxe)",
      "developer": "LostIn70s",
      "standalone": true,
      "description": "Free tube bass amplifier simulator with two independent channels, 9-band EQ per channel, 4 cabinet models, and built-in beatbox/looper."
    },
    {
      "name": "bx_greenscreamer",
      "developer": "Brainworx / Plugin Alliance",
      "standalone": false,
      "description": "Free emulation of the Ibanez TS808 Tube Screamer overdrive pedal with the signature JRC 4558D IC chip tone."
    },
    {
      "name": "Decapitator",
      "developer": "Soundtoys",
      "standalone": false,
      "description": "Analog saturation modeler with 5 hardware-modeled saturation styles, tone control, mix knob, and a Punish button for extreme drive."
    },
    {
      "name": "DynOne3",
      "developer": "Leapwing Audio",
      "standalone": false,
      "description": "Multiband parallel compressor with up to 5 bands, adaptive attack/release timing, and transparent musical dynamics processing."
    },
    {
      "name": "iZotope Neutron 4 Elements",
      "developer": "iZotope",
      "standalone": false,
      "description": "AI-powered channel strip with Assistant View for intelligent processing suggestions and tone-matching technology."
    },
    {
      "name": "soothe2",
      "developer": "oeksound",
      "standalone": false,
      "description": "Dynamic resonance suppressor that identifies and reduces problematic resonances in real-time; handles harshness, mud, sibilance, and boom."
    },
    {
      "name": "Surge XT Effects",
      "developer": "Surge Synth Team",
      "standalone": false,
      "description": "Free open-source effects plugin providing the effects section from Surge XT as a standalone effects processor (filters, distortion, etc.)."
    }
  ],

  "audio-fx-time": [
    {
      "name": "Comeback Kid",
      "developer": "Baby Audio",
      "standalone": false,
      "description": "Analog-flavored character delay with intuitive controls for a wide range of delay sounds from subtle to extreme."
    },
    {
      "name": "Permut8",
      "developer": "Sonic Charge",
      "standalone": false,
      "description": "12-bit digital delay with variable sample rate and programmable processor; produces glitch, bitcrushed, circuit-bent, and flanged effects."
    },
    {
      "name": "Valhalla Room",
      "developer": "Valhalla DSP",
      "standalone": false,
      "description": "True stereo algorithmic reverb with 12 original algorithms ranging from tight ambiences to vast modulated spaces; 0.1s to 100s decay."
    }
  ],

  "master-chain": [
    {
      "name": "iZotope Insight 2",
      "developer": "iZotope",
      "standalone": false,
      "description": "Comprehensive metering suite with loudness, spectrum, spectrogram, sound field, intelligibility, and history meters; stereo to 7.1.2 Atmos support."
    },
    {
      "name": "iZotope Ozone 10 Elements",
      "developer": "iZotope",
      "standalone": false,
      "description": "Streamlined AI-assisted mastering suite with essential mastering tools in a simplified interface."
    },
    {
      "name": "iZotope Ozone 11",
      "developer": "iZotope",
      "standalone": true,
      "description": "Full mastering suite with 13-17 tools (Standard/Advanced), Master Assistant, reference track comparison, and comprehensive mastering chain."
    },
    {
      "name": "Oxford Inflator",
      "developer": "Sonnox",
      "standalone": false,
      "description": "Increases perceived loudness and adds warmth/presence without squashing dynamic range or raising peak levels."
    }
  ],

  "utility": [
    {
      "name": "iZotope Relay",
      "developer": "iZotope",
      "standalone": false,
      "description": "Low-CPU utility plugin enabling inter-plugin communication between iZotope products for visual mixing, unmasking, and automated level balancing."
    },
    {
      "name": "iZotope RX 10 (all modules)",
      "developer": "iZotope",
      "standalone": true,
      "description": "Industry-standard audio repair suite with spectral editing, noise reduction, de-hum, de-click, and text navigation; standalone editor and DAW plugins."
    },
    {
      "name": "MTuner",
      "developer": "MeldaProduction",
      "standalone": false,
      "description": "Free chromatic tuner with monophonic and polyphonic modes, frequency detection (50Hz-2kHz), and note history log."
    },
    {
      "name": "WaveShell",
      "developer": "Waves",
      "standalone": false,
      "description": "Not a plugin itself; acts as a container/gateway that hosts all installed Waves plugins within DAWs."
    }
  ],

  "standalone-apps-not-plugins": [
    {
      "name": "Ableton Live 11 Suite",
      "developer": "Ableton",
      "standalone": true,
      "description": "Full-featured DAW with integrated instruments, effects, and Max for Live; Suite edition includes all built-in content."
    },
    {
      "name": "Bitwig Studio",
      "developer": "Bitwig",
      "standalone": true,
      "description": "Modular DAW with built-in instruments, effects, and a visual modulation system (The Grid)."
    },
    {
      "name": "Guitar Pro 8",
      "developer": "Arobas Music",
      "standalone": true,
      "description": "Tablature editor and score player for guitar, bass, and other stringed instruments with realistic audio playback."
    },
    {
      "name": "Renoise",
      "developer": "Renoise",
      "standalone": true,
      "description": "Tracker-based DAW with sample-based instruments, effects, and a unique vertical pattern editing workflow."
    },
    {
      "name": "REAPER",
      "developer": "Cockos",
      "standalone": true,
      "description": "Lightweight, highly customizable DAW with extensive routing, scripting (ReaScript), and broad plugin format support."
    },
    {
      "name": "Blender",
      "developer": "Blender Foundation",
      "standalone": true,
      "description": "Free open-source 3D creation suite for modeling, animation, rendering, compositing, and video editing (not audio-specific)."
    }
  ],

  "sample-libraries": [
    {
      "name": "Kontakt Libraries",
      "location": "/Volumes/External/kontakt_libraries",
      "description": "Various Kontakt-format sample libraries including acoustic instruments, guitar, banjo, and more. Loaded via Kontakt 7/8."
    },
    {
      "name": "M-Tron Pro Library",
      "location": "/Volumes/External/M-Tron Pro Library",
      "description": "Mellotron tape bank sample library for use with GForce M-Tron Pro IV."
    }
  ],

  "unknown-category": [
    {
      "name": "ArchitectAU",
      "developer": "Unknown",
      "standalone": "unknown",
      "description": "Could not identify this plugin. No matching results found in plugin databases. May be a custom/obscure AU plugin or a component of another application."
    }
  ]
}
```

## Notes

- **Bitspeek** is categorized as `instruments` because while it processes audio input, its primary creative use is resynthesizing audio through MIDI-controllable oscillators, effectively turning it into a playable instrument.
- **Captain Beat** is categorized as `note-generators` rather than `instruments` because its primary output is MIDI drum patterns (exportable as MIDI), even though it includes built-in drum sounds for preview.
- **Captain Play** and the **Pilot** series are categorized as `note-generators` because they generate MIDI note output for other instruments to play.
- **DynOne3** is categorized as `audio-fx-tone` rather than `master-chain` because despite mastering use cases, its primary function is multiband compression (a dynamics/tone-shaping tool).
- **Oxford Inflator** is categorized as `master-chain` because its primary use case is increasing perceived loudness on master bus or final mixes.
- **iZotope RX 10** is placed in `utility` as it is primarily an audio repair/restoration tool rather than a creative effect.
- **WaveShell** is a container/wrapper, not a plugin itself. The actual Waves plugins it hosts are not individually listed here since they were not enumerated.
- **ArchitectAU** could not be identified through web searches. It may be worth checking `/Library/Audio/Plug-Ins/Components/` for the actual component file to determine its origin.
- The `note-fx` category is currently empty -- none of the installed non-Sugar Bytes plugins are pure MIDI effect processors.
- **Surge XT** appears in `instruments` (the synth) and **Surge XT Effects** appears in `audio-fx-tone` (the effects-only version) as they are separate plugins.
