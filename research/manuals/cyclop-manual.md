# CYCLOP

## Manual


### Content

WHAT IS CYCLOP 4


INSTALLATION 5

WINDOWS 5
MACOS 6


UNINSTALLING 7


AUTHORIZATION 7


CYCLOP STRUCTURE 8


THE PRESETS 9

THE PRESET HANDLER 10


THE 4 MAIN CONTROLS 14

THE WOBBLE GENERATOR IN DETAIL 15


THE HOTKEY SYSTEM 20


THE CENTER SCREEN 21

WOBBLE SETTINGS PAGE 22
STANDARD MODULATORS PAGE 23
MODULATION ASSIGNMENTS PAGE 24
FX PAGE 25
MAIN KNOB RECORDERS PAGE 28
MIDI SETTINGS PAGE 29


MASTER EFFECT SECTION 30

SUB OSCILLATOR 30
BASS 30
STEREO 31
DISTORTION 31
MASTER ENVELOPE 32
GLIDE 32


SYNTHESIS AREA 33

THE SYNTHESIZERS 33
THE ROUTING UNIT 38
DISTORTION 40
THE FILTERS 41


NATIVE KONTROL STANDARD NKS 45


HOST INTEGRATION 48

MIDI REMOTE 54


THE GAME 55


2


QUESTIONS? 57

SILENCE 57
LICENSE 57


IMPRESSUM 58


3


### What is Cyclop

Cyclop is a monophonic Synthesizer with a large number of innovative features. The
finest DSP algorithms give Cyclop an unbelievable direct and powerful sound which is
made to fit perfectly into the mix.

Cyclop specializes in wobble sounds, which means that rhythmical material is the special
power of this synthesizer. Conventional structures have been twisted in a refreshing way
to give you a workflow full of fun and lucky surprises.

The 4 main controls let you tweak your sound in different ways, which you can move with
recordable envelopes, fired up by your MIDI notes.

Vocal sounds are not made by just vowel filters anymore, also the oscillators can produce
humanoid sounds, especially the Transformer, which is a sophisticated
wavetable/granular/pitchformer sampler.

The Effect section was made to impress, being a mixture of Effectrix and Turnado flavors,
adding the Gater and recordable knob envelope as special performance features.

We hope you will have lots of fun with your new bass machine!


BACK TO TABLE OF CONTENT


4


### Installation

[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)

The standalone version and the manual will be installed into:

Windows: C: \ Program Files \ Sugar Bytes \ Cyclop
macOS: /Applications/Sugar Bytes/Cyclop

Presets will be installed into Documents \ Sugar Bytes \ Cyclop.
Do not move the Cyclop presets after installation!

#### WINDOWS


Default installation paths:

VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C: \ Program Files \ Common Files \ Avid \ Audio \ Plug-Ins

#### macOS


The Audio Unit, the VST Plugin, the AAX Plugin will be automatically installed into the
correct folders.

Default installation paths:

VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins


5


### Uninstalling

In order to uninstall Cyclop, please take the following steps:
Windows: Uninstall Cyclop under Control Panel/AddRemove Software.
macOS: Here is the way to delete everything regarding Cyclop:

/Applications/Sugar Bytes/Cyclop
/Library/Audio/Plug-Ins/VST/Cyclop.vst
/Library/Audio/Plug-Ins/VST3/Cyclop.vst3
/Library/Audio/Plug-Ins/Components/Cyclop.component
/Library/Application Support/Avid/Audio/Plug-Ins/Cyclop.aaxplugin

NKS:
/Library/Application Support/Native Instruments/Service Center/Cyclop.xml
/Library/Application Support/Sugar Bytes/Cyclop/
/Library/Preferences/com.native-instruments.Cyclop.plist

~/Documents/Sugar Bytes/Cyclop
~/Library/Preferences/com.sugar-bytes.Cyclop.plist

~ means: /Users/YOURLOGINNAME (your home folder)

(Please note that since OSX 10.7.x the library folder is a hidden folder.
Therefore please use the "Go To Folder" menu and then enter ~/Library.)

### Authorization


The serial number is requested for installation.

If the serial number validation fails, the plugin will show that in the Cyclop About Screen.


Back to Table of Content


6


### CYCLOP Structure

Essentially, the upper part of the instrument is the modulation and FX area, while in the
lower half you’ll find synthesizer, audio routing, and filters.

Cyclop is essentially controlled by a MIDI keyboard. Using the 4 Main knobs along with
your performance will create vivid sounds, full of madness and vitality.

A sound is created by setting the synthesis controls and assigning modulators. There are
always 16 assignable controls: 3 synth controls, 3 filter controls, 2 routing controls,
master pitch and master level.

Between synthesizers and filters you find the Routing module, where you can easily
connect oscillators and filters in different ways.

The master effect section includes sub oscillator, bass processor, distortion and stereo
imaging.

The effect sequencer is the last module in the signal path.
It combines a 4-track sequencer with lots of effects.


Back to Table of Content


7


### The Presets

The Cyclop presets are located in Documents/Sugar Bytes/Cyclop.

Here you find one folder for presets and one folder for samples.

The presets and samples can be found in the lower subfolder structure. Only one
subfolder is possible.


The DICE button selects a random preset.
The ARROW buttons switch to next/previous preset.

The preset field shows the current preset and above the preset folder.
Click into the preset name to open the giant Preset Handler.

The “Disk” button will save a preset and opens a window for assigning tags to your
preset. You can select tags from the menu but also just write your own tags into the tag
fields.
Tags can also be edited later in the Preset Handler.


The Robot shows when a tag has been applied.


8


#### The Preset Handler

The new gigantic Preset Handler offers convenient ways to find your desired sound.

Here you can assign four tags, rating and author to the selected preset.
Presets can be filtered using these tags.

Furthermore, you can create your own program change lists and load/save them.



9


##### The Trace Window

Here you can filter presets depending on their tags or other preferences.
4 modes are available:


Cloud
The beautiful way to find nice sounds. The Cloud shows all tags, with different size,
according to their population.
Click on a tag to show all presets with that tag in the “Result List”.
Click on another tag to sharpen the search.


Click the “Reset” button to reset the search.


Tag List
All tags are shown in a list.
Works exactly like the cloud.


Author List
Here you can find presets according to their authors.


Folder List
Here all preset folders are shown and presets can be filtered according to the folder they
are in.


10


##### The Result-List

Here all found presets are listed.
Double click a preset to load it.
Click on NAME, AUTHOR or RATING to sort the presets.

##### The MIDI Program List


The MIDI program list can be expanded from the result list.
When the MIDI Program List is shown, MIDI Program Changes can be executed.

Drag & drop presets from the Result list into the MIDI program list in order to build your
own MIDI Program List.

Don't forget to save the list when you are done. If you only want to use one list regardless
which preset you load, you should save your list as 'Default.smbp'.

If you want to connect a certain list with a certain preset you have to load a preset. Then
load or save a MIDI PRG LIST and then save your preset.
So in general one could say: a preset always loads the MIDI PRG LIST it had chosen when
the preset was saved.


You can also copy the whole result list to the program change list using a button.

Program lists can be saved and loaded.
The presets contained in a program list cannot be edited anymore.


11


##### The Edit Field

In this field, tags are assigned to the selected preset.
Author, Rating and 4 tags can be assigned.
All changed are executed immediately.
The Robot shows which tags are assigned.
For each assigned tag, one of his parts will lighten up.

##### Working with Tags

A tag can be chosen from the tag list.
To create your own tags, just write your tag into the tag list.
In order to delete a tag, just make sure it is not assigned to any preset.


Back to Table of Content


12


### The 4 main controls

Cyclop has been made to join first-class DSP with modulation madness
to achieve unbelievable sounds.

The 4 main controls are for tweaking the current sound. Each of the main controls
includes a recordable envelope which is called Recorder. The recordable envelope
remotes the control when its play button is active and when a MIDI note is played.

Wobble Knob : Waveform and speed of the Wobble LFO.
Assign Knob: Morph between two Wobble->Parameter assignments.
Sound Knob: Manual value, that can modulate parameters.
FX Knob: Control about the FX Sequencer.

##### Wobble Knob


The Wobble Generator is displayed by the mighty Wobble Knob in the upper left part of
the instrument. The Wobble Knob lets you choose from 12 LFO Speeds and Waveforms.
The Wobble is a Modulator and can be assigned to 16 different internal targets.

##### Wobble Amount Knob


The smaller Wobble Amount Knob performs a morphing between two Wobble>Parameter assignments. With this knob you can morph from one wobble to another or
just to fade a wobble in or out.


Make Wobble assignments where all assignments are made — in the Assignment Page.


13


##### Sound Knob

The Sound Knob also is a modulator that creates a “control voltage” which can be
assigned to different parameters in the Assignment page.

The Sound Knob makes it easy to morph from one sound to another by just turning
parameters up or down, according to the assignments you made in the Assignments
Page.

We recommend using the Sound Knob Recorder Envelope to ride parameters exactly the
way want. A common way of using this is to turn down the pitch after a while in order to
create a custom tape stop effect.

##### FX Knob


At the top right we find the beautiful FX Knob which gives you control over the FX
Sequencer. The Knob also shows all active effect slots and the current Gater pattern.
Effects and Gater can only be edited in the FX Sequencer, so clicking into the funny FX
Knob area opens the FX Sequencer directly.

The FX Knob can be remoted by the Recorder (green Play Button), by the FX Sequencer
Clock (blue Play Button), or by Mouse/MIDI CC (Hand Button).

#### The Wobble Generator in detail


The Wobble Generator is an advanced LFO that is built of the 3 main units Wobble Knob,
Wobble Settings and Wobble Amount. The Wobble Knob lets you choose from 12 LFO
Speeds and Waveforms, while the Wobble Amount Knob morphs between 2 Wobble>Parameter assignments. The Wobble Settings Page lets you do some deeper tweaking
of the wobble performance, like phase offset, restart options, wave quantizer and
different ways to control the knob.


14


##### Wobble Knob

The Wobble Knob allows control about Wobble speed and wave form.


Special about the Wobble LFO are the fixed values.
The snowflake indicated Freeze mode. Like a sample and hold module,
The Freeze will maintain the last active value as long as it is selected.
If the Wobble Knob turns from a sine wave to the snowflake, the last value of the sine
wave will be held until another wave form is selected.


Furthermore, there are 5 fixed valued available. These values are
0%, 25%, 50%, 75% and 100% and are displayed by square with different sizes. These
values make it possible to use the Wobble Generator like a step sequencer.


The central wave form control sets all wave forms at once.


The Random Button sets a random wave form situation.


The Wobble knob can be controlled by its own recordable envelope.


Click the record button to arm for envelope recording and directly open the
Envelope Recorder Screen.



15


##### Wobble Settings

The Wobble Generator has its own settings screen where you can make even deeper
adjustments.

The following options are available:

Start Phase
Here you can set the starting phase of the wobble LFO. This determines if the modulation
will go upwards or downwards after you hit a note.
Quantize
The LFO signal is quantized to stepped values.
Restart
This control determines when the wobble LFO will restart. You can restart it with a MIDI
note, but also when the Wobble Recorder Envelope wraps around or with several beat
divisions.
Interpolate
This button determines if the LFO Speeds are switched or faded.
Hotkeys
The 12 Wobble Knob positions can directly be controlled by the 12 Hotkeys.
Velocity
This controls the Wobble Knob by MIDI velocity values.


16


##### Wobble Amount Knob

The Wobble Generator creates a unique modulation curve that you can to apply to
synthesizer parameters — that’s what the Assignment Screen is all about. Here you can
see all modulations at a glance and you can call up the Assignment Pages for all
modulators quickly, according to their data.

If you call the Wobble Assignment Page, you can see that it has A and B pages. These
pages are morphed by the Wobble Amount Knob.

Hit the A Button to setup the Wobble for the lowest position of the Wobble amount
Knob. Then hit the B button then create the Wobble for the highest knob position. Now
use the Wobble Amount knob to morph between the wobbles.


Back to Table of Content


17


### The HotKey System

The red keys in the lowest octave are the HotKeys. These keys produce no sound, they
just save different setups in different places of Cyclop. If you see this Button, you can
activate the HotKeys. If the Hotkeys button is off, the HotKeys are disabled and will not
affect your sound when you hit a HotKey by accident.

Use the Hotkeys to connect Wobbles with Effect Sequences or Knob Recordings. Here´s
how it works in the single places:

Wobble Knob
Use the HotKeys to call the 12 Wobble Knob positions directly and save the 12
waveforms of the Wobble Knob.

Knob Recorders
Use the Hotkeys to call different Recordings. That means, each Hotkey can contain a
different Knob Recording (Remember? The 4 Main Knobs contain recordable Envelopes).

Assignment Pages
Save different Modulation Assignments on the Hotkeys. That way, you can load
completely different sounds with the HotKeys.

FX Sequencer
Use the Hotkeys to call up different FX and Gater Sequences.


Back to Table of Content


18


### The Center Screen

The Central Screen covers 6 units:
Wobble Settings, Standard Modulators, Modulations Assignments,
FX Sequencer, Main Knob Recorders, MIDI Settings and the game.

Use the 6 buttons around the screen to call the pages:


Wobble Settings


Standard Modulators


Modulation Assignments


Effect Sequencer


Recorder Envelopes


MIDI Settings Back to Table of Content



19


#### Wobble Settings Page

Here you can make special settings for the Wobble Generator.

Restart: Decide if the Wobble LFO restarts with each MIDI Note, at certain beat divisions,
or when the Recorder Envelope wraps around.

Single/Multi: Decide if the Wobble LFO restarts with each note (Multi) or with each first
note (Single).

Start Phase: Use the fader to set the start position of the Wobble LFO.

Quantize: The Waveform is quantized to stepping values.

Interpolate: Decide if the Wobble Knob switches or fades between beat matched LFO
rates.

Velocity Sets Knob Position: MIDI Velocity will control the Wobble Knob.

HotKeys: Activate this button to control the 12 Wobble Knob positions with the 12
HotKeys.


The wobble wave form is displayed in the upper left bull´s eye.
Here you can see all waveform changes and LFO restarts.


Back to Table of Content


20


#### Standard Modulators Page

The Standard Modulators Page contains the modulators Envelope, LFO and Step
Sequencer. These modulators can be assigned in the Assignment Screen. All modulators
are triggered with a MIDI note. The LFO can be controlled by the Envelope and the Step
Sequencer can be driven from various Sources.

##### Envelope


The Envelope is an AHDSR Envelope which can be restarted with each MIDI note (Multi)
or with each first MIDI note (Single).

Attack sets the fade-in time (from zero to full value) until the hold/decay/sustain is
reached.

Hold determines how long the maximum value is held before decay is started.

Decay is the fade time to the sustain value.

Sustain is the value that remains constant as long as the note is held.

Release is the fade out time after the note is released.

##### LFO


The LFO generates a specific waveform which modulates parameters. Nine different LFO
waveforms are available. These are the same waveforms as in the wobble generator,
except for the freeze and the fixed values.

LFO Rate and LFO amount can be faded in and out with the Envelope.
Use the exponential and logarithmic waveforms to produce percussive sounds.

Back to Table of Content


21


Rate: The LFO rate, always in sync with your song tempo.

Waveform: The LFO Waveform.

Env->Amt: Envelope controls LFO amount.

Env->Rate: Envelope controls LFO Rate

Scope: Shows you the current LFO signal.

##### Step Sequencer


The 16-Step Sequencer delivers a sequence of 16 values.
You can read the sequencer in different ways to achieve the moqr craziest modulations.
Usually a clock is used to read a sequencer, so the clock menu gives you choice about the
available read modes:

Gater: The FX Gater clock controls the sequencer.

MIDI Gate: Each MIDI note reads the next step.

LFO: LFO controls the step sequencer.

ENV: Envelope controls the step sequencer.

Clock: The step sequencer´s own clock speed.

#### Modulation Assignments Page


Here you find all Modulation Assignments.

Back to Table of Content


22


In the lower part of the screen you see all modulations at work. Plus, you can see all fader
positions of the individual Assignment Screens.

Each of the internal modulators has one Assignments Screen: Wobble Generator,
Envelope, LFO, Step Sequencer and Sound Knob.

Click one of the small windows to call the Assignment Page for the desired modulator.

Click the X button to delete all assignments for the selected modulator.

The Wobble Amount Page contains two screens which are morphed by the Wobble
Amount Knob. Click the A and B buttons to call the screens directly.

#### FX Page


Here you’ll see the FX Sequencer. It provides 4 sequencer lanes, each with a choice of 8
effects. The Effects have no further controls, only the “Send FX” offer dry/wet controls to
determine the effect mix.
The other effects are “Looper-Effects” which always run at 100% wet.

Use the FX Slots like knobs, mouse them up- or downwards to select the desired effect.
Spread the same effect across several steps holding the Shift key.

The Effect Sequencer can be read in 3 different ways:


A clock is used the read the FX sequencer.

Back to Table of Content


23


The Knob is used to read the FX Sequencer.


The Recorder Envelope controls the FX Knob and so reads the FX Sequencer.


The Effect Sequencer can be filled with effects randomly. (Dice Button)
The X Button deletes the sequence.


The Clock determines the read speed of the sequencer, in relation to the song bpm.


The Swing function plays each second step a bit later.


The playback direction can be set to different modes, also Random.


Use 12 different FX/Gater sequences by activating the hot keys.
An empty Gater will mute all audio!!!


The FX Sequencer has a loop bar which determines where the sequencer starts and how
many steps it will play in loop.
Grab the loop bar ends to resize the loop.
Grab the loop bar middle to move the loop.

Use the HotKeys to fire up different FX Sequences directly from you MIDI keyboard.

On the top of the page you find the Gater which interrupts the audio signal.

Back to Table of Content


24


The Single/Multi button defines how the sequencer will restart.
If Single is selected, the sequencer will restart with each first note.
If Multi is selected, the sequencer will restart with each note.

##### Pitch Looper


The Pitch Looper repeats the audio signal for a certain amount of time. With each
repetition, the pitch becomes higher or lower. The Pitch Looper provides 4 different
settings for “Pitch Up” and 4 different settings for “Pitch Down”.

##### Looper


A simple looper effect which repeats the audio material at a certain rate. The 8 settings of
the Loop FX lane offer 8 different loop sizes.

##### Vinyl FX


This is a collection of several vinyl effects.


1. Tape Stop fast
2. Tape Stop slow
3. Vinyl slow
4. Vinyl med slow
5. Vinyl med fast
6. Vinyl fast
7. Scratch slow
8. Scratch fast

##### Send FX


The send FX are all delay-based effects. There are 2 settings available for Phaser, Chorus,
Delay, and Reverb.


These effects offer individual dry/wet controls to determine effect intensity.


Back to Table of Content


25


##### Gater

On top of the FX Sequencer page you find the Gater which works like a trance gate: it
interrupts the audio signal with a groovy pattern.

In addition, the Master Amp Envelope is triggered. Usually you would not
notice, until you use Release or Delay in the Amp Envelope. Then you can
let the Gater step have decay or release curves.

#### Main Knob Recorders Page


Here you’ll find the Recorder Envelopes for the 4 Main Knobs.

Essentially, these are 144-Step Sequencers which can record data from their respective
Knobs. You can also draw values with the mouse and switch it to a 16-step sequencer.


The Recorder has a loop bar which defines the playback range within the sequence.
Grab the loop bar ends to resize the loop.
Grab the loop bar middle to move the loop.


The Record and Play functions are activated with these buttons and
are finally executed with a MIDI note.

Use CTRL+Mouse to draw straight lines (only in FINE draw more).


Back to Table of Content


26


Length: Defines record and playback speed.


Erase: Deletes all data.


Draw Fine: Draws each of the 144 steps at once.
(use the CTRL key to draw straight lines).


Draw Coarse: Draws like a 16 step sequencer.


Mode: Determines if recording or playback is repeated or running only for one time, as
long as a MIDI note is held.

#### MIDI Settings Page


All MIDI-related settings are made here. Additionally, here you find the pitch LFO that you
would expect when using the modulation wheel.

Ignore Program Change: Incoming program change messages will be ignored. Only
presets from the folder “MIDI Programs” will be used for program changes.

CC Preset Isolate: MIDI-CC assignments (MIDI Learn) will not be saved or changed with
the presets.


27


CC Map: Load or save your current MIDI CC assignment.

Pitchbend Range: Intensity of the pitch bend wheel in semi notes.

Master Tune: Makes the overall tune fit to your “out of tune” song.

Modwheel to Pitch LFO: You expect a slight pitch LFO when using the modwheel. Set this
up here.

### Master Effect Section


The Master Effects section contains final insert effects and the sub oscillator.

#### Sub Oscillator


The Sub Oscillator provides a clean bass fundamental. That ensures that you can use the
synthesizers for any sounds without having to pay attention on the bass provided by the
synthesizers 1 and 2.

The Sub Osc is a high quality Sine Osc that plays along with your MIDI notes. You can set
it 1 or 2 octaves below original pitch to have the bass where you want it.
The Sub Osc is not sent through any filters or effects, just the pure sine is delivered
directly to the output.

#### Bass


The Bass processor provides a defined bass boost are 60 and 80 Hz while it cuts down
the 225Hz a bit. This will put the bass where you need it.
If the synthesized sound contains no low frequency, there is nothing to amplify. In such a
situation, it is better to use the Sub Oscillator to add some decent bass.


28


#### Stereo

The Stereo Processor spreads the audio signal in the stereo field.
No delays are used to avoid any phase problems. The Signal becomes split into 8
frequency bands between 250Hz and 4000Hz which become sent to the left and right
speaker, while frequencies below 250Hz and above 4000Hz remain in the middle. This
M/S Stereo processing is quite unique and will make your bass fill the room.

#### Distortion


The 9 available Distortion units give the final synth signal some roughness and dirt. Nice
flavors are available to add some beef to your sound.
The same Distortions can be found in the Routing Unit, where distortions are used
between the filters when they run in series.

##### Amp

Amp/Speaker simulation with lots of warmth.

##### Drive

Nice and angry overdrive with a special top end.

##### Dist

Intensive distortion that turns the sound into something new.

##### Diode

The distortion core from the MS-20 filters is used here to provide some mojo.

##### Clip

The audio will be boosted until it clips. Use this unit to just boost your level or to add
some really evil distortion.

##### Sine

The audio signal is boosted and then runs through a sine algorithm.

##### 1-Bit

The audio signal must decide 1 or 0? The hardest digital method.

##### Crush

Nice bit crusher that basically adds some silver to the sound.


29


##### Digitize

This pitch-dependent sample rate reducer is always good for some digital vocal sounds.

#### Master Envelope


The Master Envelope defines the overall Level performance.
It can fade the audio signal in and out while a note is pressed and can let the synth fade
out slowly after a Note has been released.

The Attack control lets the sound fade in for up to 4 sec.

The Decay/Release control is special:
If the knob is below 50%, it is decay and the sound will fade out while you hold the note.

If the knob is at 50%, it is just sustains and the sound will be heard as long as you hold
the note.

If the knob is above 50%, it is release. Now the sound fades out after you release a note.

The Velocity button determines whether or not MIDI velocity is used to define the Level.

#### Glide


The Glide processor fades from one note to the next and can take from 0ms to 2000ms
until the next note is reached.


The Glide offers two modes:
One Finger: Glide is performed always.
Two Fingers: Glide is only performed when two or more notes are played.


Back to Table of Content


30


### Synthesis Area

In the lower half of the instrument you find the Synthesis Area.
It consists of Synthesizer 1, Synthesizer 2, the Routing Module, Filter 1 and Filter 2.
Synthesizers and Filters can be routed in different ways to
achieve a wide variety of possible sounds.

The 3 main controls of synthesizers, routing, and filters can be modulated by the internal
modulators. Use the Wobble Assignment Page to check out the modulation stuff.

The 3 main controls of synthesizer and filter contain a lamp that shows the current
modulation at work. The Red Light indicates negative modulation, the Blue Light
indicates positive modulation.

The two main controls of the Routing Module show their modulations with the Arrowdisplays. These displays display the final parameter position.

The routing parameters usually fade between two synths and/or two filters. If filters are
placed in series, the filter mix control becomes the distortion amount control.

#### The Synthesizers


Cyclop generates its sound with 3 oscillators: the sub oscillator and the 2 main
oscillators. The sub oscillator is part of the master FX section. The main oscillators are
fairly complex synthesis units which we call Synthesizers 1 and 2. You’ll find then in the
lower left part of Cyclop.


31


Each of the Synthesizers offers 6 different synthesis methods that have been engineered
with a great deal of listening and tweaking, until that special sound was attained that
makes Cyclop so impressive.

The three main controls of the Synthesizer units are modulation targets that can be
assigned in the Assignments Screen.

Cyclop always produces 4 Unison voices. You can offset the pitch of the voices using the
Unison Control. Detune the Synthesizers with each other using the Detune and the
Octave Control.

Power the Synthesizer on/Off using the S1 or the S2 Switch.

Use the menu to load the desired Synthesizer engine.

##### Saw Regiment


This is a special Super-Saw oscillator thet generates 7 sawtooth waveforms running at a
slight pitch offset for a massive sound.
Additionally, the four unison voices can be used to stack octaves.
The Digitize parameter is a frequency-dependent sample rate reducer.

The modulatable parameters:

Super: Offsets the pitch for the 7 saw waves.

Stab: Adds up to 3 octaves to the sound.

Digitize: Special pitch dependent sample rate reduction.


Back to Table of Content


32


##### Analog Sync

This fat and juicy emulation of two analog oscillators which run in sync with each other
gives you some seriously heavy bass sounds.
Modulate the sync frequency to let the beast out of the cage.

The 3 main parameters:

Main/Sync: A cross fader that blends between master and slave oscillator.

Sync F: Sync frequency of the slave oscillator.

PW: Pulse width of the Pulse and the Double Saw oscillators. Goes from 100% narrow to
100% wide. Center position should be used for an equal pulse wave.

RAW: Deactivates a special anti-aliasing method for a rougher sound.

Fixed Frequency: Unlinks the Sync pitch frequency from the master pitch frequency. If
this button is deactivated, the sync frequency will be proportional to the master
frequency.

##### FM


Our idea of easy 3-OP-FM synthesis. A Modulator Oscillator modulates
2 Carrier Oscillators. Two FM algorithms provide a variety of FM sounds that fit snugly to
the Cyclop concept.


33


Main Parameters:

FM 1: Determines how much Carrier 1 is modulated.

FM 2: Determines how much Carrier 2 is modulated.

Mod: Determines overall linear modulation intensity.

Additional parameters:

M: Frequency ratio of the Modulation oscillator. The heart pops up when a harmonic ratio
is chosen.

C1: Frequency Relation Modulator-to-Carrier 1.

C2: Frequency Relation Modulator-to-Carrier 2.

##### Transformer


This very special unit is essentially a wavetable synthesizer. The loaded sample is
analyzed and then sliced into waveform-cycles. These Cycles
can be addressed by the Position Knob. By riding the Position knob with a modulator, you
can read a sample in many ways.

The loaded sample will most likely not sound like before. This synthesis method
completely destroys the sample and puts it together so that it always plays the pitch that
you play on the keyboard.

This synthesis method also allows Formant shifting which is one of the key features of
Cyclop. This is the real vocal synthesizer!

Load any kind of monophonic material for best results.

Main Parameters

Formant: Formant shifting. Double click to set it to center position.


34


Pos: Determines the wavetable that you selected within the sample.
In order to read a loop so that it runs along with your song, modulate
the position control with an upward saw LFO. Put the Lfo Speed to 1 bar.

Use the envelope to read the sample exactly as you desire.

Use the step sequencer to modulate the position control for skipping effects.

Grain: This control allows fine tuning of the grain size that actually defines the size of the
wavetable. Double click for center position.

##### Spectromat


The Spectromat works with 32 internal oscillators that add up to a very complex sound.
The 32 spectral bands give you a huge number of tweaking possibilities. Spread, shift,
shape them, or deactivate bands as you like.

Main Parameters:

Spec: Spectral frequency offset. Spectral bands are offset by up to 5 semitones with
relations to each other. Double-click for center position (2 semi notes spread).

Shape: Select the amplitude curve which is applied to the spectrum.

Shift: The whole spectral curve can be shifted within the frequency domain.

Each band offers an on/off button which works like this:

- Left click to draw

- Right click to erase


Back to Table of Content


35


##### Phase Stressor

The Phase Stressor is our idea of a Phase Distortion oscillator. It is in essence a sine wave
modulated in different ways, including self modulation. The very special display shows
the phase distortion of a sine wave in a spherical coordinate system.

Main Parameters:

Mod: Intensity of waveform modulation.

SelfMod: Intensity of self-modulation. Includes some sonic surprises along the way.

Sym: Defines the phase symmetry of the waveform.

#### The Routing Unit


Cyclop offers a special routing feature for mixing the synthesizer and filter signals in
various ways. There a 4 routings available, most of them include a combination of filters
and synths. If filters are running in series, there is a distortion unit placed between them
to add some sonic spices before the next filter stage.


36


The floating plasma always shows the you way that the audio signal is going, until it
reaches the output which is displayed by a speaker symbol.

The 4 Routings:

##### 1. Parallel


Synth 1 and 2 are mixed with each other. The resulting audio signal runs through filter 1
and 2 simultaneously. The two resulting signals are then mixed together to the final
signal.

##### 2. Serial 1


Synth 1 and 2 are mixed with each other.
The resulting signal then goes to filter1, passes the distortion unit and then goes through
filter 2.

##### 3. Serial 2


Synth 1 and 2 are mixed with each other.
The resulting signal then goes to filter2, passes the distortion unit and then goes through
filter 1.

##### 4. Split


The Signal from Synthesizer 1 goes directly to Filter 1.
The Signal from Synthesizer 2 goes directly to Filter 2.
The resulting two signals are then mixed to the final signal.


Back to Table of Content


37


#### Distortion

The 9 available Distortion units give the synth signal some roughness and dirt, when the
filters are running in series. Routing Ser1 and Ser2.

The same Distortions can be found in the Routing Unit, where distortions are used
between the filters when they run in series.

##### Amp

Amp/Speaker simulation with lots of warmth.

##### Drive

Nice and angry overdrive with a special top end.

##### Dist

Intensive distortion that turns the sound into something new.

##### Diode

The distortion core from the MS-20 filters is used here to provide some mojo.

##### Clip

The audio will be boosted until it clips. Use this unit to just boost your level or to add
some really evil distortion.

##### Sine

The audio signal is boosted and then runs through a sine algorithm.

##### 1-Bit

The audio signal must decide 1 or 0? The hardest digital method.

##### Crush

Nice bit crusher that basically adds some silver to the sound.

##### Digitize

This pitch-dependent sample rate reducer is always good for some digital vocal sounds.


Back to Table of Content


38


#### The Filters

Cyclop offers two identical Filter units that contain 10 all-new filter creations from our
DSP nerds. Most of the filters are saturated in a way that preserves a strong sound —
especially a strong bass — even at high resonance settings. Four different lowpass flavors
cover the sound palette from aggressive (Ms-20-style Lp 2 Pole) to fat (Moog-style
Ladder Lp 4 Pole).

The filters also contain a vowel mode. Activate it to use any filter model in Vowel Mode.

Main Parameters:

Cutoff: Determines the working frequency according to the filter type.

Resonance: Determines the filter resonance/sharpness.

Mix: Mixes the input signal with the output signal of the filter.

##### HP


A highpass filter with 12db depth.
High Pass only lets frequencies pass that are above the cutoff frequency.
This high Pass is a special MS-20 style algorithm that provides a strong bass and a very
rich and colorful attitude.

Back to Table of Content
Perfect for using with the vowel mode.


39


##### BP

A Band Pass filter with 12db depth. Only frequencies at the cutoff frequency pass this
filter.

##### BPLP


A Moog style Band Pass/Low Pass combination.

##### LP 2


2-Pole Low Pass filter with 12db depth. This filter uses a special MS-20-style for the most
juicy and overdriven filter sound that works best with the vowel mode.

##### LP 4


40


4 Pole Lowpass with a darker sound.

##### LP Ladder


4 Pole Low Pass with Moog Ladder Filter flavor. Features a fat sound and a sharp
resonance.

##### MBST


Mid Boost Filter, a mixture of lowpass and bandpass Filters. Sounds pretty fat because it
puts out a good deal of uncommon filter sound.

##### RPL


Ripple Filter. A spectral filter that consists of 4 bands that are shifted within the
frequency domain.


41


##### CMB

Comb filter that is based on short delay times. This one is good for vowels and resonator
sounds.


Back to Table of Content


42


### Native Kontrol Standard NKS

Cyclop is the first SB product to support Native’s NKS standard, giving you the same
deep integration with NI controllers as Komplete Instruments.

The main features of our free update are a plug-and-play support of Cyclop’s presets
browser and carefree tagging/organisation for inclusion in the powerful Komplete
Kontrol / Maschine browser. This lets you search the presets by sound type (e.g. synth
lead), character (e.g. dark) or any combination.

We aimed for most detailed control of Cyclop’s sound engine. Knobs and faders can be
mapped to those on the Kontrol and Maschine hardware in a logical way, with the option
to group similar controls by page. For example: Jump to the Filter page and find the set
of controls related to character of filter.

All presets have been wrapped into .nksf files which contain preset and tagging
information and mapped controls. Browsing through categories, different genres and
moods will speed up producers’ workflow and keep your eyes off the computer screen.

Controller Mapping
We aimed for most detailed control of Cyclop’s sound engine.

All mappings are consistent throughout the different presets.


There are six pages:


1) Oscillator one & two (7 active knobs):


(1)-(6) all main controls for each oscillator from top-right to bottom left
(variable, depending on which oscillator is chosen)

(7)Disable unit

2) Filter One & Two (7 active knobs)

       - the (3) main controls on top

       - Vowelmode on/off

       - Vowel A & B

If any of the above controls are modulated in a preset, you can easily shift the
modulation’s base/starting point via the hardware.


3) Mix/Env/Sound (8 active knobs)

       - Mix ing filter 1 & 2 and oscillator 1 & 2

       - Env elope: Attack and Release/Decay

       - Sound : Sub Osc / Bass / Stereo / Distortion


43


4) Main Knobs (4 active knobs)

    - Wobble

    - Amount

    - FX Sequencer

    - Sound



Back to Table of Content


44


Presets
Cyclop’s NKS preset tagging reflects the categories given in Maschine.


Bank
This category follows Cyclop’s main categories. You can choose between different
styles of SB’s own presets or patches created by artists.

Type
This one gives a rough & global idea of the preset’s instrumental character. Cyclop
being the beast it is, most of the patches fall into the categories monophonic,
bass, synth lead, synth bass, etc.

Mode
This describes the character of the patch.

Properties
More detailed description of the tonal and harmonic feel for each preset.

Saving Presets and assigning individual tags
If you want your own presets accessible in Maschine, load them in Cyclop and save/tag
them in Maschine.

These will be automatically saved as .nksf files.


Back to Table of Content


45


### Host Integration

##### Cubase

Go to the Cubase plugin manager and make a full rescan there.
Make sure that the Cyclop.dll/Cyclop.vst3 (Win) or Cyclop.vst/Cyclop.vst3 (macOS) file is
contained in Cubase‘s assigned VST Plugins folder.


Create an Instrument track and load Cyclop as insert on that track.


Back to Table of Content


46


##### Ableton

In Live it's highly recommended to use the VST version.
The installer will ask you for the VST plugins folder.
Make sure that the Cyclop.dll/ Cyclop.vst3 (Win) or Cyclop.vst/ Cyclop.vst3 (macOS) file
is contained in Ableton Live‘s assigned VST Plugins folder.

At least in Live it can happen that a plugin gets marked as unloadable and will not be
rescanned automatically. You have to force a rescan by unchecking and checking the
'Use custom VST Folder' checkbox in Preferences/File Folder/Plug-In Sources.

Insert Cyclop as an instrument in a MIDI track from the Plug-Ins list.


Back to Table of Content


47


##### Pro Tools

When installing Cyclop, make sure to select the AAX plug-in format.

Launch Pro Tools and create an Instrument track. Load Cyclop as insert on that track.

##### Logic


Choose Cyclop as an AU-Instrument from the I/O dialogue of a Software Instrument
track.


Back to Table of Content


48


##### Sonar

Make sure you set the VST Plug-ins folder that Sonar is using.

Go to Utilities> Cakewalk Plug-in Manager. In the VST configuration section, click on
Options then click Add and select the folder your VST plugin is installed to. Press OK and
click the Scan VST Plug-ins button.


Insert Cyclop as a Soft Synth.


Back to Table of Content


49


##### Studio One

Go to the Studio One menu and choose Options, click on Locations, then VST Plug-Ins.


Click the Add button and select your VST Plugin folder. Press OK then close and re-open
Studio One. If you still don’t see your plugin, go back into that screen and click the “reset
blacklist” button, then close and open Studio One again.

Create an Instrument track and load Cyclop as insert on that track.


Back to Table of Content


50


##### FL Studio

Please go to Options -> File Settings and select the folder your VST plugin is installed to or
double check that you install the “Plug-In”.dll in the VST folder FL Studio is using.


Now please go to Channels->Add one->More...


There you should find Cyclop and do a refresh again.


51


You can now open Cyclop in the Mixer-Inserts

#### MIDI remote


All relevant Cyclop parameters can be controlled via Host Automation.


All relevant Cyclop controls can be remoted via MIDI controllers.

You find the MIDI Learn function when you right click a control.


Back to Table of Content


52


### The Game

While we created the Cyclop Robot logo, lots of funny little bots were drafted. So the idea
to a little shooting game came up, here you can see how it turned out.

Click the Cyclop robot logo to start the game. You can still play MIDI notes while the
game is running.

The Game offers nice methods to just check random presets which are called when you
shoot the little tank, and to create nice sounds by shooting enemies or letting them
break through to create funny melodies according to the selected major/minor scale.

##### Mouse movements in the Game


A mouseclick into the game sets the Hero (your white bot) position.
As long as you hold the mouse down, the robot will keep on shooting.
The vertical mouse position controls the shooting rate.

The Game triggers MIDI notes whenever you shoot, when you hit an enemy, when enemy
hits you or when enemy breaks through.

##### Game Controls


The game offers various controls to get the best out of it.
Basically the knobs decide how the game works together with the Cyclop synthesizer.


53


Spawn

This control determines how many enemies are created and how fast they are. With
higher high score, the spawn will raise internally as well.

Gun Pitch

This control determines the pitch envelope amount for the note triggered by your
shooting.

Kill Pitch

This control determines the pitch envelope applied to the note that is generated when
you kill an enemy. The pitch can go up or down, depending on the position of the knob.
When the knob is set to its middle position, the pitch is not changed.

Root Note

The Key that the scale is based on.

Scale

Determines if enemies that break through create pitches in a major or minor scale.

Gate Time

Overall length of a note, generated by the game.

##### High Score


The highest high score is generally saved.
Your ranking is displayed in the game screen, the high score points are displayed above
the wobble wave display.

##### Points


Erase Enemy: 1

Erase Shooting Enemy: 20

Being Shot: -1

Enemy Breakthrough: -1


Back to Table of Content


54


### Questions?

#### Silence

##### Silence because of empty Gater

Maybe you called a HotKey by accident and it called an FX page with
an empty Gater. Just click and drag with the mouse in the Gater
to activate the tracks.

##### Silence because of Master Level modulation


The Master Level can be modulated, with the second bar in the Assign Screens. If Master
Level is set to Zero by Envelope or Sound Knob, the instrument might produce no sound.

##### Silence because of modulated filter


Filters can mute all audible frequencies. Make sure that Low Pass and Band Pass filters
are not running at minimum cutoff all the time, Band Pass and High pass should not run
at maximum cutoff all the time.

##### Silence because of disables oscillators


A disabled oscillator produces no sound. Activate the S1 or S2 buttons to make sure
synthesizers are running.

##### Silence because of the wrong Serial Number


The wrong serial number disables all sound. Check the serial number in the about screen,
retype it there or just re-install the Cyclop.

#### License




- The Cyclop License covers both the macOS and Windows versions and can be



used on two computers. For any use on more than two computers, you must buy
an additional license.

- You may resell the software (and therefore transfer the license) three months or



more after purchase.



Back to Table of Content


55


### Impressum

Sugar Bytes GmbH | Made of passion
Robert Fehse, Rico Baade | Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395| Str.-Nr. 37/207/21266 | HR-Nr. HRB 124199 B
[info@sugar-bytes.de](mailto:info@sugar-bytes.de) [| www.sugar-bytes.com](http://www.sugar-bytes.com/)


Back to Table of Content


56


