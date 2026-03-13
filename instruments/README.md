# Instruments (MIDI → Audio)

Plugins whose primary function is converting MIDI notes into audio sound.

## Sugar Bytes

### Aparillo
Orbital FM synthesizer with unique orbiter-based modulation. Two operators with FM synthesis, built-in arpeggiator, and extensive modulation matrix. Great for evolving pads, metallic textures, bells, and experimental tones.
- **Standalone**: Yes
- **Pedalboard**: 162 params (level, octave, detune, orbiter_x/y, ratio, fm_amt...)
- **Presets**: ~/Documents/Sugar Bytes/Aparillo/Presets/ (.sbd files)
- **CC Maps**: ~/Documents/Sugar Bytes/Aparillo/CC Maps/
- **Best for**: Folktronica pads, experimental textures, ambient beds

### Cyclop
Bass-focused synthesizer with wobble engine. Two oscillators with extensive modulation, built-in effects, and the signature wobble knob for dubstep/bass music.
- **Standalone**: Yes
- **Pedalboard**: 146 params (master_level, wobble_knob, sound_knob, fx_knob...)
- **Presets**: ~/Documents/Sugar Bytes/Cyclop/Presets/ (.sbcy files)
- **Samples**: ~/Documents/Sugar Bytes/Cyclop/Samples/
- **Best for**: Electronic bass, folktronica low end, experimental bass textures

### DrumComputer
Synthesized drum machine with 8 channels of additive/subtractive synthesis. Generates drums from synthesis rather than samples. Built-in sequencer.
- **Standalone**: Yes
- **Pedalboard**: Crashes (use in DAW only)
- **Presets**: ~/Documents/Sugar Bytes/DrumComputer/Presets/ (.sbb files)
- **Wavetables**: ~/Documents/Sugar Bytes/DrumComputer/Wavetables/
- **Best for**: Electronic drums, folktronica beats, experimental percussion

### Factory
Hybrid wavetable synthesizer. Combines wavetable, FM, and subtractive synthesis with a powerful modulation system.
- **Standalone**: Yes
- **Pedalboard**: 231 params (master_volume, morph, filter_cutoff, filter_resonance...)
- **Presets**: ~/Documents/Sugar Bytes/Factory/Presets/ (.sbep files)
- **Wavetables**: ~/Documents/Sugar Bytes/Factory/Wavetables/
- **Best for**: Pads, leads, electronic textures

### Guitarist
Virtual acoustic & electric guitarist with strumming engine. Plays chords with realistic strumming patterns, amp modeling, and built-in effects.
- **Standalone**: Yes
- **Pedalboard**: 81 params (amp_volume, amp_drive, model_x_toneswit, chorus_rate...)
- **Patterns**: ~/Documents/Sugar Bytes/Guitarist/Patterns/ (Ballad/Blues/Funky/Hard/Indie/Jazzy/Picking/Pop/Rock/Spacy/User)
- **Chords**: ~/Documents/Sugar Bytes/Guitarist/Chords/ (same categories)
- **Sounds**: ~/Documents/Sugar Bytes/Guitarist/Sounds/ (same categories)
- **Best for**: Folk guitar backing, singer-songwriter demos, alt country rhythm guitar

### Obscurium
Spectral synthesizer with a unique XY matrix for sound exploration. Creates sounds through spectral manipulation rather than traditional oscillators.
- **Standalone**: Yes
- **Pedalboard**: 130 params (master_level, shift_interpolat, arp_min/max...)
- **Presets**: ~/Documents/Sugar Bytes/Obscurium/Presets/
- **Assignments/CC Maps**: ~/Documents/Sugar Bytes/Obscurium/
- **Best for**: Ambient textures, experimental sounds, evolving pads

### Unique
Unison synthesizer with massive detuning capabilities. Multiple voices with independent detuning for huge, wide sounds.
- **Standalone**: Yes
- **Pedalboard**: 155 params (master, osc_1_level, osc_1_pan, voice_mode...)
- **Presets**: ~/Documents/Sugar Bytes/Unique/Presets/
- **Best for**: Huge pads, supersaw leads, electronic anthems

## Other Instruments

### Kontakt 8 (Native Instruments)
Industry-standard sampler. Loads NKI instrument libraries. Not hackable via pedalboard but has extensive scripting via KSP.
- **Libraries on internal**: Session Guitarist (Electric Sunburst Deluxe, Picked Acoustic, Strummed Acoustic 1&2), Scarbee Rickenbacker Bass
- **Libraries on external**: 30+ including 8Dio guitars, mandolins, banjos, Spitfire strings, Pedal Steel, MOJO Horns
- **Database**: ~/Library/Application Support/Native Instruments/Kontakt 8/komplete.db3

### M-Tron Pro IV (GForce)
Mellotron emulation with tape-based sounds. Two layers with independent controls.
- **Standalone**: Yes
- **Pedalboard**: 116 params (tone, master_pitch, master_volume, tape_rewind...)
- **Libraries**: /Volumes/External/M-Tron Pro Library/ (Streetly Tapes Vol 1-6, ChamberTron, OrchesTron, etc.)
- **Best for**: Classic rock organ/strings/choir, vintage textures

### Surge XT (Surge Synth Team)
Open-source hybrid synthesizer. Wavetable, FM, subtractive, additive all in one. Extremely deep.
- **Standalone**: Yes
- **Pedalboard**: 775 params
- **Best for**: Any electronic sound, from subtle to extreme

### DecentSampler
Free, open-source sampler that loads .dspreset files. Community library of free instruments.
- **Standalone**: Yes
- **Pedalboard**: 1 param (bypass only)

### Synthesizer V Studio 2 Pro (Dreamtonics)
AI-powered vocal synthesizer. Creates realistic singing voices from MIDI + lyrics.
- **Standalone**: Yes
- **Best for**: Vocal harmonies, choir parts, vocal experimentation
