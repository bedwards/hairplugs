# Hairplugs

Audio plugin knowledge base, hacking toolkit, and quick-start experiment library for Bitwig Studio.

## Signal Flow Model

```
┌──────────────┐   ┌──────────┐   ┌─────────────┐   ┌───────────────┐   ┌───────────────┐   ┌──────────────┐
│ Note         │──▶│ Note FX  │──▶│ Instruments  │──▶│ Tone FX       │──▶│ Time FX       │──▶│ Master Chain │
│ Generators   │   │          │   │              │   │ (non-time)    │   │ (time-based)  │   │              │
│              │   │ MIDI→MIDI│   │ MIDI→Audio   │   │ Audio→Audio   │   │ Audio→Audio   │   │ Audio→Audio  │
└──────────────┘   └──────────┘   └─────────────┘   └───────────────┘   └───────────────┘   └──────────────┘
```

## Plugin Inventory

### Instruments (MIDI → Audio)
| Plugin | Maker | Standalone | Pedalboard | Description |
|--------|-------|-----------|------------|-------------|
| Aparillo | Sugar Bytes | Yes | 162 params | Orbital FM synthesizer |
| Cyclop | Sugar Bytes | Yes | 146 params | Bass synthesizer with wobble |
| DrumComputer | Sugar Bytes | Yes | crash | Drum synthesizer & sequencer |
| Factory | Sugar Bytes | Yes | 231 params | Hybrid wavetable synthesizer |
| Guitarist | Sugar Bytes | Yes | 81 params | Virtual guitarist (strumming engine) |
| Obscurium | Sugar Bytes | Yes | 130 params | Spectral synthesizer |
| Unique | Sugar Bytes | Yes | 155 params | Unison synthesizer |
| Kontakt 8 | Native Instruments | No | N/A | Sampler (loads NKI libraries) |
| DecentSampler | Decent Samples | Yes | 1 param | Free sampler |
| M-Tron Pro IV | GForce | Yes | 116 params | Mellotron emulation |
| Surge XT | Surge Synth Team | Yes | 775 params | Open-source hybrid synthesizer |
| Synthesizer V Studio 2 | Dreamtonics | Yes | TBD | AI vocal synthesizer |

### Note Generators (Nothing → MIDI)
| Plugin | Maker | Description |
|--------|-------|-------------|
| Captain Chords (Epic) | Mixed In Key | Chord progression generator |
| Captain Melody (Epic) | Mixed In Key | Melody generator |
| Captain Deep (Epic) | Mixed In Key | Bassline generator |
| Captain Beat (Epic) | Mixed In Key | Drum pattern generator |
| Captain Play (Epic) | Mixed In Key | Performance tool |
| Pilot Chords | Mixed In Key | Chord generator (newer) |
| Pilot Melody | Mixed In Key | Melody generator (newer) |
| Pilot Bass | Mixed In Key | Bass generator (newer) |
| Pilot Arpeggio | Mixed In Key | Arpeggio generator (newer) |

### Note FX (MIDI → MIDI)
| Plugin | Maker | Standalone | Pedalboard | Description |
|--------|-------|-----------|------------|-------------|
| Consequence | Sugar Bytes | Yes | 88 params | MIDI arpeggiator & chord sequencer |
| Thesys | Sugar Bytes | Yes | 47 params | Step sequencer & note FX |

### Audio FX — Tone (non-time-based)
| Plugin | Maker | Standalone | Pedalboard | Description |
|--------|-------|-----------|------------|-------------|
| WOW2 | Sugar Bytes | Yes | 86 params | Filter / vowel / modulation |
| Artillery2 | Sugar Bytes | Yes | 1025 params | Multi-effect processor |
| Turnado | Sugar Bytes | Yes | 253 params | Real-time multi-effect (8 dictator knobs) |
| Egoist | Sugar Bytes | Yes | 61 params | Slicer / beat mangler |
| Looperator | Sugar Bytes | Yes | 116 params | Loop effect sequencer |
| Effectrix | Sugar Bytes | Yes | 118 params | Step-sequenced multi-effect |
| Decapitator | Soundtoys | No | TBD | Analog saturation / distortion |
| bx_greenscreamer | Plugin Alliance | No | 5 params | Tube Screamer overdrive |
| Oxford Inflator | Sonnox | No | TBD | Loudness / harmonics enhancer |
| soothe2 | oeksound | No | 56 params | Dynamic resonance suppressor |
| DynOne3 | Leapwing | No | 114 params | Multiband dynamics |
| Surge XT Effects | Surge Synth Team | Yes | 13 params | Open-source effect suite |

### Audio FX — Time (time-based)
| Plugin | Maker | Standalone | Pedalboard | Description |
|--------|-------|-----------|------------|-------------|
| Comeback Kid | Baby Audio | No | 23 params | Character delay |
| Valhalla Room | Valhalla DSP | No | 23 params | Algorithmic reverb |

### Master Chain
| Plugin | Maker | Description |
|--------|-------|-------------|
| iZotope Ozone 11 | iZotope | Full mastering suite (17 modules) |
| iZotope Ozone 10 Elements | iZotope | Simplified mastering |
| iZotope Insight 2 | iZotope | Metering & analysis |
| iZotope Neutron 4 Elements | iZotope | Channel strip |
| iZotope Relay | iZotope | Gain staging / routing |

### Audio Repair (Utility)
| Plugin | Maker | Description |
|--------|-------|-------------|
| iZotope RX 10 | iZotope | Audio repair suite (15 modules) |

## Kontakt Libraries

### Internal Drive (/Users/Shared/)
- Scarbee Rickenbacker Bass
- Session Guitarist - Electric Sunburst Deluxe
- Session Guitarist - Picked Acoustic
- Session Guitarist - Strummed Acoustic (1 & 2)

### External Drive (/Volumes/External/kontakt_libraries/)
- 8Dio Misfit series (toy instruments, unusual instruments)
- 8Dio Postapocalyptic Guitar, Songwriting Guitar v2
- 8Dio Mandolin + Strummer
- Acou6tics, Pedal Steel, RealiBanjo, RealiDrums
- Realivox Blue, Realivox Ladies, RealiWhistle
- MOJO 2 Horn Section
- Spitfire (Solo Strings, Solo Violin, Percussion, The Grange)
- The Fiddle, The Mandolin, The Resonator
- WURL-e Studio, Soundiron Theremin+, SONGBIRD VIRTUOSO

### M-Tron Pro Libraries (/Volumes/External/M-Tron Pro Library/)
- Streetly Tapes Vol 1-6, M300, Violins & Vox, SFX Console
- ChamberTron, OrchesTron, OptiTron, IsolationChoir
- Alex Ball Expansion, Hainbach Expansion

## CLI Hacking

Most plugins can be loaded and controlled headlessly via Python pedalboard:

```python
from pedalboard import load_plugin

# Load any VST3 plugin
wow2 = load_plugin("/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3/WOW2.vst3")

# Read/write any parameter
print(wow2.cutoff)        # 1.0
wow2.cutoff = 0.5
wow2.resonance = 0.7

# Process audio
import numpy as np
audio = np.random.randn(44100).astype(np.float32)
output = wow2(audio, sample_rate=44100)
```

## Standalone Apps
All 15 Sugar Bytes plugins at `/Volumes/Macintosh HD/Applications/Sugar Bytes/`
Plus: Surge XT, DecentSampler, M-Tron Pro IV, Synthesizer V Studio 2 Pro

## DAWs Installed
- **Bitwig Studio** (primary)
- Ableton Live 11 Suite
- REAPER
- Renoise
