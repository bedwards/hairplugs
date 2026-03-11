# Unique

## User Manual



1


#### Content


###### About Basic Structure The User Interface Oscillator section Filter section Controllers Main Controls Arpeggiator section MIX section Effects Master section Preset System Settings Screen Installation Uninstallation Authorization Host integration Native Kontrol Standard NKS Videos Contact



2


### About

Unique is a pretty versatile virtual instrument.

It is a well-crafted emulation of synthesizers from the golden age of analogue keyboard
sounds, delivering a wide spectrum of sound-design options: from dark basses and
strong leads to warm pads.

Unique comes with a state-of-the-art vowel filter. The engine of this filter is the result of
years of development here at Sugar Bytes in Berlin and it’s fair to say that it shaped the
sound and workflow of many high-profile electronic musicians since its release.

Unique also includes two effect sections with Sugar Bytes’ arsenal of signature effects to
pimp your productions.

The sound and the functionality of Unique have been designed together with musicians
and sound designers in order to cover a wide range of sounds and possibilities.
The user interface is simple but powerful. With Unique you will explore a new world of
amazing sounds.

### Basic Structure


On top of the screen, you find the PRESET SYSTEM, you can open the menu to choose a
preset from a certain category or you can simply step through the presets via the < >
buttons.

The Arpeggiator section (top-left) also contains some general settings regarding the MIDI
input.

Right beside is the Oscillator section and the MIX SECTION (mix and panning).

On the bottom there’s the Filter section (left), the Effect section (middle) and the Master
section (right).

The Controllers sections contains 4 freely assignable modulators.

Right beside the Controller section you find the SETTINGS SCREEN which offers additional
settings and functions and a link to the manual.


BACK
TO TABLE OF CONTENT


3


### The User Interface

Unique’s user interface has 5 main elements

Oscillators
Unique’s oscillators (upper third of the GUI) are specially designed to cover a wide
spectrum of sounds: from dark basses and strong leads to very warm pad sounds.
There are 5 generator setups in total:


Saw Tooth
Triple Saw
Pulse
Triple FM
Noise (white-noise generator)

Each oscillator can produce 8 voices in full stereo. The oscillators are anti-aliased for
clearer sound at high frequencies.

Filters
The Filter section (middle on the left side of the GUI) offers 5 filter types:


High Pass (2-Pole)
Band Pass (2-Pole)
Band Pass (4-Pole)
Low Pass (4-Pole)
Comb Filter

Each of these five filter types can also be used in Vowel Mode, where two filters
concentrating on vowels can be used in interaction with each other.
This little miracle engine makes it easy to create humanoid line sensations in your setup.

Controllers
If you tap the red Controllers icon, the upper third of Unique’s GUI will change and show
the four modulators:


LFO
Envelope
Sequencer
Motion (an x/y pad)

Each and every parameter in Unique can be modulated, automated or controlled via
MIDI .

The assignment process is easy and simple. Right click any knob to open the modulation
assignment screen.


4


Effects
Unique comes with a line up of Sugar Bytes’ signature effects.
There are 2 effect sections with a total of 6 effects:


Delay
Reverb
Phaser
LoFi
Filter on effect 1 / Chorus on effect 2

Arpeggiator
Unique has a built-in arpeggiator in the MIDI-IN section in the top-left corner.
The arpeggiator can be applied independently to the oscillator, letting you explore
interesting sounds and melodies. There is an intelligent double voice mode .


BACK
TO TABLE OF CONTENT



5


##### Oscillator section

Unique has two main oscillators with five generator options each.


Sawtooth
Triple Saw
Pulse
Triple FM
Noise

Both oscillators offer typical ADSR parameter:

Attack: adjust the attack time of the amplitude
envelope

Decay: the time after the attack phase until sustain


Sustain: adjust the amplitude level after the decay


Release: adjust the release time of the envelope

The Octave knob (attenuated) sets the rootnote.
The five positions allow for adding/subtracting one or two octaves.

Detune will detune the voices slightly. Usually a good way to add some analogue and
warm impression.

##### Sawtooth


The Sawtooth is the most basic oscillator and
contains the spectral content of all natural
sounds. The anti-aliased algorithm produces a
crystal clear sound even in high frequency ranges.
This oscillator is very efficient regarding CPU
consumption.

##### Triple Saw


Triple Saw uses 3 hard synced Sawtooth
oscillators to produce a very rich frequency
spectrum. Spread, a pitch offset between the 3
oscillators, results in a fatter sound. With this
oscillator you can create string- and organ
sounds, as well as sharp sync leads.



6


##### Pulse Triple FM Noise



The Pulse oscillator can create very dominant
and analogue sounding signals.

Modulate pulse width to get a wide range of
sounds out of this oscillator.

PW: the pulse width of the pulse waveform
PWM RATE: speed of pw modulation (bpm-synced)


Triple FM is based on frequency modulation of three
oscillators. This oscillator provides classic FM sounds,
but also unheard-of and inspiring material, from thin and
piano-like to fat, detuned and distorted.

FM: intensity of internal frequency modulation
SHAPE: amount of the shape algorithm


The Noise oscillator offers an intelligent noise-generator.
It contains a multimode filter that can be linked to the
current pitch. At high resonance values, the noise
oscillator can produce weird sounds close to voices, choir
or monster sounds.

Type: filter type (LP, HP, BP)
Color: adjust the cutoff frequency of internal filter
Reso: resonance of the internal filter
Track: connect voice pitch to filter frequency
In Track mode, the Color control is used to detune the
oscillator.

BACK
TO TABLE OF CONTENT


7


##### Filter section

Unique’s Filter section is an outstanding
creative tool. Its expressive potential should not
be underestimated.

##### The 5 Filter Types


Highpass 2 Pole:

Only frequencies above cutoff are passed. A two-pole has a slope of 12 dB/oct.


Bandpass 2 Pole:

Only signals around cutoff are passed. Fits perfectly into the Vowel Mode.


Bandpass 4 Pole:

The 4-pole BP has a smaller bandwidth than the 2 Pole. Good fit for the vowel
mode. A four-pole has a slope of 24 dB/oct.


Lowpass 4 Pole:

Only frequencies below cutoff are heard.


Comb Filter:

This Filter is based on a feedback algorithm with delay times that correspond to
filter frequencies. In Vowel Mode, this filter mutates to a monster mouth, providing
strong, scary and weird sounds.

##### Standard Filter Controls


These controls are identical across all filter types:

Reso: adjusts the resonance of the filter

Drive: adds overdrive to the filter

Mix: mixes the dry with the filtered signal


BACK
TO TABLE OF CONTENT


8


##### Modulation of Filter Parameters

There are five modulation sources:


Envelope
LFO
Four Step
Pitchbend
Modwheel


Envelope


In this mode there is an ADSR envelope,
which modulates the cutoff frequency.


Cutoff and Peak
Use the cutoff and peak knobs to set the start and end of envelope modulation.

During the attack phase, the cutoff frequency moves from its starting point to the
defined peak frequency. In the release phase, the cutoff will move from the peak back to
the cutoff frequency.


Trigger
Trigger determines on which particular event the envelope is restarted.


Each: each new note retriggers

Lowest: triggers, if a note played is lower than the notes played before
(in Legato only)

Loudest: will only retrigger if a note played has a higher velocity than before

First: triggers on the first note played

Arp: the arpeggiator’s tempo sets the trigger interval


BACK
TO TABLE OF CONTENT

9


LFO


LFO lets you modulate between 2 filter
frequencies or 2 vowels in Vowel Mode.

Like with the envelope you select a start
frequency (Cutoff) and a destination frequency
(Peak).

Rate: the frequency rate of the LFO (synced to the host BPM)

Fade: fades in the LFO rate

Fade In: time until the full LFO amount is reached

Note : The LFO has one more retrigger option than the envelope. This is the Clock Start
trigger mode. In this mode the LFO is retriggered when you hit play in your host.


4 Step


4 Step lets you setup 4 different
frequencies (or vowels) to be played in
series.

These steps can be played back at a
defined speed and different directions .

Tempo: the playback speed of the 4-Step sequencer


Glide: time to fade from one step to the next


C1-C4/V1-V4: frequency/vowel values of the steps


Forward mode
Backward mode
Ping-Pong
Inverse Ping-Pong
Random

Note that these directions modes are also used in the modulation sequencer and
arpeggiator section described later.

BACK
TO TABLE OF CONTENT

10


Pitchbend


Morph between two frequencies with the
Pitchwheel.

These 2 frequencies are once again
defined by the Cutoff and the Peak
parameter.

With the Slope parameter you can define the fading curve.
If the parameter is in middle position you have a linear fading between the frequencies.

A higher Slope value results in a larger controlling range for the Cutoff parameter while a
lower value does the opposite.


Modwheel


The Modwheel mode works in the same
way as the Pitchbend mode, except that it
assigns the MIDI modulation wheel to fade
between 2 frequencies (or vowels).


Vowel mode


The Vowel Mode emulates the human mouth,
opening possibilities that you know from a talk
box or a vocoder.

Beside the classic vocals A-E-I-O-U we also
added mutated vowels like AE and German
Umlauts.

The vowel mode is the main feature of Unique and the result of years of hard work at
Sugar Bytes. It offers new sound dimensions. When the vowel mode is powered on,
the cutoff parameters are changing to vowel parameters.

You can use a vowel parameter in the same way as the cutoff knob, just click and drag to
select different vowels.


BACK
TO TABLE OF CONTENT


11


##### Controllers

This section gives you access to the control panel for 4 powerful modulators:


LFO
Envelope
Sequencer
Motion Pad (x + y axis)


To assign them to a parameter, just right click the destination parameter and choose
from the available modulators.


BACK
TO TABLE OF CONTENT



12


##### LFO

The LFO Modulator has a BPM synced Rate
parameter. This Rate can be faded in, using
the Fade Rate knob.

The classic LFO waveforms (sine, saw,
square, tri) can be morphed using the Wave
parameter. Just click and drag the Wave
view.

You also can fade in the LFO intensity by using the Fade parameter.


Trigger:
trigger determines on which particular event the envelope is restarted

Each: each new note retriggers


Lowest: triggers, if a note played is lower than the notes played before (in Legato only)


Loudest: will only retrigger if a note played has a higher velocity than before


First: triggers on the first note played


Arp: the arpeggiator’s tempo sets the trigger interval

Via the Range parameter you can adjust the minimum and the maximum value of the
LFO.

##### Envelope


A classic ADSR envelope.

Use Range to limit min/max amount.


BACK
TO TABLE OF CONTENT



13


##### Sequencer

Eight steps to create individual modulation sequences.

The speed can be adjusted by the Tempo (synced to your
host BPM).

Glide defines a fading time between the steps to smooth
step transitions.

The sequencer features different Direction modes:


Direction Modes


Forward mode
Backward mode
Ping-Pong
Inverse Ping-Pong
Random


And finally the Range parameter for calibrating the working range.

##### Motion


Use the Motion Pad with your finger to record movements.
Each modulation target can then read out the current x
and the y value.
To do so, just turn on Record and click and move the red
circle. With the Smooth parameter you can smooth the
movements.

Again there are the different Trigger modes for restarting
the motion. (See Filter/Envelope/Trigger)
Trigger determines on which particular event the envelope
is restarted.

Each: each new note retriggers
Lowest: triggers, if a note played is lower than the notes played before (in Legato only)
Loudest: will only retrigger if a note played has a higher velocity than before
First: triggers on the first note played
Arp: the arpeggiator’s tempo sets the trigger interval


BACK
TO TABLE OF CONTENT

14


##### Pitch and Modwheel

Assign a Pitch LFO to the MIDI modulation wheel (CC 1).

Just click the LFO button in the Settings Screen of Unique and adjust the Speed of the
LFO.

There you can also define the pitchbend range of the MIDI - pitchbend wheel.


BACK
TO TABLE OF CONTENT


15


##### Main Controls

The main controls in Unique are knobs. Just click them and drag up or down to turn
them. While moving them, a display appears showing the value and unit of the
parameter.


The knobs have different colors, which reflect certain functionalities.

White: are modulation-related parameters
Red: are midi-related parameters
Blue: are general sound design parameters
Yellow: are amplification parameters


All knobs can be modulated with internal modulators or controlled by MIDI or Host
Automation. Just right click on a parameter and a menu with certain modulation sources
comes up. The first 5 entries assign a modulator to the knob you just clicked on.

The entry ‘ MIDI LEARN ’ puts the knob into MIDI learn mode. Then the next MIDI-CC
message you send to Unique will control this knob.

To clear any assignment, just hit the entry ‘CLEAR’ .

Note: If you assigned a knob to a modulator or to a MIDI-CC you should not use Host
Automation for this knob. Otherwise the parameter will receive multiple values at the
same time, which might cause unpredictable behaviors.


BACK
TO TABLE OF CONTENT


16


##### Arpeggiator Section

In this section you can control how your incoming MIDI signals
are processed (see MIDI IN indicator).

In the right upper corner is a menu to switch between Poly and
Unison. Poly is a classic 8-voice polyphonic mode. Unison turns
Unique into a monophonic synthesizer with 8 voices playing
simultaneously.

Spread adjusts a pitch offset of the eight voices.

Glide sets the time to move from the previous note pitch to the currently pressed note
pitch. In Poly mode, Unique offers a polyphonic glide, where a glide happens from the last
voice to all new voices.

The Arpeggiator can be turned on independently for each
oscillator with the OSC1 and OSC2 buttons. Tapping the ARP
button will open the arpeggiator’s menu.

The arpeggiator has 5 playing Styles. Up, Down, Up and Down,
Down and Up and Random.

Tempo sets the speed of the arpeggio (synced to your host).

Arp Trigger Settings:


ClockStart: Clock triggers Arp

Each Note: new note played retriggers Arp

First Note: Arp starts on first note pressed

Lowest: if a note sets a new low – triggers arp (Legato)

Highest: if a note sets a new high – triggers arp (Legato)


BACK
TO TABLE OF CONTENT


17


##### MIX section

Right between the two oscillators is Unique’s Mix
section. Here you can adjust level and pan for each
oscillator.

Top left and top right you find the Poly Buttons, which
decide if the panning is handled monophonic or
polyphonic. In Single mode, the pan is monophonic,
like you know it from a classical pan control. In Poly
mode, each voice has its own position in the stereo
field.

Pan defines the width of the stereo effect for each oscillator.

Level controls volume for each oscillator.

Autopan: LFO-controlled Panning
There’s an individual auto-pan for each oscillator. Also the auto- pan can work
monophonic or polyphonic, like the Pan control mentioned above. So in polyphonic
mode, each voice will be auto-panned individually. If you play 2 oscillators with 8 voices
using auto-pan, you can have 16 sounds moving around in the stereo field.

Rate sets the frequency of the LFO controlling auto-pan.


BACK
TO TABLE OF CONTENT


18


##### Effects



Two multieffect units running in series.

Each unit contains 5 effects. They basically
offer the same effects with the exception
that Effect 1 offers a Filter where Effect 2
has a Chorus instead.

##### Delay


Time: adjusts delay time (synced to Host-BPM)

Feedback: intensity of internal feedback

Cutoff: controls the cutoff of the built in low-pass filter

Reso: controls the resonance of the built in filter

Mix: controls the dry/wet mix of the signal

##### Reverb


Room: size of the reverberation room

Damp: adjust damping properties of the room

Width: controls the stereo widening

Hipass: controls the cutoff of the internal hi-pass filter

Mix: controls the dry/wet mix of the signal

##### Phaser


Rate: phasing speed synced to host-BPM

Feedback: internal feedback level

Width: controls the stereo widening

Stages: number of stacked phasing stages

Mix: controls the dry/wet mix of the signal


19


##### Lofi

Crush: bit-crushing intensity

S-Rate: amount of sample-rate reduction

Mix: controls the dry/wet mix of the signal

##### Filter


Cutoff: the filter cutoff frequency

Reso: resonance of the filter

Type: 5 filter-types (LP, LPBP, BP, BPHP, HP)

Mix: controls the dry/wet mix of the signal

##### Chorus


Rate: chorus speed synced to host-BPM

Feedback: internal feedback level

Depth: intensity of the chorus

Width: controls the stereo widening

Mix: controls the dry/wet mix of the signal


BACK
TO TABLE OF CONTENT



20


##### Master section

The master section gives you all tools to finally shape the sound.


Of course there is the Master volume control to adjust
the overall volume.

A special feature of the Master Section is the Sub
Oscillator, which uses a Sine waveform.

It is connected with Oscillator 1, so it uses the ampenvelope and the arpeggiator assignment of Oscillator 1.

The Sub- Osc parameter adjusts its volume. The sub oscillator is very handy if you want to
add bass to your sound, but also if you want to add another sound dimension on top.
Define its pitch octave via the Oct knob.

The Master section also contains a Tremolo effect which modulates the final volume with
an internal LFO.

Tremolo controls its intensity, the Rate defines the speed (BPM-synced) and the Fade
parameter defines a fade in time for the tremolo. Note that the tremolo fade time is
triggered by the first note you press.


BACK
TO TABLE OF CONTENT


21


##### Preset System

Unique’s presets are accessible via the preset menu in the top area of the interface.

You can easily step through the presets with the arrow buttons on the left and right side.
When the preset name is clicked from the top area of Unique, a menu will come up
showing all preset categories.

A special folder is the User folder . This folder is empty and is meant to store the presets
you created.

The little disc icon opens the ‘Save Preset’ entry and is for saving presets. It should
automatically save the preset into the User folder.


BACK
TO TABLE OF CONTENT


22


##### Settings Screen

In the settings screen you find some global settings and functions.


Pitch LFO

Here you can define the amount of pitch modulation caused by the Pitch LFO in the
Modwheel section and adjust the Speed of the LFO.


Pitch Bend
The Range parameter defines the pitchbend range of the MIDI - pitchbend wheel.


Global


Velocity
Adjusts the velocity behavior of your incoming MIDI notes.


Glide On First Note
When activated Glide will work on the first note.


Tune
With the Global Tune parameter you can change the overall tuning of Unique in order to
adapt it to other sound sources.


MIDI


CC Recall Lock
When active MIDI Learn Settings will be kept and not be changed when selecting a
different preset.


BACK
TO TABLE OF CONTENT


23


### Installation

[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)
Double-click on the installer and follow exactly the instructions provided by the
installation process.

The standalone version and manual will be installed to:
Windows: C:\Program Files\Sugar Bytes\Unique
macOS: /Applications/Sugar Bytes/Unique

Presets will be installed into Documents\Sugar Bytes\Unique.
Important: Do not relocate Unique presets after installation!


WINDOWS
Default installation paths:
VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins


macOS

Default installation paths:
VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins


BACK
TO TABLE OF CONTENT



24


### Uninstallation

To uninstall Unique, please follow the instructions:


Windows
Uninstall Unique under Control Panel>Add/Remove Software.


macOS
Delete all the following files and folders:

/Applications/Sugar Bytes/Unique
/Library/Audio/Plug-Ins/VST/Unique.vst
/Library/Audio/Plug-Ins/VST3/Unique.vst3
/Library/Audio/Plug-Ins/Components/Unique.component
/Library/Application Support/Avid/Audio/Plug-Ins/Unique.aaxplugin

~/Documents/Sugar Bytes/Unique
~/Library/Preferences/com.sugar-bytes.Unique.plist

/Library/Application Support/Sugar Bytes/Unique
/Library/Application Support/Native Instruments/Service Center/Unique.xml
/Library/Preferences/com.native-instruments.Unique.plist

‚~‘ means: /Users/YOURLOGINNAME (your home folder)
(Please note that in macOS 10.7 and later, the user Library folder is hidden. In case you
cannot locate your Library folder in the Finder: Select „Go to Folder“ from the Finder‘s Go
menu and enter ‚~/Library‘.)

### Authorization

The serial number is requested during installation. If the serial number is missing or
incorrect, the product will not produce any sound. Check the the top area of the Unique
interface to verify whether your serial number is VALID. Manually entering the correct
serial number there or performing a quick reinstall, should fix any issues.


License
License covers both the macOS and Windows version and can be activated for two
computers. For use on more than two computers, please buy an additional license.


BACK
TO TABLE OF CONTENT


25


### Host integration

Unique works as a VST2 / VST3/ AU / AAX plugin in the most commen DAW hosts.
Make sure that Unique is installed in the Plugins folder used by your DAW.
Some hosts need to perform a plugin rescan when a newly installed plugin is launched
for the first time. Please find all detailed instructions for your DAW below.

##### Cubase

Perform a full rescan in the Cubase plugin manager.
Make sure that the Unique.dll/Unique.vst3 (Win) or Unique.vst/Unique.vst3 (macOS)file
is contained in Cubase‘s assigned VST Plugins folder. Load Unique as Instrument into an
Instrument track.

##### Ableton Live

When using macOS, we recommend using the VST version of Unique in Live.
Please note: With Ableton Live, plugins sometimes will be marked as unloadable and not
rescanned automatically. If this happens to be the case, force a rescan by unchecking
and checking the ‚Use custom VST Folder‘ checkbox in Preferences/File Folder/Plug-In
Sources. Set up a MIDI track and insert Unique as instrument.

##### ProTools

When installing Unique, select AAX plug-in format.
(AAX is supported by Pro Tools 10.3.5 and higher.)
Use Unique as an instrument.

##### Studio One

Go to the Studio One menu and choose Options. Click Locations, then VST Plug-Ins.
Click the Add... button and select your VST Plugins folder. Press OK.
Create an instrument track and pick Unique up from the Instrument list.

##### Sonar

Make sure that Unique is installed in the VST Plugins folder used by Sonar.
Insert Unique as a „soft synth“.

##### Logic

Select Unique as an AU-Instrument from the I/O dialogue of a Software Instrument track.

##### FL Studio

Go to Channels>Add one>More...There you should find Unique and perform a refresh. You
can now open Unique in the Mixer Inserts.


BACK
TO TABLE OF CONTENT


26


### Native Kontrol Standard NKS

Unique supports Native’s NKS standard, giving you the same deep integration with NI
controllers like Komplete Instruments.
The main features are a plug-and-play support of Unique‘s preset browser and troublefree tagging/organisation for inclusion in the powerful Komplete Kontrol / Maschine
browser. This lets you search the presets by sound type (e.g. synth lead), character (e.g.
dark), or any combination thereof. We have strived for highly profound control of
Unique‘s sound engine. Knobs and faders can be mapped to match those on the Kontrol
and Maschine hardware in logical ways, with similar controls grouped by pages.
For example: Skip to the Filter page and you will find the set of controls related to the
filter characteristics. All presets have been wrapped into .nksf files which contain preset
and tagging information as well as mapped out controls. Different genre and mood
categories will speed up the producers’ workflow when browsing
through libraries, and help you keep your eyes off the computer screen.

##### Controller Mapping

We have strived for highly profound control of Unique‘s sound engine.
All mappings are consistent throughout the different presets.
There are seven pages available:

Page 1: Master
Features the level and pan controls as well as the sub level and drive parameter.

Page 2 and 3: Osc1/Osc2 + Env1/Env2
Here you will find the controls of Unique‘s Osc 1 and Osc2.
Octave, Detune and the Osc’s related envelope controls. Depending on the oscillator
model selected, you will find the knobs of the Osc mirrored in NI Maschine, e.g.:
Pulse: PW and PWM Rate.
Triple FM: FM and Shape and so on.

Page 4 and 5: FX1 + FX2
These two pages feature the controls for Unique‘s effects slots.
Depending on the effect type selected, you will find the corresponding effect parameters
(e.g. Rate, Feedback, Depth and Width for „Chorus“).
The Mix parameter is provided with every effect type.

Page 6: Filter + ENV
Here are the controls of Unique‘s filter section.
The Resonance and Mix parameter are provided with every filter type.
Depending on the modulation source selected and on if Vowel mode is active or inactive,
we have the knobs e.g.: Vowel1, Vowel2 and the envelope controls for Vowel with
Envelope as modulation souce.

Page 7: Modulation
This page contains all important controls for easy sound modulation like
Unique‘s Spread, Glide, Tremolo (and its Rate parameters) as well as the LFO-controlled
Panning controls (Autopan).

27


### Videos

Here are some links to youtube videos with short tutorials on Unique.
They are using the old GUI version so the GUI design is different and the layout differs
here and there, but they are very useful understanding some concepts.


[OVERVIEW 01:34](https://www.youtube.com/watch?v=LsVp4TS1o4A) (NO VOICEOVER)

[MAKING MINIMAL PADS 10:01](https://www.youtube.com/watch?v=4EDNN8iR8DI) (DAN-D, PART 1)

MODULATION & [CONTROLLERS 06:58](https://www.youtube.com/watch?v=c4loYb3Zu5g) (DAN-D, PART 2)

A [70'S BASS 05:15](https://www.youtube.com/watch?v=QNTeSX8eO0M)

DEMO 03:09 [- HAVE A LOOK AT THIS TO SEE HOW MUCH FUN UNIQUE IS](https://www.youtube.com/watch?v=wwiwOxFLjhE)

### Contact

Sugar Bytes GmbH | Made of passion
Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395
[info@sugar-bytes.de](mailto:info@sugar-bytes.de)
[www.sugar-bytes.com](http://www.sugar-bytes.com/)


BACK
TO TABLE OF CONTENT



28


