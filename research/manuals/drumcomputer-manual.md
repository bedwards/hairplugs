### **RUM OMPUTER**
# **D C**
### **USER MANUAL**



1






What is DrumComputer 3
Overview 4
Get Started 5
User Interface 6
Sound Pages 7
Resonator 9
Wavetable/Analogue Oscillator 11
Resynth/Sampler 14
Filter 15
Insert FX 15
Modulation Section 16
Global Section 19
Kit Page 20
Sequencer Page 24
Pattern, Mute & Mapping 29
Mixer 33
Remix Feature 36
Header & Settings 38
MIDI CC Assignments 42
Host Integration 43
Installation/Uninstallation 45
Sounddesigner 46
Contact 47



2


**What is DrumComputer?**


Congratulations on your purchase of DrumComputer.
Please read this manual carefully, in order to get the best out of this outstanding Synthesizer.

In essence, DrumComputer is a drum machine with 8 individual sound engines, including everything you might think of when it comes to
drum sounds and patterns. And it not only synthesizes sounds, DrumComputer also is capable of randomizing kits, patterns and fills.

When it comes to synthesizing a drum sound, there are no compromizes made. 3 synthesis layers (analog resonator,
wavetable/analogue, resynth), super flexible modulations and effects plus the awesome randomizer deliver an incredible variety of
possible sounds.

The wave import for Wavetable and Resynth Oscillators ensure a never ending source of timbres.

The sequencer is packed with features and provides fully consistent MIDI drag and drop.

The AutoFill feature creates intelligent fills by juggling existing triggers around and creating little roll figures, spiced up by pitch bends
and filter/reverb modulations, all included in the exported MIDI file.

With configurable audio and MIDI single outs, DrumComputer is ready for all mixing situations.

We hope you enjoy using DrumComputer as we enjoyed making it, and we wish you a lot of fun defining the drum sounds of tomorrow.



3


## Overview

DrumComputer‘s user interface is divided into six main sections:

Sound Pages There are 8 sound engines available which make out a kit. Each sound engine consists of 3 synthesis engines:
Resonator, Wavetable/Analogue and Noisetable . The synth engine also delivers a multimode filter, equalizer,
compressor with sidechain from the other engines, 2 distortion modes (overdrive and digital reduction), rolls
(use the keyzone for controlling the roll speed), 2 modulation generators (can be envelope, lfo or random), a
modulation matrix and a flam engine (makes three triggers out of one, good for claps).

Kit Page Here you have control over your kit. You might randomize single sounds or a full kit using profiles, enjoy
control over global pitch and decay and have the " modify " knob as a manual modulator.
Here you also find the master fx, consisting of a transient shaper, compressor and maximizer, plus tube or
tape distortion.

Sequencer Page Here you can design up to 16 patterns and enjoy many cool features like humanizing, step delay and a great
modulation sequencer section.

Mixer Here you find all your levels, send levels, pan controls and send effects, namely Room and Hall.
The remix control covers lots of groove and fun as well.

Mapping section Map the individual drum engines to MIDI keys and copy/paste or sequence your patterns.

Options Here you set your overall preferences, but also assign the mute group and MIDI/audio out assignments.



4


## Get Started

DrumComputer can be triggered per MIDI notes or per internal
sequencer. Send MIDI notes from C0 upwards to trigger the drums
manually or activate the Play button to start the internal sequencer.


**Presets**

There are global presets (top bar menu) which contain everything, and
there are Cell presets which contain the sound of a single engine.


**Sounds**

To get new sounds quickly, hit the Make Kit button. This will randomize
sounds using profiles for certain drum categories. Hit the buttons
repeatedly until you like the kit. You can also use the individual
randomize buttons in the drum channels.


**Making Fills**

Use the Remix slider to create crazy fills without any further action. Set it to "autofill" and enjoy fills coming in automatically.

**Mapping/Zones**

You have total freedom when it comes to mapping drum sounds to your keyboard. Just click the Mixer/Mapping section button (colored button
with the arrow) to enter the keyboard mapping. Drag the numbers to the desired keys.



5


# **User Interface**

Sound Pages


Kit Page


Sequencer Page


Pattern, Mute & Mapping


Mixer


Remix Feature


Header


Settings


MIDI CC Assignment



6


### **Sound Pages**

**Create punchy and complex drum sounds with 8 individual sound engines.**



7


Pitch and Fine-Tune

Pitch is displayed in numbers. If you are not familiar with this,
the note C is represented as 24, 36, 48, 60, 72, 84, 96, 108, 120.


Level
Individual volume control for each oscillator.

Filter
Activate this button to assign the oscillator to the global multimode filter.

Pitch-Mod
The level-envelope (controlled with decay parameter) is used to generate
a pitch-modulation.

Decay
The progressive reduction in amplitude of a sound over time.

Velocity
Activate this button to have a velocity-sensitive pitch envelope.


On/Off
Deactivate the speaker button of an oscillator to mute its audio signal.

Scroll up and down your mousewheel to step/scroll through the values/settings of all relevant parameters and configuratios.
Shift-click on a knob and move up and down your mouse to edit for finer adjustments.


8

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


A wonderful recipe, inspired by the 808 signal flow, a self oscillating multi mode filter.
Since we have a resonating circuit here, it requires an exciter to get going. The exciter usually is a very short signal,
like the moment when the stick hits the drum membrane.
There are 6 exciter modes available:it


er

Env
The internal exciter-envelope sends an impulse to the filter, making it resonate as an organic sine wave.

Noise + Env
Noise is added to the exciter-envelope, bringing you the ingredients for snares and classic analog noise cymbals
and hihats.

Wavetable
The audio signal coming from the Wavetable Oscillator is used as exciter. It‘s an invitation to experiment with different timbres.

Resynth
The audio signal coming from the Resynth Oscillator is used as an exciter, providing an endless range of noise colors for incredible snare,
cymbal and percussion sounds.

Parabol
Adds a bit of realism and softness to the drum impact.

Parabol + Noise
Is a classic choice for snares or can add some air to other drum sounds when combined with a lowpass filter.

The parameter set of the Resonator is a bit unusual when it comes to envelopes and the real length of a sound. While the Decay parameter in the
other oscillators really controls the overall length of the sound, in the Resonator the parameters Resonance and Decay are somewhat woven into
each other. When making a snare drum, you will use a noisy exciter, and decay will control the length of noise, while resonance controls the
length of body.


9

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Resonance
Determines the resonance of the self oscillating filter, and so controls the overall length of the resulting sine
wave.

Partials
The Resonator Oscillator contains 3 voices, so it can generate partials. Partials are frequencies that are usually
non-harmonic and determine the shape and material of the drum you are creating. If the Partials control is set to
zero, no partials are added. The higher you turn this parameter, the higher the partials frequencies will get, while
the level of the partials will increase with a steep curve.

Tone
The Tone parameter controls a 2 Pole low-pass filter with a hint of resonance. It allows for dialing in just the right
amount of brightness with a sharpened edge.


Filter Type
The Resonator is based on a self oscillating 12db/oct multi mode filter. The Resonator Pitch determines the
cutoff frequency, which is important to know when using band-pass and low-pass modes, as these pass noise
only at higher frequency settings.
With the Filter Type menu you can select the filter type:
High-pass: Will always let noise pass through, so this should be used for snares and cymbals.
Band-pass: Passes only the Pitch (Cutoff) frequency, should be used for kicks, persussions or snare body.
Low-pass: Eliminates frequencies above the Pitch (Cutoff) and offers interesting kick timbres.


10

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


A Wavetable Oscillator uses a chain of single-cycle waveforms and morphs between them, providing awesome spectral changes. Creating a
drum sound, you would use the Wavetable Osc to generate the body. The provided wavetables usually start at waveforms with few harmonics
and go to more complex waveforms with many harmonics. In order to create punch, you would modulate the Wave parameter with a short
envelope, so your punch has as a lot of spectrum, as you would do with a pitch envelope. The Analogue Oscillator works exactly like the
wavetable oscillator, but with a fixed set of virtual analogue waveforms.


Wave
Here you select the position within your wavetable. Give it a short envelope for snappy attacks.
Usually you will modulate this parameter with an envelope, so it is already assigned to MG2 by the sound
randomizer.


FM
The Wavetable Osc interacts with the Resonator Osc. The waveform of the Resonator Osc is used as a
Frequency Modulator for the Wavetable Osc. Since the Resonator puts out a decaying sound, the Fm
Modulator is never static and might even be absent when the Resonator has decayed out quicker than
the Wavetable.


RM
Bipolar Ringmodulation. The Wavetable includes a Sine Oscillator which is used to modulate the
amplidude of the Wavetable Osc. The bipolar RM parameter determines the Sine Osc´s frequency ratio in
relation to the Wavetable´s pitch. The RM pitch works as follows:

-100% = -2 octaves
-50% = -1 octave
0 = inactive
50% = +1 octave
100% = +2 octaves


Sound Pages       Kit Page       Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents11


Pitch Mod/Decay


The internal decay-envelope can be used to modulate Pitch directly, and always controls the amplitude.
There are 8 envelope shapes available:


Envelope Shapes



Natural
The natural, exponential envelope shapes of an analogue decayenvelope.


Ping
Inspired by Vactrol-driven low-pass gates, we have a strong punch
in the beginning and a long decay in the end.


Superping
Taken the idea of a Vactrol-based envelope a bit further for even
punchier attack and natural decay.


Hold
Just a DC offset is being used as envelope, good for gated snares.


Soft
A special algorithm forms a sweet round curve which can be
compared to a decay-envelope that went through a low-pass
filter.



A/D
A/D is an attack/decay envelope, where the time determined by the
Decay parameter is divided into attack time and decay time.


There are 3 different blends of attack and decay time modes available:


1/3: If the Decay parameter would show 100ms, the envelope
would perform 33ms of attack time and 66ms of decay time.


1/1: If the Decay parameter would show 100ms, the envelope
would perform 50ms of attack time and 50ms of decay time.


3/4: If the Decay parameter would show 100ms, the envelope
would perform 66ms of attack time and 33ms of decay time.



12

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Invert Button


Activate this button to invert the envelope. While a decay-envelope is all about fading out, the inverted version will just fade in and then
jump back to zero. The inversion process also inverts the curve shapes which shows interesting results.

Load/Import Sample


The best thing about the Wavetable Oscillator is that it will convert any wave into a wavetable.

Open the wavetable menu and click IMPORT or directly drag and drop a Wav files into the wavetable menu.

Wav files of any kind can be loaded.
In the ideal case you prepared a waveform that performs a shift from low spectrum to high spectrum.

We will detect the included pitch and provide a wavetable containing 16 waveforms, that have been evenly picked out of the whole source
waveform.


The resulting wavetables will be auto-saved into a user folder that will be generated.
After 32 wavetables, the next user folder will be created (user1, user2 etc).


13

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


While the Wavetable Osc is a never ending source of complex and surprising timbres,
the Analog Osc will provide you with the classical analog waveforms.
Sine and Triangle for drum shells, Saw and Pulse for edgy tones and sharp attacks.

The Wave parameter lets you morph from one waveform to another, while the final phase
of the parameter performs a pulse width modulation on the pulse osc.
So for a classic pwm sound, you would set the Wave control to pulse and then add an lfo to modulate
the pulse width.

FM and RM work the same way as in the Wavetable Oscillator, where the FM source is the Resonator
and the RM source is an internal sine osc.


Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents14


The Resynth Osc is the non-harmonic version of a Wavetable Oscillator.
It just contains one single waveform, and it also provides conversion of any waveform into a so-called
"noise table", which is a wave that can be seamlessly looped without ever generating recognizable
pitch. This is exactly what is required for synthesizing cymbals and snares. But it turned out that it
also works perfectly on chords.

Load/Import Sample
Wave import works exactly as described in the Wavetable section with the small difference that only
one wave-cycle is generated.

Color
This parameter controls a low-pass filter if Color is below 50% and a high-pass filter if Color is above
50%.


For Pitch- Mod, Decay, Velocity, Filter and Level see the shared parameters section here.
The Envelope Shapes and Invert button are described in the Wavetable Ocillator section here .

Switch to Sampler mode to play back samples the ordinary way. You can load a sample from the menu, directly drag and drop files into the
sample menu or link up to four folders on your hard drive to DrumComputer’s sample browser.
Sample Waveform is shown together with Start/End marker (grey line).

Start defines the playback start point in the sample.
Loop : Sample playback can be looped. Loop=100: Sample will not be looped. Loop <100: Defines loop size.
Start and Loop can be Mod destinations. When using the Randomizer it will jump to the Resynth Osc.


15

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


The multimode filter can be assigned to any of the 3 oscillators.
It provides 6 Filter Types :

Filter types

High-pass
Get rid of low frequencies.
Band-pass
Lets only the cutoff frequency pass through.
Peak EQ
Use this to emphasize or the selected frequency to support
the character of your drum sound.
Low-pass
Get rid of high frequencies or perform classical resonant
synth sweeps.
Notch EQ
Use this to de-emphasize a certain frequency in your drum
sound.
Vowel
Use Cutoff to morph between vowel frequencies, use
Resonance for sharper intonation.
Compressor

A compressor with automatic gain make up and inter-engine side chaining.
You can select another sound engine as a side chain source for the compressor.
For example: attenuate a synth bass with the kick drum.



Cutoff

Determines the working frequency according to the filter
type.

Q/Gain

The Q determines the Filter Resonance. In EQ modes, the
Q-Factor is fixed at 2 octaves, while the Q/Gain
parameter determines the gain (0-18db for Peak / -18db
for Notch).

Distortion

The two available distortion types give the signal some
roughness and dirt.


Drive Give your sound more power and harmonics.


Reduce Reduce the overall bit depth and sample rate
for a very digital sound.



16

Sound Pages       Kit Page      Sequencer Page       Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


The Equalizer is just the right tool to shape your drum sound to perfection. 2 bands of cut and gain up to 18 db and a Q-Factor of 3
octaves provide control over your frequency content. Strengthen your kicks, sharpen your snares and make the hi-hats shine with
this one. Be aware of possible level boost generated by the eq, and reduce the mixer level accordingly. Levels exceeding the
dynamic range will be sorted by the Finalizer´s drive circuit.


EQ Controls:


Hi Freq: 1khz-20khz


Hi Gain: -18db – 18 db


Low Freq: 32hz-1khz


Low Gain: -18db – 18 db


Sound Pages       Kit Page      Sequencer Page       Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents17


The Modulation section provides 2 Modulation Generators and a Modulation Matrix with 4 sources and targets. 1 & 2


Two identical Modulation Generators provide Envelopes,
LFOs, Random and individual modulation assignments.

Speed
Determines the speed of the modulation and can work in two modes:

Sync


If Sync is on, Speed works at tempo divisions, always in sync with your bpm.


If Sync is off, Speed works with Hz with a range from 0.01Hz to 100Hz.


Loop

If Loop is off you have a one-shot envelope, otherwise you have an LFO.

Retrigger


(only if Loop is on) Will restart the curve when the sound engine is triggered.

Velocity

Will set the modulation amplitude to velocity level.

Shapes

Choose from different shapes.


18

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Mod Amount Knob 1 & 2
Determines the intensity of the modulation being sent.

If the Amount knob is below 50%, the modulation affects the target
parameter in an negative way.

If the Amount knob is above 50%, the modulation affects the target parameter in a positive way.

Mod destinations
Opens the targets menu to assign the MG to a target throughout the selected sound page.


19

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Here we have the Source menu (top), an Amount control (bipolar) and a Target Menu (bottom).
The Amount controls can also be modulated, which allows complex modulations,
for example controlling an LFO amount with an envelope.

Mod destinations
See MG 1&2 targets menu here.

Mod sources
Most sources speak for themselves, here are some hints on the rather unusual ones:


Env1/Env2/Env3
The Envelopes of the 3 Oscillators. Note that Env1 represents the Exciter-Envelope of the Resonator (Decay).

Modseq
Seq 1(Dec): Modsequencer 1 is hardwired to global decay (affects decay of all Oscillators), but can also be used as assignable modulation source.
Seq 2 (P): Modsequencer 2 is hardwired to global pitch (affects pitch of all Oscillators), but can also be used as assignable modulation source.
Seq 3: Is not hardwired and works as an assignable modulation source.


Zone
The keyzone, resulting from the MIDI mapping, can be used as modulation source.


Resonator, Wavetable and Resynth Osc
These are audio sources, coming from the 3 Oscillators. You might modulate the WT pitch with Spec Osc to have a noisy, inharmonic WT.


Modify
The parameter on the KIT page, can be used as a direct modulator, for example if used with a MIDI controller.


20

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Load Engine Preset
Here you find the Engine Preset. This preset recalls an entire sound and is shared by all engines. So you could save a snare in Engine 1 and then
load it in Engine 8.

Random Button
Click the Random trigger button to perform a sound randomization according to the profile selected.

Random Profile


Select a profile for the sound randomizer here.
If you liked a previous sound, use the UNDO/REDO arrows to go back in history.

Key Pitch

If enabled it uses the keyzone for controlling the pitch. Note that the first
keyzone is capable of bipolar pitch influence, while the last keyzone reaches
to the end of the MIDI note range.

Key Roll

If enabled it uses the keyzone for creating rolls and controlling the roll speed.
The Rootkey will roll at ¼ rate, getting faster with every key to the right.

Flam Time

Makes three triggers out of one and determines the amount of delay
between the triggers.


Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents21


### **Kit Page**

**The Kit Page delivers easy access to the most important parameters of the sound engines.**



22


Here we have 8 channels, representing the 8 sound engines and to the right we find the Master Effects .


Channel
The Engine Channels are numbered 1-8, and they are
represented by their engine color.

On top of a channel you find the Engine Preset .
This preset recalls an entire sound so you could save a
snare in Engine 1 and then load it in Engine 8.

Each of the eight kit channels has its own Global Pitch
and Decay, a Modify Knob and a Random Function .

Choke Groups
Define a choke group (also known as mute group) in oder
to make a trigger on one engine choke the sound on
another engine. Choke Groups is usually used for
open/closed hihat choking, but its also interesting with
synth sounds.


23

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Pitch
This bipolar control will add or subtract a global pitch to all 3 Oscillators and makes it easy to change the pitch of the whole sound.
The Modulation section refers to this target as "Global Pitch".

Decay
This bipolar control will add or subtract a global decay time to all 3 Oscillator‘s envelopes and makes it easy to change the length
of the whole sound. The Modulation section refers to this target as "Global Decay".

Modify
This is a bipolar manual modulator that can be assigned to any parameter throughout the engine, using it as a source in the
modulation matrix. The sound randomizer usually assigns it to "Filter Cutoff".

Random Profile
Select a profile for the sound randomizer here.

Random Trigger
Click the Random trigger button to perform a sound randomization. If you rather liked a previous sound, use the Undo/Redo
arrows to go back in history.


24

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


The right side of the Kit page is the kingdom of the Finalizer. Here we have a dynamics section with Transient Shaper,
Compressor and Maximizer, plus a Warmth circuit with 3 Distortion modes. The Finalizer section provides 5 profiles
and no further parameters but just the Amount knob .


Amount Knob
Use profiles at your personal taste, basically they are sorted in speed.
Attacky : Emphasized the attacks of your drum sounds, making them appear shorter and punchier. Fast Maximizer.
Punchy : Still paying attention to attacks, gentle compression and maximizing.
Decent : A nice mix of transient shaping, compression and maximizing.
Pumpy :  Emphasizes the release phase of your drum sounds, slower compression, making the whole mix appear
fuller.
Relaxed : Slow compression, maximum attention to the release phase of your drum sounds, strong and slow
maximization.

The Master Warmth circuit will make sure that no digital clipping will occur at the output.


Sine distortion : The audio signal is amplified, until it runs into a sine wavefolder.
Tube distortion : 18db of Gain and Warmth provided by a tube emulation circuit.
Tape distortion : 18db of Gain and Warmth with a tape emulation circuit.

Signal Flow notes:
The Finalizer is hardwired to Audio Outputs 1&2 (Master). So if all channels are routed to master, the Finalizer affects the final mix.
Engines which are assigned to audio outputs other than 1&2 are not affected by the Finalizer.
The send effects are added to the Mix (and processed by the Finalizer) if they are assigned to 1&2 (Master).
If the send effects are assigned to other outputs than 1&2, they are not affected by the Finalizer.


25

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


### **Sequencer Page**

**What would be a drum machine without a sequencer! In this one we enjoy all 8 tracks in one view.**



26


The Sequencer contains 8 tracks. Each track has a certain color and represents one of the 8 sound engines.
You can design up to 16 Patterns and enjoy cool features like Humanizing, Pattern Randomizer and a great Modulation Sequencer section.

Click into the Event Matrix to create Trigger events, or drag to create/delete multiple events.
These events will vary in velocity a little bit for natural feel.

Use the Lane Numbers to enter the different sequencer tracks for further editing.
For example, click the 4. All controls will turn blue, indicating that you are now editing engine 4.
Now you can choose an Individual Tempo or Randomize, Shift and Initialize .


The MIDI data generated by DrumComputer can be saved to a MIDI file - for more information click here .


27

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Swing
Humanize
Shift
View Follow (Swing and Humanize)


Global Random
Global Initialize


28

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Each sequencer track has common controls and functions:


Loop Bar
Tempo
Direction
Shift


29

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Note that you can select between two different random and initialize modes for the sequencer.
Depending on the „Init/Rnd resets seq length“ in the settings page track length and tempo division will be reset to default or not.
Here you find a brief overview in which case the different random and initialize buttons will reset track length and/or tempo division:


Global Random
Global Initialize
Track Random
Track Initialize






|Col1|Col2|Col3|
|---|---|---|
|Global Random|Track Length<br>Tempo Division||
|Track Random|Track Length||
|Global Init|Track Length<br>Tempo Division|Tempo Division|
|Track Init|Track Length||



30

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


The Modulation Sequencer lane covers all sequencer features:


Vel Assign different velocity values for each step.

Prb Trigger certain events each 2nd, 3rd, 4th (and so on) time.

Roll Sub-divide the step into a number of triggers, from 1 to 8.


Ofs Give your event positive or negative delay/offset.


Dec (ModSeq 1) Controls the global decay and can moreover be used as assignable modulation source.

Ptch (ModSeq 2) Controls the global pitch and can also be used as assignable modulation source.


Mod (ModSeq 3) Can be used as assignable modulation source.

_**Controls and functions**_ :


Randomize Create a random number of steps and values.


Initialize Delete all data of the selected modulation track sequence.

Invert Max becomes min, min becomes max, half stays half.


Ramp Create a perfect ramp.

Triangle Create a perfect triangle.


Hold CTRL and drag the mouse to affect all events in the sequencer lane (up or down) at once.


31

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


### **Pattern Keys, Mute Keys & Mapping**

MIDI related features, including a flexible multi-purpose keyboard.


Click this icon to get access to the Pattern, Mute and Mapping section.


32


Pattern
16 patterns are available in a preset.

The Pattern Keys respond to 16 MIDI notes, from note C-2 to D#-1.
Use the Pattern Keys to call/play patterns with the mouse while editing, or just let it display incoming MIDI notes.


Copy/Paste

Copy/paste has never been easier: Click the Copy/Paste button, all patterns but the source pattern start blinking, now click the
target pattern number or key. Finished! You can now edit your variation.

Note: There are 2 clock modes to be found in the settings here.
In Internal Clock mode patterns play from the beginning, as long as the Pattern Key is active.
In Host Clock mode, patterns play along with the Host Song Position.


33

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings      Table Of Contents


The Pattern Sequencer (Chain) plays up to 16 different patterns in any order.


Select the desired pattern number by holding the mouse button and dragging up or down.

Chain (on/off)

When off, the Chain is inactive.
When on, the Pattern Sequencer steps through the patterns determined by the Chain Sequencer.
It runs at a one bar step resolution.
Loop Bar


Determines the total length of the Chain sequence. After playing the last step in its sequence, the sequencer will loop back to the
beginning and continue playing through the pattern steps in order.
Delete


This initializes the Pattern Sequencer for a fresh start, creating a sequence which iterates through all patterns.


View Follow

If this button is off (eye closed), the view follows the pattern keys, so you can edit a pattern while other patterns are played by the
pattern chain. If this button is on (eye open), the view follows the pattern chain. So you will always see the currenty active pattern.


Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents34


Mute
Engines can be temporarily muted by MIDI notes, using the Mute Keys.
These are represented by their engine colors and numbers. The Mute Keys respond to note C-1 to B-1.

Mapping/Zones
The keyzones show the color and number of the mapped sound engine. You can handle keyzones easily by clicking the engine number and
dragging left or right. The engine number also represents the rootkey. The space between the rootkeys are the keyzones.
These can be mapped to pitch or roll and can be used as modulation sources. Note that the first zone can be bipolar and allows for negative
modulations, which might be interesting if you need to up- and downpitch a sound.
The first key of the Zone Keys responds to note C0.
The last keyzone always ends at key 128, which gives you a large zone for drastic modulations.


Save/Load Mapping
Click the Mapping Preset menu to load/save the desired engine/MIDI mapping.


Shift

Shifts the mapping either left or right, key by key.

Display keyboard zones


Click and drag the scroll bar below the keyboard to bring the „hidden“ parts into view.


35

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


### **Mixer**

**Here you find all your levels, send level, pan and send effects, namely Room and Hall.**



36


Click this button to get access to the Mixer section.


Mute
Mute the related engine.


Solo
Solo a single engine.


Level
Control the engine level,

Pan
Adjust stereo positioning.


Send Level
Room and Hall are send effects, these knobs control the amount of signal being sent to the send effects.


37

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Two incredibly good sounding reverbs are found in the Send Effects section. Use the faders in the mixer to define the send fx output level.
Assign the send effects to individual audio outputs in the Settings.



Room
In order to have a realistic sound, you can put
your drums into the same room.
The room works slightly different to the hall, as it
computes more density in a smaller space.

Size
Adjusts the size of the room.


Tone
Acts as a low-pass filter.


Unmute/Unsolo
Will unmute/unsolo all channels.


Master Level
Controls the master level.



Hall
A huge and dense reverb effect, meant to be
used for real reverberation effects, as it is
common with snares and claps for example.


Size
Sets the reverb 'room' size.


Tail
An additional control to define the length of the
reverb tail.


Tone

Acts as a low-pass filter.



38

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


### **Remix feature**

Create crazy fills with ease or enjoy them coming in automatically.



39


Remix
The Remix Feature is a one touch fill maker. Activate the Remix control temporarily to mutate the current pattern. 16 remix figures are available:
1-8 creates small rolls over 2-3 drum sounds, each figure addressing another group of engines.
9-14 will assign existing patterns to different engines.
15&16 creates pure 16th rolls and fires these across the engines.
Additionally, random pitch bends, send fx- and filter sweeps will be generated.

Auto Fill
Will generate random fills automatically and works in a song-oriented way:


Auto 1
At the end of each 4th bar, a fill will be generated for the last 1/4 note.
At the end of each 8th bar, a fill will be generated for the last 1/2 note.
At the end of each 16th bar, a fill will be generated for the while 16th bar.

Auto 2
Same as Auto 1 but generates fills more frequently (fills at 2/4/8 instead of 4/8/16),

Fills include trigger/engine re-routings, randomized send effect levels, filter sweeps and pitchbend curves. Since AUTO FILL is connected to your
song position, it might be ill-timed when your song does not start at bar 1. Use Auto Fill Offset in the Settings, to adapt Auto Fill to your real song
start. For example, if your song starts at bar 3, set Auto Fill Offset to 3 bars.
AUTO FILL is completely translated to MIDI.
Use the MIDI drag and drop feature to get an unlimited number of fills and then choose the best.


40

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


### **Header & Settings Screen**

**Manage your presets, set your overall preferences, generate a MIDI file and make your MIDI/audio out assignments.**



41


PLAY button and current pattern display
Starts the sequencer. When the PLAY button is lit, it indicates that the clock is running.
If the PLAY button is off, the sequencers will not run, and external MIDI notes might trigger the individual engines.
If the clock mode is set to internal, the PLAY button shows stripes („armed“) until a Pattern Key activates the sequencer.

Note: If the PLAY button is ON, all modulation data comes from the internal sequencers.
If the PLAY button is OFF, modulation data is expected on the MIDI CC numbers given in the Settings Screen.

Pin Button
If enabled the current sequence won’t change when selecting another global preset.

Preset name
Click the preset name (here init) to load presets and save your own work.

Make Kit Button
Creates entire kits with just one click.
Use the "MakeKit sorts Profiles" option in Settings, to reset the random profiles to their default settings whenever MakeKit is executed.
Leave the option off to randomize kits with your own profile setup.

Undo/Redo
Set back or redo your last operating step with the curved arrows.


42

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Options
Clicking the gear icon opens up the Settings Screen where you find some global settings and functions.

Note: The header of the Sequencer Page differs a little bit from the others. While you have the usual menu bar, there now is an additonal entry:

Drag MIDI (Sequencer Page)
The MIDI data generated by DrumComputer can be saved to a MIDI file. Just drag and drop the « Hand » icon to a MIDI track in your DAW or to
your desktop and the file will be created. Use the BARS control to the left to set the length of the MIDI file. The maximum length is 64 bars.

MIDI File
The sequencer translates all data to the MIDI file:


       - triggers are generated on their root notes, given in the Mapping Screen

       - modulation sequencers are translated to MIDI CC´s, displayed in the Settings Screen

       - probability, rolls and offset are translated to MIDI notes directly (occurrence and timing)

       - autofills are completely translated to MIDI notes and CC´s

!!! Note that the MIDI export process may take some time. So please make sure to hold your mouse button until the cursor indicates that the
process has finished.


43

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Click the gear icon in the upper right of the Header to open the Settings Screen. Here you find some global settings and functions.


Clock Start
Determines the clock source. DrumComputer can run in sync with your DAW (HOST),
or it can be triggered by a MIDI note (INTERNAL), only applying the sequence as long as you hold a note.


Ignore Program Change
Incoming Program Change messages will be ignored.


CC Snap Isolate
When active, MIDI Learn settings will be kept and not be changed when selecting a different preset.

CC Map
Load or save your current MIDI CC assignment.


Mapping Snap Isolate
When active mappings won't change when selecting a different preset.

Auto Remix Offset (Bars)
Adapt Auto Fill to your real song start.


Init/Rnd resets seq length
Determines if loop bar position and tempo devision will be resetted or not. Please see here for detailed information.


44

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


MakeKit sorts Profiles
Determines if MakeKit will affect the profile list.

Mod Seq Value Latch
Uncheck this option to read the Mod Seq stepwise, instead of having it latched with triggers.
This makes it possible to modulate parameters of sounds with a long decay.

UI Scale Factor (Zoom)
Adjust the DrumComputer GUI to your monitor screen size. Hold down the Ctrl key and press the + to increase the size or - to decrease the size.

Channel Assignment
Assign the sound engines and send effects to 20 available outputs. Only engines assigned to Master will run through the Finalizer.
The 8 sound engines can be assigned freely, in order to build subgroups. However, the send effects have fixed output assignments which can be
switched between Master (1/2) or their single outputs 17/18 for Room and 19/20 for Hall.

Send MIDI
Enable/disable the MIDI output of the respective channels.

Remix/ Auto CC Assignment
This MIDI CC list gives an overview of all continuous controllers and which action they are assigned to.

About
Shows your serial number, along with its validation status. Click ? for quick access to this manual or the link to open the Sugar Bytes website.


45

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


MIDI LEARN


Right-click any control to open up the MIDI learn popup window.


Click the left MIDI socket symbol to assign incoming MIDI CCs.
Click the crossed out MIDI socket symbol to remove the assignment.
Click the field labelled „None“ and enter the desired CC number.


When using the Standalone version of DrumComputer:
If CC Preset Isolate is enabled in the MIDI Settings of DrumComputer MIDI Learn settings won't change when loading presets.
If CC Preset Isolate is unchecked the CC Map will be recalled with the related preset.

Within a DAW DrumComputer’s MIDI Learn settings will be saved with the song.


Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents46


### **Host Integration**

DrumComputer works as a VST2 /VST3/ AU / AAX plugin in the most common DAW hosts.


Make sure that DrumComputer is installed in the plug-ins folder used by your DAW.
Some hosts need to perform a plug-in rescan when a newly installed plugin is launched for the first time.


Please find all detailed instructions for your DAW below.



47


**Cubase**
Perform a full rescan in the Cubase plugin manager. Make sure that the DrumComputer.dll/DrumComputer.vst3 (Win) or DrumComputer.vst/
DrumComputer.vst3 (macOS) file is contained in Cubase‘s assigned VST Plugins folder. Load DrumComputer as Instrument into an Instrument
track.


**Ableton Live**
When using macOS, we recommend using the VST version of DrumComputer in Live. Please note: With Ableton Live, plugins sometimes will be
marked as unloadable and not rescanned automatically. If this happens to be the case, force a rescan by unchecking and checking the ‚Use
custom VST Folder‘ checkbox in Preferences/File Folder/Plug-In Sources. Set up a MIDI track and insert DrumComputer as instrument.


**Pro Tools**
When installing DrumComputer, select AAX plug-in format. (AAX 64 is supported by Pro Tools 11 and higher.) Use DrumComputer as an
instrument.


**Studio One**
Go to the Studio One menu and choose Options. Click Locations, then VST Plug-Ins. Click the Add... button and select your VST Plugins folder.
Press OK. Create an instrument track and pick DrumComputer up from the Instrument list.


**Sonar**
Make sure that DrumComputer is installed in the VST Plugins folder. Insert DrumComputer as a „soft synth“.


**Logic**
Select DrumComputer as an AU-Instrument from the I/O dialogue of a Software Instrument track.


**FL Studio**
Go to Channels>Add one>More...There you should find DrumComputer and perform a refresh. You can now open DrumComputer in the Mixer
Inserts.


48

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


[Download (requires login) the latest version here. Double-click the installer and follow the instructions provided by the installation process.](http://www.sugar-bytes.de/account)

The standalone version and manual will be installed into: Presets will be installed into
Windows: C:\Program Files\Sugar Bytes\DrumComputer \Users\YOURLOGINNAME (your home folder)Documents\Sugar
macOS: /Applications/Sugar Bytes/DrumComputer Bytes\DrumComputer



The standalone version and manual will be installed into: Presets will be installed into
Windows: C:\Program Files\Sugar Bytes\DrumComputer \Users\YOURLOGINNAME (your home folder)Documents\Sugar
macOS: /Applications/Sugar Bytes/DrumComputer Bytes\DrumComputer

Important: Do not relocate DrumComputer presets after installation!

macOS Windows

Default installation paths:

Default installation paths: VST2 C:\Program Files\VSTPlugins
VST2 /Library/Audio/Plug-Ins/VST/ VST3 C:\Program Files\Common Files\VST3
VST3 /Library/Audio/Plug-Ins/VST3/ AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins



Windows
Default installation paths:
VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins



49

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


To uninstall DrumComputer, please follow the instructions:


**Windows**
Uninstall DrumComputer under Control Panel>Add/Remove Software.


**macOS**
Delete all the following files and folders:

/Applications/Sugar Bytes/DrumComputer
/Library/Audio/Plug-Ins/VST/DrumComputer.vst
/Library/Audio/Plug-Ins/VST3/DrumComputer.vst3
/Library/Audio/Plug-Ins/Components/DrumComputer.component
/Library/Audio/Plug-Ins/Components/DrumComputerMidiFX.component
/Library/Application Support/Avid/Audio/Plug-Ins/DrumComputer.aaxplugin

~/Documents/Sugar Bytes/DrumComputer
~/Library/Preferences/com.sugar-bytes.DrumComputer.plist

Authorization
The serial number is requested during installation. If the serial number is missing or incorrect, the product will not produce any sound.
Check the top area of the DrumComputer interface to verify whether your serial number is VALID. Manually entering the correct serial number
there or performing a quick reinstall, should fix any issues. One License covers both the macOS and Windows version and can be activated for
two computers at the same time. For use on more than two computers, please buy an additional license.


50

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


Sugar Bytes GmbH | Made of passion

Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395



Sugar Bytes are:
Rico Bernhardt & Robert Fehse
Vincent Miethe
Nadine Purrmann



51

Sound Pages       Kit Page      Sequencer Page      Mapping/Zones      Mixer      Remix Feature      Header & Settings       Table Of Contents


