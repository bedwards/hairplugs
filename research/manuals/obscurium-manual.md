# Obscurium User Manual



1


## Table of Content

#### ABOUT ............................................................................................................................... 3 GETTING STARTED .......................................................................................................... 4 1) CLEANING UP THE TABLE .................................................................................................. 4 2) OSCILLATORS ................................................................................................................... 5 3) PITCH ............................................................................................................................... 7 4) MODULATORS................................................................................................................... 9 5) OUTPUT .......................................................................................................................... 10 6) LOOP BARS AND THE TRIGGER SEQUENCER ................................................................... 10 REFERENCE GUIDE ....................................................................................................... 12 MAIN TABS .......................................................................................................................... 12 PLUGIN HOSTING ................................................................................................................ 21 THE SEQUENCERS & LOOP BARS........................................................................................ 24 FLEXIBLE PARAMETERS ....................................................................................................... 26 ARPEGGIATOR ..................................................................................................................... 29 TOOLS ................................................................................................................................. 30 PRESET BROWSER ............................................................................................................... 38 ABOUT SCREEN ................................................................................................................... 39 HOST INTEGRATION ............................................................................................................. 40 TROUBLESHOOTING ..................................................................................................... 46 CAN’T DRAW ANYTHING IN THE SEQUENCER. ....................................................................... 46 OBSCURIUM MAKES NO SOUND ........................................................................................... 46 MY SEQUENCER MOTION LANE GRID IS EMPTY ..................................................................... 46 OBSCURIUM SHOWS STRANGE TEMPO BEHAVIOUR .............................................................. 46 INSTALLATION & UNINSTALLING OBSCURIUM ...................................................... 47 CONTACT & LICENSE ................................................................................................... 49 APPENDIX ....................................................................................................................... 50 SCALES................................................................................................................................ 50

2


## About

Obscurium is a timbral organism, a generative synthesizer feeding on scales, chords and
classic synthesis producing vivid harmonics paired with an elaborate aesthetic. It is the
source of a dazzling array of organic and lively sounds, delivering spherical pads, bubbly
arpeggios and deadly percussion attacks.

Obscurium offers detailed control over the musical grammar of its generative engines: its
results are far from arbitrary. Get the sequencer going and define polyphony, chords and
arpeggiator for each of the 32 steps. Detailed sound controls allow for a free mix between
the FM analogue oscillators and ongoing modulation of three variables for each of the
generators.

The playful user interface streamlines the complexity of the inner workings: You can freely
change and swap all parameters and motion lanes leading to hundreds of new sounds from
the init preset, so you can realize unique and surprising sequences in a matter of a few
clicks. Thanks to its VST interface, you can host any of your sound generator plugins in
Obscurium for fresh sounds.

We hope you will enjoy exploring the depths of Obscurium. In a best-case scenario, our
latest instrument communicates our love for detail, humor and passion for what we are
doing.

Our intention was to make the instrument immediate and intuitive. Your ear is probably the
most important organ here and we believe Obscurium holds a vast potential for the
experienced electronic musician.


Back to Table of Content


3


## Getting Started

Hopefully this section saves you some time. We tried to explain as briefly as possible the
most important aspects of the instrument.


1) CLEANING UP THE TABLE

2) OSCILLATORS

3) PITCH

4) MODULATORS

5) OUTPUT

6) LOOP BARS AND THE TRIGGER SEQUENCER

### 1) Cleaning up the table

Obscurium’s settings, flexible parameters and moving modulators – many of these
interdependent - can be overwhelming at first sight, so starting with a clean slate is
probably the best approach:


INIT preset : Click the vertical triangle in the preset area & go to the USER folder.

If you want an even more reduced approach to Obscurium, you can switch off all its engines
& effects like this:


a) Activate „MIDI only“ in the Pitch Tab to
switch off all generative engines.



b) Switch off all flexible parameters by
deactivating the triangular indicator left to
their slots in the flexible parameter column.

c) Leave the filter on (CUTOFF)! Switching it
off would mute the output.



Flexible Parameter Column,

switch on/off on the left


Back to Table of Content


4


### 2) Oscillators

The oscillators produce the original sound, which is then fed through the filters and effects.

Obscurium has two oscillators: Analogue & FM . Find their main controls in the Sound Tab .


Analogue. The main control is the SPREAD
dial. When set at zero, this gives you
classic, synced oscillation in form of a sawor pulse wave. Cranking up SPREAD will
produce super-saw waves, resulting in
broad pads.


FM. Obscurium’s FM generator uses three
FM modes. These can be routed in three
different ways and harmonized with the
harmonic button (this button also works as
an indicator). You can also regulate the
RATIO between the carrier frequencies and
the modulating frequencies.

Have a look at the flexible parameters: Activate the MIX parameter :

1) Switch on its left indicator and
2) Activate its slot by clicking on its name.

You can now draw the MIX parameter’s motion lane in the sequencer. If you want a clean
analogue signal, draw at the low end of the grid, top for FM.

Start playing with the oscillator’s features in the Sound Tab and the flexible parameters:

#### Analogue

Check out the Analogue section of the flexible parameters:


SNCFRQ Sets the sync frequency of the analogue oscillators.
PW Pulse Width of the analogue pulse wave.
WAVE Min=SAW, Max=PULSE -> relates only to the lower half of the SPREAD
dial when the analogue oscillator is on synced oscillation.

#### FM

We included three operators to spice things up.

These three operators can be routed in three different ways (serial, parallel & always
harmonic).


5


The interaction between modulating frequencies and carrier waves can produce unique and
live-like sounds unachievable with other types of sound synthesis.

Flexible Parameters:


FMX This parameter controls the carrier frequencies of the three
FM operators. It covers a massive spectral playground and
should be used carefully. It works similar to the „Ratio“
control in the Sound Tab, but if the Ratio is harmonic, the
carrier frequencies will also be harmonic. In Routing Mode 3
(Sound Tab) it controls formant-shifting.

FM1 This parameter controls the amount of frequency
modulation of the three operators. If this parameter is
raised, the timbre will become brighter.

FM2 This parameter controls a feedback circuit within the FM
algorithm, adding complexity to the spectrum.


Back to Table of Content


6


### 3) Pitch

Here’s where the magic starts: Obscurium generates notes, sound, pitch along with the
notes you are playing on your keyboard.

Switch off the MIDI only option in the pitch tab to activate Obscurium’s pitch features.

Pitch can be controlled via the Pitch Tab (fixed settings) or the top-five (flexible)
parameters. Both controls have maximum impact on Obscurium’s output.

#### Pitch Tab (fixed settings)

The Pitch Tab holds the general fixed settings for Obscurium’s generated voices (up to
seven):

OCTAVE

Octave sets the root note’s position of Obscurium’s generated
voices by +/- 2 octaves.

DETUNE

Detune Obscurium’s voices from each other to achieve more
organic results.

GLIDE

Glide will create smoother transitions between the individual
pitch voices over time. It works as a classical portamento control
and causes the pitch to glide from one note to another.

SCALE



Choose from 34 different scales to define the harmonic
structure of the generated voices. A detailed overview of
the different scales can be found in the APPENDIX.

CHORD TABLES



The chord table picks notes from the scale selected and
stacks them to a chord. One chord table consists of 24
chords.

MIDI ONLY



This will switch off Obscurium’s voice generator.



Back to Table of Content


7


#### PITCH: Flexible Parameters

ARP The Arpeggiator automatically steps through a generated sequence of
[notes based on the input chord and the scale selected, thus creating](http://en.wikipedia.org/wiki/Chord_(music))
an arpeggio. Define the arpeggiator’s offset in the central grid (max. +
3 octaves) and/or with the pitch parameter.

The Arp uses the current 8-voice pitch and has its own polyphony. Just
open the AMP ENV Tab and use the ARP control to define the
polyphony of the arpeggio.


MOD This is a plain manual modulator . Define its amount in the central grid.
Choose from these targets:




- the Arp Envelope’s



Attack/Sustain/Release (see tab AMP
ENV)

- The main modulators themselves



(envelope’s ASR and the LFO rate (see tab
MODS)).



PITCH Fine tunes the root note of the generated voices/chords (max +24).

CHORD Depending on your chosen SCALE and CHORD TABLE in the pitch tab,
you can trigger any of up to 24 chords in the central sequencer.


Usually 24 chords are available (unless you chose the 54 chords table).

In the PITCH Tab, you can select chord tables and scales.

POLY Check the y-axis in the sequencer – it shows the total number of voices
played by Obscurium (one up to eight).


Here, the maximum polyphony is defined. For each step in the motion
screen, you can define an individual value. This also affects the
arpeggiator polyphony in the AMP ENV tab.


Back to Table of Content


8


### 4) Modulators

Obscurium offers six modulators:


An envelope follower, tracking the amplitude of the output (MODS tab)
Targets: all flexible parameters

A Low-frequency oscillator (MODS tab)
Targets: all flexible parameters

The MOD parameter as part of the Motion Sequencer (flexible parameters)
Targets: AHR envelopes, LFO rate (AMP ENV & MODS tab)

LFO, envelope & Step Sequencer (MORPH pop-up)
Target: Morph- and Shift Fader

For the sake of clarity, we will focus on the
envelope follower and the LFO here:

The MODS tab holds settings for envelope’s AHR,
the frequency of the LFO and the modulators’
principal amount controls.

Each flexible parameter can be made a target for
these two modulators.

The tiny column chart next to the parameter’s
name holds a pop-up to


1) Define the final min/max values  - „final“ meaning after the y-axis setting in the

sequencer and after modulation impact.
2) Parameter’s individual amounts of the incoming modulator signal (ENV & LFO)


Back to Table of Content


9


### 5) Output

#### Filter

Obscurium’s Filter can be controlled via the flexible parameters in the central grid.


CUTOFF Define cutoff frequency between 35Hz and 16 kHz – switching
this parameter off will mute Obscurium’s output!
RESONANCE Set the filter’s resonance.
TYPE Use the grid to switch between Low-, Band- & High Pass.

#### Tab „AMP ENV“


ARP Envelope
The ARP ENVELOPE is triggered on a step by step basis through the white-globe sequencer
at the bottom. It is the gateway to Obscurium’s arpeggiator opening up the dynamics of
Obscurium’s generated pitch.

MIDI Envelope
Use the MIDI envelope to manipulate the amplitude of the incoming signals.

### 6) Loop Bars and the Trigger Sequencer

#### The Trigger Sequencer


This sequencer triggers the Arp Envelope (to be found on the AMP ENV tab) and the Mod
Envelope (to be found on the MODS tab).

Also, each trigger will select voices from the current scale for the arpeggiator.

#### The Loop Bars


The Loop bars determine which part of the sequence is being played.

The upper Loop bar sets the part played by the THE MOTION SEQUENCER.

The Loop bar below defines the part of the sequence which is played by the Trigger
Sequencer.

10


Drag the start- and endpoints to resize the loop bars. Drag the centre to move the loop bars.

The loop bars also determine which part of the sequence is used for copy and paste.

Goodies

1. Obscurium’s PLUGIN HOSTING
2. Tune in to the universe: changing Obscurium’s MASTER TUNE.
3. SHIFT FADER.
4. MORPH between two sequencer states.
5. Work with the MODIFIERS.
6. SUPER OBSCURE MODE.
7. STEP KEYS/ STEP PLAY Feature.


Back to Table of Content


11


## Reference Guide

MAIN TABS
PLUGIN HOSTING
THE SEQUENCERS & LOOP Bars
FLEXIBLE PARAMETERS
TOOLS
PRESET BROWSER
ABOUT SCREEN

### Main Tabs


Obscurium’s tabs hold a variety of settings throughout the signal path:


CLOCK : all you need to read the sequencer.

PITCH: all about Obscurium’s harmony.

AMP ENV controls the duration and the amplitude shaping.

MODS controls the properties of the two modulators.

SOUND controls the sound generating engines / Plugin Hosting

GENERAL Other Settings.


Back to Table of Content


12


#### CLOCK

The Clock Tab offers general settings for the
speed and style of reading through the
sequencer.

The mini sequencers for clock and direction
need to be activated via the on/off switches
on the right.


CLOCK

Here you set the note length of one
step. Usually you would work with
16 [th] or 8 [th] notes, but here, also
tripled divisions are available.



DIR


SWING



The running direction of the sequencer. We implemented the usual options like
forward, backwards, ping pong and random. Try 2 [nd], 3 [rd] and 4 [th] to play every
second, third or fourth step in the sequencer.


This will add a triolic feel to your groove, adding a delay to every
second step.



LEGATO
Activating Legato will result in an uninterrupted sequencer movement once an additional
note is pressed.


STEP KEYS
Since we have 32 steps, we can put the information of the steps to 32 keys! With this
button activated, the clock will run no longer and each key on the keyboard (from C1 to G3)
now relates to a single step in the sequencer.


STEP PLAY
If this button is on, the sequencer will move one step ahead when you hit a key. Hit two keys
at once to reset to the first step.


OBSCURE CLOCK

This sequencer lets you change the tempo
divider in ¼ note steps .
So you can change tempo on the fly.
That will make some great stumbling
grooves: put in some triplets and rolls…


13


OBSCURE DIRECTION

This one also runs at quarter note speed.
The upper field determines the playback
direction. The direction contains funny
settings like playing each 3 [rd] or 4 [th] step, or
staying on a step for a number of counts.

The circled numbers set the number of repeats for each step. If the master clock is set to
1/16 notes, give it a 4 to make the step last for one bar. 8 would be two bars then.


Back to Table of Content


14


#### PITCH

The Pitch Tab offers vital controls for the
generative engine.

As a pitch generator, Obscurium will take
what you play on the keyboard and add
melody and rhythm to it. When you play
one note, Obscurium can add up to 7 more.
When you play more notes, Obscurium will
prefer the MIDI notes over the generated
notes, but still the MIDI notes will be
matched to the scale selected.

The lowest note played on the keyboard is the root note for generated scales and chords.
The Pitch sequencer lane can change the root note by +/- 2 octaves.


OCTAVE

The overall octave has a huge impact on sound. Try the setting that fits best: deep
and sinister or shimmering and glimmering. The octave setting is also displayed by
the keyboard, where the circle-icons show the final pitch.



DETUNE


GLIDE



Detune the synthesizer-voices with each other. This results in a subtle and more
organic pitch.


The pitch will slide from one voice to another with increasing glide time, as you
crank up the knob: a classical portamento control.


Back to Table of Content


15


SCALE



Choose from lots of scales to define which notes will be played. Different
scales will change the harmonic structure of your sound. Click here for a
detailed explanation of the scales concept.



CHORD TABLES
The chord table picks notes from the selected scale and stacks them
to a chord. One chord table consists of 24 chords.

A chord table contains 24 variations. The CHORD motion lane will select any one of the 24
chords available.

The 54 chords table is taken from our MIDI Sequencer Thesys and contains, yep, 54 chords.

The chord is based on the root note. The root note is the lowest note
on the keyboard, plus the Pitch sequencer value.


MIDI ONLY

This will bypass all pitch generation and Obscurium will strictly use
the pitch played on the keyboard. The number of MIDI voices might
still be altered by the POLY parameter.


Back to Table of Content


16


#### AMP ENV

Two Attack/Hold/Release (AHR) envelope
generators work together to shape the final,
polyphonic amplitude of Obscurium’s output.

The Arp envelope can be modulated via the MOD
parameter.


Arp Envelope
The ARP ENVELOPE is triggered on a step by step basis through the
white-globe sequencer at the bottom. It is the gateway to Obscurium’s
arpeggiator opening up the dynamics of Obscurium’s generated pitch.



MIDI Envelope



Use the MIDI envelope to manipulate the amplitude of the
incoming signals. This one works together with your finger on the
keyboard.



MIX
Crossfades between ARP envelope (top) and MIDI envelope (bottom).


MOD


The MOD motion lane comes into play here.

Activate the MOD buttons to modulate envelope times via the MOD parameter.


Back to Table of Content


17


ARP

The Trigger Sequencer starts a voice for the arpeggiator and this knob sets the
number of voices played simultaneously by the Arp – it defines the Arp’s
polyphony.

Obscurium generates up to eight voices of pitch, so up to eight voices can be
triggered here. Note, that the POLY motion lane can still limit the polyphony .


0: full eight-voice polyphony (including your input). Here, the Arp would be
hardly audible as it always plays all voices.

50: The Arp will cycle through the available voices playing a stack of four
voices.

100: One voice monophonic. Here the Arp will cycle through the available
voices, only playing one note at a time.


Velocity

MIDI Envelope Velocity. Here you can determine how much MIDI velocity will be
affecting the MIDI envelope output level.


Bottom: no velocity, Top: full velocity.


Back to Table of Content


18


#### MODS

The Mods Tab offers access to Obscurium’s
main modulators: Envelope and LFO . These
can be assigned to modulate any of the 16
flexible parameters.

In the MODS tab, you can affect the principal
Amount for both these modulators.
Both of the amount controls here are
powerful weapons that control the overall
sound of Obscurium in an uncanny way.
Tip: MIDI-Learn them for massive sound
changes at your fingertips.

Besides the general amount setting here, you can also define the modulators’ impact on the
flexible parameters in their individual settings.


Envelope


The envelope controls focus on Attack/Hold/Release (AHR) and
is triggered by MIDI notes and the trigger sequencer (below the
motion lanes).


LFO


The LFO generates a sine wave, and the rate can be set in 1/16 [th]
notes.


MOD


The envelope controls and LFO rate can be modulated by the MOD motion lane.

That makes it possible to vary your sequences with flexible AHR times and varying
LFO rates. The LFO rate goes from 0Hz to 100Hz and is retriggered with MIDI notes.


Back to Table of Content


19


#### SOUND

This tab holds the controls for Obscurium’s
sound generators, three classic effects and
access to the host functionality .

Use the pan control to generate random
stereo effects.


SPREAD
The Analog Oscillator’s main control is
Spread . This control crossfades between the
sync oscillator with a saw or pulse wave
(min/max of the “WAVE” parameter) and a
super-saw for broad pads and strings.


ROUTING
The FM Oscillator features three routing
modes (serial, parallel & always harmonic), a ratio control and an “Always Harmonic” button
which will allow harmonic ratio settings only. The third routing mode is always harmonic
whatever your ratio setting.


EFFECTS

The effect controls are split, there’s a knob and a fader. The knob controls the amount, the
fader the dry/wet mix of the respective effects.

The delay uses 16th notes as a resolution:


0: One 16th note delay
50: One bar (16 16th notes)
100: two bars (32 16th notes)


Back to Table of Content


20


#### Plugin Hosting

Obscurium offers plugin hosting as an experimental
sound-design feature . We put in a lot of effort into
this based on our expertise we gathered when
developing Trans VST. However, we also faced some
instability with outdated plugins. The older software
just can’t cope with the data being sent by
Obscurium. We recommend saving your preset
before going into hosting.

Obscurium will only be able to host 64bit.
On a MacBook with Apple M1 Silicon CPU make sure
to launch the related version, native ARM64 or Intel.
Obscurium will not be able to run Intel-based plug-ins
under Rosetta 2 in a DAW that is running natively on
Apple Silicon (and vice versa)! So to use your ARM64 compatible plug-ins you should launch
Obscurium within a native Apple Silicon version of your DAW. To use your Intel-based plugins you should launch Obscurium within your DAW (or the standalone version of
Obscurium) via Rosetta. Therefore just right-click your DAW (or the Obscurium standalone)
icon in the applications folder and select “Open using Rosetta”.This will force it to launch in
Intel compatible mode.


If Plugin Mode is activated, the internal sound engine will be bypassed and a
plugin can be used instead. The lower 11 flexible parameters can be sent to the plugin as
automation data. The top five remain in Obscurium


Plugin Menu

Rescan All
This should be your first step when you plan to integrate
your existing plugins into Obscurium. Obscurium’s
scanner will focus on the installation VST path, unless you
Select VST Path.

Rescan Blacklist
Will rescan previously excluded/crashed/unloadable plugins.

Update Plugins
Initiates a new scan, ignoring the plugins already registered with Obscurium – this option
will save you time, when you want to include a recently installed plugin.

Unload
This button will remove the currently loaded plugin from Obscurium.

Select VST Path
Here, you can select a path for Obscurium’s VST scanner manually.

Back to Table of Content


21


Preset
If available, plugin presets will be shown here.


GUI Button


Open the plugin’s graphical user interface.


Assignment Presets
Save and Load plugin-specific automation assignments.


Parameter Displays (1-11)
Click to learn or unlearn an automation parameter.

Click for learn mode, then open plugin interface and move the control you want to learn.
The display will then show the name of the assigned parameter.


Learn All Button


This will activate the sequential learn mode and makes it possible to learn all 11

parameters one after another:


Click to activate learn mode.
Open plugin interface and move 11 controls, one after another.

You can now see that all 11 automation parameters are assigned to their respective plugin
controls.


Unassign All Button


Click this button to unassign all automation connections.


Random Assign Button


Click this button to assign all automation lanes at once, randomly.


Back to Table of Content


22


#### GENERAL

Ignore Program change
Only presets from the folder “MIDI Programs” will be
used for program changes. Incoming program-change
messages will be ignored.


CC Map
Load or save your current MIDI CC assignment.


Isolate CC Map from Preset Change
MIDI-CC assignments (MIDI Learn) will still be saved or
changed along with the presets.


Master Tune
[Tune the whole instrument. Have a look for more details: THE GOD NOTE](http://motherboard.vice.com/read/the-fringe-audiophiles-who-want-to-topple-standard-tuning)


Lag
This lag processor will interpolate all data changes over a certain amount of time.


Latch by the trigger sequencer
All data will be triggered by the Trigger Sequencer. That means no parameters will change
when no trigger is played. When your sequence includes un-rhythmical sound changes, you
should activate this control.


Isolate Plugin from Preset Change
You can unchain the plugin from being recalled. This makes it possible to change
Obscurium presets without losing the plugin and its related settings.


MIDI OUT
The same MIDI that is sent to the plugin hosting interface is also sent to the MIDI-out port.

Additionally, the same 11 Motion Lanes that are used for plugin automation can be
assigned to MIDI CCs.
Enter the MIDI CC page in the General Tab.


Use the CC number as a knob to dial in the desired CC
number. The display to the right will show the General
MIDI (GM) standard target.



Use the preset menu to save your CC assignments.
Assignments are being saved and recalled with the
host’s song file.

Activate the Isolate feature to prevent your
assignments from being changed by Obscurium’s
global presets.



Back to Table of Content


23


### The Sequencers & Loop Bars

#### The Motion Sequencer

The Motion Sequencer basically is a step sequencer and contains 16 motion lanes, one for
each flexible parameter.

Each lane has a certain colour and represents one of 16 flexible parameters on the righthand side of the instrument: click the name of any parameter to activate its motion lane.

The Motion Sequencer has 2 states. You can morph between these, using the MORPH FADER.

Motion lane assignments can be shifted around, using the SHIFT FADER. If Shift is at work,
Motion Lanes will switch places with each other.

The Draw Tools offer different ways to draw modify or just randomize sequences easily.


Back to Table of Content


24


#### The Trigger Sequencer

This sequencer triggers the Arp Envelope on the AMP ENV Tab and the Mod Envelope on the
MODS Tab. You can also Latch by the trigger sequencer in the GENERAL Tab.

Also, each trigger will select voices from the current scale for the arpeggiator.

#### The Loop Bars


The loop bars determine which part of the sequence is being played.

The upper loop bar sets the part played by THE MOTION SEQUENCER.

The Loop bar below defines the playground of THE TRIGGER SEQUENCER.

Drag the start and endpoints to resize the loop bars. Drag the centre to move the loop bars.

The loop bars also determine which part of the sequence is used for COPY/PASTE.


Back to Table of Content


25


### Flexible Parameters

The flexible parameter section contains 16 slots to manipulate
Obscurium’s manifold levers. Each of the 16 parameters is
represented by a motion lane in Obscurium’s sequencer.

To manipulate a single parameter in the motion lane sequencer,
click and highlight its name               - the 32 positions of this parameter
in the sequencer will then be circled and you can vertically
adjust them for each step.


Deactivate individual motion lanes via the indicator buttons
on the left.


The Button to the right unchains the parameter from the
SHIFT FADER. For example: If you like your Pitch and Chord,
unchain these parameters from Shift, so they will not change
when you move the Shift Fader.


Each parameter slot contains a little horizontal meter displaying the final
value, being the sum of motion lane value, envelope and LFO, within the Min/Max range
chosen.


The vertical meters offer a quick look at the parameters’ settings. The four
vertical columns show (from left to right):


           - Envelope amount,

           - LFO amount,

           - Min value and

           - Max value

Click the display to open the Parameter window .

The Min/Max controls determine the range for the final parameter
value .

If you shift the parameters around using the Shift fader, the Min/Max
range is a handy tool to keep your overall sound within a range.


Back to Table of Content


26


Here are all 16 flexible parameters explained in detail:

#### ARP

The ARPEGGIATOR is the first of the PITCH parameters. These cover the
generative engine of Obscurium.

ARP offers detailed control over the positioning of the generated notes.
The y-axis of the motion-lane sequencer is divided into three octaves.
These three octaves cover eight notes each.

#### MOD

This is a plain manual modulator . Define its modulation in the
motion-lane sequencer. Choose from these targets:




- the Arp Envelope’s Attack/Sustain/Release



(see tab AMP ENV)

- The main modulators themselves



(envelope’s ASR and the LFO rate (see tab
MODS)).

Use Envelope and LFO in the MODS Tab to modulate MOD.


#### PITCH

This parameter adds up to 24 notes to the root pitch note coming from
MIDI and so it will shift scale tunings and chords.

#### CHORD

CHORD selects one of 24 available chords.

Different chord tables can be selected in the edit screen. Chords always
have the basic pitch as root note. The basic pitch is the lowest note you
pressed on the keyboard. The “54” chords table contains 54 chords.

#### POLYPHONY

Here, the maximum polyphony is defined. This also affects the
arpeggiator polyphony in the AMP ENV tab.

Defines Obscurium’s polyphony from 1 to 8 voices.

#### MIX

Crossfades between the Analog and FM Oscillator.

#### WAVE

Crossfades between Saw and Pulse wave when the SPREAD setting
turned to its lower end, producing classic, synced oscillation in form of
a saw- or pulse wave (cranking up SPREAD will produce super-saw waves).



27


#### SYNFRQ

Sync frequency of the analogue oscillator.

#### PW

This parameter controls the pulse width of the Analog Synth’s
pulse wave. It also controls the super effect of the Super Saw
oscillator.

#### FMX

This parameter controls the carrier frequencies of the three FM
operators. It covers a massive spectral playground and should
be used carefully. It works similar to the „Ratio“ control in the
Sound Tab, but if the Ratio is harmonic, the carrier frequencies
will also be harmonic.
In FM Mode 3 it controls the formant-shift feature.

#### FM1

This parameter controls the amount of frequency modulation of
the three operators. If this parameter is raised, the timbre will
become brighter.

#### FM2

This parameter controls a feedback circuit within the FM algorithm,
adding complexity to the spectrum.

#### NOISE

Provides noise when air is needed for pads and atmospheres or
noise cymbals for percussions.
This control defines the level & the filter frequency of the noise
algorithm.

#### CUTOFF

Filter Frequency.

#### RESO

Filter Resonance.

#### TYPE

Filter Type (LP, BP, HP).
Tip: Use the Low Pass for Kick drums, Hi-Pass for Hi-Hats.



Back to Table of Content


28


### Arpeggiator

Obscurium generates up to 7 voices of pitch, according to the
settings on the PITCH tab.

The arpeggiator can trigger these voices in order to create melodies
and rhythmic chords.


The ARP ENVELOPE triggers the arpeggiator (in concert with the
Trigger Sequencer). Shape its amplitude via the AHR faders on
the AMP ENV tab.

The ARP knob then determines how many voices the
arpeggiator will play.

On the AMP-ENV tab, the arpeggiator is crossfaded with the MIDI ENVELOPE, which is the fully
polyphonic pitch stack. So if you don’t hear the arpeggiator working, make sure the
crossfade is on top position, and the Arp knob should be cranked up.

The flexible parameter ARP selects the basic voice for the arpeggiator. If you apply an LFO
modulation to the parameter, you will hear how it changes voices quickly.


Back to Table of Content


29


### Tools

#### Keyboard

The virtual keyboard shows the MIDI input and the notes generated by Obscurium’s pitch
engine, and can also be clicked with the mouse (Left click to trigger a key).


The vertical click position within a key determines the velocity.

Right click to lock a key, left click it to unlock it.

The MIDI input is displayed with rectangles.

The generated pitch is displayed with circles.

The red circle shows the root note. (The root note is the lowest MIDI-note, plus the value
coming from the PITCH parameter).

Obscurium generates an 8-voice pitch representing a chord.

#### Draw Tools

The Draw area delivers a lot of features to create and edit motion sequences. For manual
drawing there are different tools available, you can edit the existing data or let the Super
Obscure Mode write a whole new sequence.


The Draw Tools are for manual drawing of a motion lane or for all motion lanes at once.

Different shapes help you creating beautiful content: just click a draw tool to select the
respective mode.


Draw All


Draw all is to draw all motion lanes at once. You can use this feature to define an overall
starting point for a new sequence.

Back to Table of Content


30


The “Offset” control defines the vertical offset for all parameters. Drawing all lines at once
with different offsets here and there leads to magical results and is the hot tip for
percussive sequences.


Free Draw

Click on the fountain-pen control to activate the free draw mode.
You can now freely draw a motion lane; change the amount of horizontal
data points.



Line Draw


Random Draw


Sine Draw



Click the “Ruler” control to activate the line draw tool.
Depending on the angle of the “ruler” control, you will now draw ascending
/ descending motion lanes.


Click the “Brush” control to activate the random draw mode.
The Brush control determines the random intensity.


Click one of the Sine controls to select the sine draw mode.
Define frequency and amplitude (bipolar) with the two controls.


Back to Table of Content


31


#### Modifiers

In order to change the sound of a single sequencer step, but also to create a whole new
sequence, the modifiers come in quite handy. Here you can edit all step data at once and
transport that step data all along the sequencer.


Lock Button
This button locks the play position. When you are editing a step with the modifiers, activate
the Lock button to hear that step only.

Deactivate the Lock button to hear the whole sequence while still editing the selected step.

Keep in mind that the copy function will always copy the step which is currently playing.
With the lock button disabled, there might be surprises when using the copy / paste
function of the Modifiers section.


ALL Button

This button (above the modifiers) will apply any modification to all parameters of
the step selected. Deactivate to edit the selected parameter only.


Copy & Paste

In the middle you have copy/paste buttons.

These copy the data of the selected step, in order to paste it on another step.



Swap



Click these buttons to swap data with the step to the left/right. Use this
control to push a certain sound to a certain position within the sequence.



Step Edit
On the top you see the number of the currently selected step.


Copy selected step


Click this button to copy the data of the step selected to the right/left. This will
erase the data of the target step and replace it with the data of the source
step. Use this control to spread a certain sound across a certain area within the sequence.

32


Furthermore, there are 3 controls to change the data of the selected step:

Move Modifier:

Click this control and drag the mouse up or down to move the step data vertically.
On the upper and lower edges of the screen, the step data will be mirrored. That
means, when step data rises across the upper frame border, it will then go down until
it reaches the lower edge.


Stretch/Shrink Modifier:
Click this control and drag the mouse up to stretch the step data. Step data will be
moving away from the mouse position.

Drag the mouse down to shrink the step data. All step data will be moving towards
the mouse position.


Rotate Modifier:
Click this control and drag the mouse up or down to rotate the step data. This works
exactly like the Shift Fader, but in a more destructive way.

Rotating the step data leads to massive sound changes, as the parameters and their
related motion lanes are mixed up.

Use this to find different sounds for the step selected.


Back to Table of Content


33


#### Super Obscure Mode

The Super Obscure Mode selects individual draw tools for each of the 16 motion lanes and
draws a whole new sequence. All draw-related settings are randomized within a certain
range.


Super Obscure Mode on/off


Switch on to generate new random/obscure patterns for each step and
eventually complete sequences


Loop Obscure Mode

When activated, the Super Obscure mode will remain active once you have

completed a sequence or reached the end of the loop bar. Deactivate to autoswitch off Super Obscure at the end and continue playing the sequence
generated before.



Grid


Multiply


Add



Draw-settings will be randomised once the given
number of steps has passed: 1: will randomize on
each step. 16: will randomize every 16th step.


Control the vertical spread of the randomized data here. If cranked up, data
points will be mirrored at the top and at the bottom of the sequencer.


This knob controls the vertical center position of the randomized data points



Random-Add

This one will randomize the vertical center position (Add).

TIP: After using Super Obscure, focus on parts of the sequence with the Loop bar and use
the copy/paste functions to extend this parts to the whole sequence (copy/extend loop
bar/paste). Copy your writing to the other morph slider position and then use obscurity
again for the current morph slider position. Then you have two cool states to morph
between.

Back to Table of Content


34


#### Shift Fader

The Shift Fader changes the Motion Lane/Parameter assignments. That means the control
curves are controlling different parameters, depending on the shift fader position.
Put the fader to the bottom in order to have no shifting.


Shift Mode


The Shift can be done in a continuous fade mode or stepped mode.

If the Shift is used in stepped mode, a modulation lane is always fully connected to a
parameter. However, if the Shift is in fade mode, the parameter/motion lane connection
changes will be interpolated. That might result in two lanes controlling one parameter.
It might also means that drawing affects two lanes at once.

The Shift fader can be modulated from the MORPH WINDOW.
If the Shift fader is modulated, you see a ghost of the fader moving along.

Troubleshooting Tip: When you experience crazy timings, first look into the obscure tempo
modes to make sure


1) tempo- and direction-sequencer are off,
2) Step play and step keys are deactivated.


Back to Table of Content


35


#### Morph

The Morph Section allows you two crossfade between two sequencer states (except the
trigger sequencer). You can easily create variations by using the copy/paste buttons.

#### Morph Fader

The Morph fader is used to crossfade between the 2 states of the motion and the trigger
sequencer. While the data transition is interpolated, the copy and paste targets switch at
the 50% fader position.

#### Copy/Paste

The Copy/Paste is a powerful function to create patterns. Each morph fader position (A &
B) has its very own copy and paste…

Copy/Paste always uses the space between the loop bars.

Copy 4 steps into the clipboard, extend the loop bar & paste to loop the 4 steps.

#### Morph Window

The morph window offers the modulators for the Morph and
Shift fader. You can activate/deactivate modulation and set
the amounts here.


Morph Fader modulation is active


Shift Fader modulation is active

‘+’ – positive modulation (adding to current value)
‘-‘ – negative modulation (subtracting off current value)


Back to Table of Content


36


Manual
No automated modulation...just grab the faders and move
them.


LFO
Sine LFO, with a rate between 1/16 [th] and 32/16 [th] notes.


ENV
AHR Envelope, triggered by MIDI.


SEQ
A simple eight-step sequencer, with a step rate from 1/16 [th]
note to 32/16 [th] notes.



Back to Table of Content


37


### Preset Browser

The upper right-hand corner houses the Preset Browser.

Click the name of the current preset to open the preset library dialogue or step through the
factory presets via the < > buttons.


Click “Save Preset” to save your own presets in the
“User” folder.
The factory presets are stored here:

/USER/Documents/Obscurium/Presets.

In default mode, MIDI assignments are saved along
with the Preset. Activate “Isolate CC Map from
Preset Change” to avoid presets from recalling CC
assignments when loaded.


Back to Table of Content


38


### About Screen

Clicking the Sugar Bytes logo at the bottom right of Obscurium opens the
About Screen.

Your Serial Number is shown in the lower left-hand corner, along with its validation status. If
you entered an incorrect serial number it will be marked as invalid. The serial number is
needed for downloading updates and additional content.

Click NEED HELP for quick access to this Manual.

Click the Sugar Bytes Logo to open the Sugar Bytes Website.


Back to Table of Content


39


### Host Integration

#### Cubase

In the Cubase plugin manager, perform a full rescan.

Ensure that the Obscurium.dll/Obscurium.vst3 (Win) or Obscurium.vst/Obscurium.vst3
(macOS) file is in Cubase's assigned VST Plugins folder.


Load Obscurium as Instrument on an Instrument track.


Back to Table of Content


40


#### Ableton Live

When on Mac macOS, we highly recommend using the VST version of Obscurium in Live.
Ensure that the Obscurium.dll/Obscurium.vst3 (Win) or Obscurium.vst/Obscurium.vst3
(macOS) file is in Ableton Live's assigned VST Plugins folder.

In Live, plugins sometimes get marked as unloadable and aren't rescanned automatically.
If this happens, force a rescan by unchecking and checking the 'Use custom VST Folder'
checkbox in Preferences/File Folder/Plug-In Sources.


Set up a MIDI track and insert Obscurium as instrument.


Back to Table of Content


41


#### Pro Tools

When installing Obscurium, select the AAX
plug-in format.

Use Obscurium as an instrument.

#### Studio One

Go to the Studio One menu and choose Options. Click Locations, then VST Plug-Ins.


Click the Add button and select your VST
Plugins folder. Press OK then close and
reopen Studio One. If you don’t see the
plugin, go back into the settings screen of
Studio One and click the Reset Blacklist
button, then close and open Studio One
again.

Create an instrument track and pick
Obscurium up from the Instrument list.


Back to Table of Content


42


#### Sonar

Ensure that Obscurium is installed in the VST Plugins folder used by Sonar.
Plug Obscurium as a 'soft synth'.

#### Logic

Choose Obscurium as an AU-Instrument from the I/O dialogue of a Software Instrument
track.


Back to Table of Content


43


#### FL Studio

Go to Channels>Add one>More...


There you should find Obscurium and do a refresh.


You can now open Obscurium in the Mixer-Inserts



Back to Table of Content


44


#### MIDI remote

Most of Obscurium’s parameters can be controlled via host automation and MIDI controllers.


Right-click/Ctrl+click a control to bring up the MIDI Learn option.


Back to Table of Content


45


## Troubleshooting
### Can’t draw anything in the sequencer.

Most probable reason is that „Draw All“ is activated in the Draw Tools

### Obscurium makes no sound

MIDI envelope or Trigger?
Cutoff Frequency needs to be activated!
Check if your serial is valid in the About Screen (Click Sugar-Bytes logo)

### My Sequencer motion lane grid is empty

Probably your audio engine is used by another program.

### Obscurium shows strange tempo behaviour

When you experience crazy timings, first look into the obscure tempo modes to make sure
tempo- and direction-sequencer are off and step play and step keys or pitch recording are
not activated.


Back to Table of Content


46


## Installing Obscurium & Deleting it

#### Installation

[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)

The standalone version and manual will be installed to

Windows: C:\Program Files\Sugar Bytes\Obscurium
macOS: /Applications/Sugar Bytes/Obscurium

Presets will be installed into Documents\Sugar Bytes\Obscurium

Do not move Obscurium presets after installation!

#### WINDOWS

Default installation paths:
VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins

#### macOS

All versions of Obscurium will be installed by default.

Default installation paths:
VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins



Back to Table of Content


47


#### Uninstalling

To uninstall Obscurium:

#### Windows: Uninstall Obscurium under Control Panel>Add/Remove Software. macOS: Delete all the following files and folders.


/Applications/Sugar Bytes/Obscurium
/Library/Audio/Plug-Ins/VST/Obscurium.vst
/Library/Audio/Plug-Ins/VST3/Obscurium.vst3
/Library/Audio/Plug-Ins/Components/Obscurium.component
/Library/Audio/Plug-Ins/Components/ObscuriumMidiFX.component
/Library/Application Support/Avid/Audio/Plug-Ins/Obscurium.aaxplugin

~/Documents/Sugar Bytes/Obscurium
~/Library/Preferences/com.sugar-bytes.Obscurium.plist
~/Library/Preferences/Sugar Bytes/3rdParty (Disregard this file, if you also are an
owner of Sugar Bytes Nest!)

'~' means: /Users/YOURLOGINNAME (your home folder)

If you cannot locate your Library folder in Finder: Select the "Go to Folder" from the Finder's
Go menu and enter '~/Library'.)

#### Authorization

The serial number is requested during installation. If the serial number is missing or
incorrect, the software will not produce any sound. Check the About page to see if your
serial is VALID. Entering the correct serial number or a quick reinstall should fix any issues.


Back to Table of Content


48


## Contact & License

License covers both the macOS and Windows version and can be activated on two
computers. For use on more than two computers, please buy an additional license.


Sugar Bytes GmbH | Made of Passion
Greifswalder Str. 29 | 10405 Berlin, Germany

phone:+493060920395

[info@sugar-bytes.de](mailto:info@sugar-bytes.de)
[www.sugar-bytes.com](http://www.sugar-bytes.com/)


Back to Table of Content


49


## Appendix
### Scales

All Scales available in the scale menu, with C as root note:

```
    Chromatic:  C C# D D# E F F# G G# A A# B

    Major:  C D E F G A B

    Dorian:  C D D# F G A A#

    Phrygian:  C C# D# F G G# A#

    Lydian:  C D E F# G A B

    Mixolydian:  C D E F G A A#

    Aeolian:  C D D# F G G# A#

    Locrian:  C C# D# F F# G# A#

    General Bebop:  C D E F G G# A B

    Harmonic Minor:  C D D# F G G# B

    Melodic Minor:  C D D# F G A B

    Major Pentatonic:  C D E G A

    Minor Pentatonic:  C D# F G A#

    Augmented:  C D# E G G# B

    Blues:  C D# F F# G A#

    Diminished:  C D D# F F# G# A B

    JazzMinor:  C D D# F G A B

    Whole Tone:  C D E F# G# A#

    Bebop:  C C# D# F F# G G# A#

    Minor Bebop:  C D D# E F G A A#

    Arabian:  C D E F F# G# A#

    Balinese:  C C# D# G G#

    Enigmatic:  C C# E F# G# A# B

    Gypsy:  C C# E F G A A#

    Hindu:  C D E F G G# A#

    Hngarian Minor:  C D D# F# G G# B

    Hungarian Major:  C D# E F# G A A#

    Japanese:  C C# F G G#

    Jewish:  C C# E F G G# A#

    Neapolitan Major:  C C# D# F G A B

    Neapolitan Minor:  C C# D# F G G# B

    Oriental:  C C# D# F F# A A#

    Persian:  C C# E F F# G# B

    Spanish 8 Tone:  C C# D# E F F# G# A#

```


Back to Table of Content

50


