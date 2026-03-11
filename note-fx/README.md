# Note FX (MIDI → MIDI)

Plugins that transform MIDI notes — arpeggiators, sequencers, chord processors. Notes in, modified notes out.

## Sugar Bytes

### Consequence
MIDI arpeggiator and chord sequencer. Takes incoming MIDI notes and creates complex arpeggiated patterns, chord voicings, and rhythmic sequences.
- **Standalone**: Yes
- **Pedalboard**: 88 params (masterlevel, masterattack, masterrelease, osc1_trigmode...)
- **Presets**: ~/Documents/Sugar Bytes/Consequence/
  - Global Presets/
  - Sequences/
  - Chord Banks/
  - Sounds/ (has a built-in synth engine too)
- **Best for**: Turning simple chords into complex arpeggios, folktronica patterns, rhythmic note sequences
- **Key feature**: Built-in sound engine means it can also output audio directly

### Thesys
Step sequencer and note effect. Creates patterns from incoming MIDI with step-sequenced pitch, velocity, gate, and modulation.
- **Standalone**: Yes
- **Pedalboard**: 47 params (root_key, scale, midi_out_octave, midi_out_transpo, swingfactor...)
- **Presets**: ~/Documents/Sugar Bytes/Thesys/
  - Global Presets/
  - Synth Presets/ (has built-in synth)
- **Best for**: Rhythmic note patterns, techno sequences, experimental note manipulation
- **Key feature**: Can output MIDI to other instruments or use its built-in synth

## Signal Chain Position

```
[Note Generator] → [Consequence/Thesys] → [Instrument]
                    ↑ transforms notes     ↑ plays result
```

Both Consequence and Thesys have built-in synth engines, so they can operate as self-contained instruments too. But their primary power is as note processors in a chain.
