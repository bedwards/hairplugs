# Thesys - YouTube Research Summary

## Plugin Overview
Thesys is a MIDI step sequencer plugin by Sugar Bytes for building patterns, generating pitch sequences, and performing live. It features an internal synthesizer and can route MIDI output to external instruments. Functions as both a composition tool and a performance instrument.

## Videos Analyzed
1. **Thesys Tutorial Part 1** - Sugar Bytes - [Watch](https://www.youtube.com/watch?v=RtHd4leqIaE)
2. **Thesys Tutorial Part 2** - Sugar Bytes - [Watch](https://www.youtube.com/watch?v=-yMD7yqsU0I)
3. **Thesys Tutorial Part 3** - Sugar Bytes - [Watch](https://www.youtube.com/watch?v=GEpuTJk2AD4)

## Key Features and Capabilities

### Pattern Building (Part 1)
- Default preset in user folder provides clean starting point
- Reset buttons per sequencer section for individual resets
- Set root note and scale type to constrain all notes to key
- Velocity sequencer controls note levels; mute steps via bottom row
- Gate time sequencer controls note length per step
- Record notes via external MIDI keyboard (live or step mode)

### Loop Bar System
- Shorten, lengthen, and shift the loop bar per sequencer
- Acts as selector for copy/paste operations
- **Global mode**: same loop length for all sequencers
- **Individual mode**: each sequencer gets its own loop bar with independent length, start, and end points for polyrhythmic variety

### Pattern Management
- Multiple patterns for different song sections
- Global copy/paste to duplicate all sequencers between patterns
- Shift pitch sequencer up/down intervals (fourths, fifths) for harmonic progression
- Pattern sequencer sets playback order and repeat counts

### Trigger Modes (Part 2)
- **Host**: starts/stops with DAW transport
- **Note Toggle**: first MIDI note starts, second stops
- **Note On**: plays only while MIDI note is held
- **Trigger By** setting: pitch keys (for transposing) or pattern keys (for switching parts)
- Play button for manual start independent of trigger mode

### Live Performance
- Transpose sequences in real-time via MIDI keyboard pitch keys
- Switch patterns on-the-fly with pattern keys
- Apply actions in real-time regardless of trigger mode
- Set trigger mode to Host for uninterrupted playback during MIDI input

### Performance Sequencer (Part 3)
- **Octave Row**: transpose 1-2 octaves up/down per step
- **Pitchbend Row**: 20 pitchbend shapes (bends, shakes)
- **Chord Row**: harmonize patterns (16 chord types, see manual appendix)
- **Roll Row**: 16 note roll patterns for rhythmic variety (effective at slow tempos)
- **Random Row**: randomize any single parameter per step

### Randomization
- **Full Random**: completely randomize all values (dice roll)
- **Mutate**: only changes existing filled values, leaves empty steps alone
- Min/max random values configurable in global settings row
- Especially useful for velocity, pitch, and gate randomization

## Workflow Tips and Tricks
- Shift-click and drag for fast series editing in performance sequencer
- Right-click a step to reset it (works in all performance rows)
- Command-click to step through choices in each row
- Use individual loop lengths for polyrhythmic complexity
- Build harmonic progressions by copying patterns and shifting pitch
- Use roll patterns as pickups to strong beats
- Three-hit rolls create interesting 2-against-3 rhythms
- Mouse over any element for tooltips; manual accessible from interface

## Creative Uses
- Generating scale-aware melodic sequences for any instrument
- Building harmonic song structures across multiple patterns
- Live performance transposition and pattern switching
- Creating polyrhythmic sequences with independent loop lengths
- Adding humanized feel with random velocity per step
- Driving external synthesizers with complex evolving MIDI patterns
