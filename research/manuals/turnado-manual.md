# Turnado

## Manual


### Contents

#### WHAT IS TURNADO 5 INSTALLATION AND AUTHORIZATION 5 Installation 5

WINDOWS 6
macOS 6

#### Uninstalling 7 Authorization 7 HOST INTEGRATION 8

Cubase 8
Sonar 8
Live 9
Logic 9
Pro Tools 10
Studio One 10
Native Kontrol Standard NKS 11

#### MAIN PAGE 12 Overview 12 About Screen 12 Settings 13 Effect Browser 14 Effect Slots 14 Main Knob 14 EDIT PAGE 15 Edit Page Sections 15

Main Controller Overview 15
Effect Name/Menu 15
Effect Preset 16
Key Sync 16
Close 16
Effect Parameters 16


2


Dry/Wet 16
Amount Controller 17
Main Controller 17

#### MODULATORS 18 LFO Function Panels 18

Waveforms 18
One-shot/Loop/Host Sync 18
Time Factor 18
Quantise 18

#### Main Parameters of the Modulators 19

LFO 19
Rate 19
Phase 19
Amount 19
Envelope Follower 20
Attack 20
Release 20

#### DICTATOR 21 THE EFFECTS 22 Delays 22

Pattern Delay 22
Reverse Delay 22
Pitch Delay 22

#### Modulation Effects 23

Flanger 23
Phaser 23
Tonalizer 23

#### Reverbs 24

Reverb 24
Freezeverb 24

#### Transformation Effects 25

Ringmodulator 25
Vocodizer 25

#### Amplifier 26

Levelizer 26
Guitar Amp 26

#### Loop Effects 27


3


Looper 27
Pitch Looper 27
Pan Looper 27
Reactor 27
Slice Arranger 28

#### DJ Tools 29

Granulizer 29
Stutter 29
Vinylizer 29

#### Filters 30

Filter 30
Filter Pattern 30
Vowel Filter 31
Spectralizer 31

#### MIDI PROGRAM CHANGE 32 FAQ 33 Silence 33 Noise 33 Licence 33 Compatibility / Returns Policy 33 CONTACT 33


4


### What is Turnado

Turnado is a new multi-effect tool for real-time beat and audio manipulation. With 24
new effect algorithms and a completely new, one-knob approach to working with Effects.

Turn the Knob ...The effect is on.

Turn the Knob further ...The effect parameters are being modified.

Turn the Knob back ...The effect is off.

### Installation and Authorization

#### Installation


Download (requires login) the latest version [here](http://www.sugar-bytes.de/account) .

The standalone version and the manual will be installed into
Windows: C:\Program Files\Sugar Bytes\Turnado
macOS: /Applications/Sugar Bytes/Turnado

Presets will be installed into Documents\Sugar Bytes\Turnado.

Do not move the Turnado presets after installation!


Back To Table of Content


5


##### WINDOWS

Default installation paths:

VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins

##### macOS


The Audio Unit, the VST plug-in and the AAX plug-in will be automatically installed into
the correct folders.

Default installation paths:

VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins


Back To Table of Content


6


#### Uninstalling

In order to uninstall Turnado, please take the following steps:

Windows: Uninstall Turnado under Control Panel/AddRemove Software.

macOS: Here is the way to delete everything regarding Turnado

/Applications/Sugar Bytes/Turnado
/Library/Audio/Plug-Ins/VST/Turnado.vst
/Library/Audio/Plug-Ins/VST3/Turnado.vst3
/Library/Audio/Plug-Ins/Components/Turnado.component
/Library/Application Support/Avid/Audio/Plug-Ins/Turnado.aaxplugin

~/Documents/Sugar Bytes/Turnado
~/Library/Preferences/com.sugar-bytes.Turnado.plist

‚~‘ means: /Users/YOURLOGINNAME (your home folder)
(Please note that in macOS 10.7 and later, the user Library folder is hidden. In case you cannot
locate your Library folder in the Finder: Select „Go to Folder“ from the Finder‘s Go menu and
enter ‚~/Library‘.)

NKS:
/Library/Application Support/Native Instruments/Service Center/Turnado.xml
/Library/Application Support/Sugar Bytes/Turnado/
/Library/Preferences/com.native-instruments.Turnado.plist

#### Authorization


The serial number is requested during installation. If the serial number is missing or
incorrect, the product will not produce any sound. Check the About Screen of the
Turnado to verify whether your serial number is VALID. Manually entering the correct
serial number there or performing a quick reinstall, should fix any issues.

One license covers both the macOS and Windows version and can be activated for two
computers at the same time. For use on more than two computers, please buy an
additional license.


Back To Table of Content


7


### Host Integration

#### Cubase Sonar



Load Turnado as an insert effect on an audio
track or instrument track.
Now create a MIDI track and choose Turnado as
target for the MIDI track.
Now you can trigger Turnado with your MIDI
knobs and record controller movements in the
MIDI track.



Plug in Turnado as an insert effect. Then enter the plug-in Settings and check the
"Configure As Synth" option. Then plug Turnado out and plug it in again.


Create a MIDI track and choose Turnado as target
for the MIDI track.
Now you can trigger Turnado with your MIDI
knobs and record controller movements
in the MIDI track.


8


#### Live Logic



Use Turnado as Insert Effect on any track.
Now create a MIDI track and send the MIDI
signal to the audio track with Turnado loaded.

You can now control Turnado with your hardware knobs, sending
MIDI to the MIDI track, or using MIDI clips.



Use Turnado as an insert effect.
In order to control it with MIDI, create an Instrument track and use the Turnado "MIDI
controlled FX".
Then, in the Sidechain menu in the upper right corner, select the Audio track or Bus that
you want to use with Turnado. Then, in the Logic mixer, turn down the level of the audio
track that you selected in the Turnado sidechain menu.


9


#### Pro Tools

Use Turnado as an insert effect.
In order to control it with MIDI, create a MIDI track and choose Turnado as Output in the
I/O Menu of the Mixer.

#### Studio One


Go to the Studio One menu and choose Options, click on Locations, then VST Plug-Ins.


Click the Add button and select your
VST Plug-in folder. Press OK then close
and re-open Studio One. If you still
don’t see your plug-in, go back into
that screen and click the “reset
blacklist” button, then close and open
Studio One again.

Pick it up from the VST Effects list. Create an instrument track and choose Turnado as
MIDI out target for that track.


Back To Table of Content


10


#### Native Kontrol Standard NKS

Turnado supports Native’s NKS standard, providing an easy integration with Komplete
Kontrol and Maschine. All presets have been wrapped into .nksfx files which contain
preset and tagging information as well as mapped out controls.
The main feature is an easy way to access Turnado’s presets via the powerful Komplete
Kontrol / Maschine browser. This lets you search the presets by various tags and
categories. Different types and modes will speed up the producers workflow while
browsing through libraries, and help you keep your eyes off the computer screen.
You also have quick access to Turnado’s main controls via the NKS assignment pages.

##### Controller Mapping

All mappings are consistent throughout the different presets.
There are two pages available:

Page 1: Eight Main Knobs
Features the 8 controls which correspond to the 8 Effect Slots.

Page 2: Dry/Wet
Here you will find the global Dry/Wet control of Turnado.

##### Komplete Kontrol / Maschine can’t find Turnado?

The installer will ask you for the VST plug-ins folder.
There make sure you set the VST plug-ins folder that Komplete Kontrol / Maschine is
using or make sure that in Komplete Kontrol / Maschine the correct folder is selected
under Preferences->Plug-ins->Locations.

If the Turnado.vst (macOS) or Turnado.dll (Win) is present please make a rescan under
Preferences->Plug-ins->Locations->Rescan

After that go to File -> Preferences -> Library -> click the Factory Paths tab and make a
rescan.

On Windows, be sure to install the correct version (32bit or 64bit).
You can check if Komplete Kontrol / Maschine is running in 64bit or 32bit when you click
Help-> About in the Komplete Kontrol / Maschine file menu.


Back To Table of Content


11


### Main Page

The Main Page of Turnado is divided in three sections.

#### Overview


Here you can chose a global preset, sequentially using the arrow tabs, or from a dropdown menu accessed by clicking on the Preset Name Display. Click on the grey buttons
to access the Settings or Dictator window. Click on the Turnado or Sugar Bytes logo to
open the About Screen.

Below the preset menu you find the Global DRY WET control to set the
Overall Dry/Wet Mix of Turnado.

To reverse or to recover changes use the Undo/Redo Buttons.

Above is a randomize button, which randomizes all effects.

#### About Screen


The About Screen displays the version number and
names of contributors. Your serial number is shown in
the top left, along with its validation status.

Just click on the little book for quick access to this
manual.


Back To Table of Content


12


#### Settings

Default settings can be made to adjust the way Turnado operates in certain situations.
Every adjustment can be made Per Preset or applied generally.

The available settings are:




- Dynamic Displays: The displays of the parameters show Real-time values.

- CC Recall Lock: MIDI Learn Settings will be kept and not be changed when



selecting a different preset.

- Dynamic Signal Flow: When checked, the last activated effect lies in front of the



previously activated effect in the signal chain. Otherwise the signal flow follows
the sequence of the respective effect slots.

- Ignore Program Change: Incoming program changes will not change effects.

- Reset After Load: The Main Knobs will be set to zero when a preset is loaded.

- FX Off at Knob Full On: The effect will be deactivated at zero and full rotation of



the Main Knob

- Activation Threshold: Determines the position at which the Main Knob triggers the



effect.

- Activate MIDI Out: Sends the position of the 8 main knobs as CC data. The knobs

are mapped to CC 1-8.

- Turn Off Knobs on Host Stop: When stopping your host, all effects are turned off



in Turnado.

- Keep Bypass State: The Bypass State will be changed or not when loading



another preset.



Back To Table of Content


13


#### Effect Browser Effect Slots



There are 24 effects in the effect browser. You can drag and drop
them into any of the 8 available Effect Slots. The effects groups are
labelled with colours for easy differentiation.

Be aware that some effects sample the audio signal and then
interchange it for the original signal. For example, Looper or Slice
Arranger turned on before audio was played can lead to unexpected
silence.



Each of the 8 Effect Slots has a Preset Menu for the chosen effect type. To adjust
parameters and performance control of the current effect there is a separate Edit Page,
which can be opened using the Edit button

#### Main Knob


Each Effect Slot has a corresponding Main Knob. This is used to turn
the effect on or off and adjust the assigned Effect Parameters. The
standard MIDI allocation is CC1 to CC8 and the 0 to 127 scale
corresponds to the MIDI specification. Each Main Knob bears a
number corresponding to the Effect Slot number, when illuminated
this number indicates that the effect is active.

Use the little lamp beside the Main Knob to bypass the effect.


Back To Table of Content


14


### Edit Page

The Main Controller, in the centre, is simply the Edit Page representation of the
corresponding Main Knob on the Main Page. The Main Controller shows the position and
activity of the Main Knob. Coloured circuits help to illustrate possible routing options
between Effect Parameters, Modulators and the Main Controller.

#### Edit Page Sections

##### Main Controller Overview

In the top left is a set of Mini Controllers, one for each of the eight effects. It is intended to
give an overview of the Main Knob positions and quick access to the other Effect Slot’s
Edit Pages. By clicking on one of the eight controllers you can jump to the corresponding
Edit Page. Moreover, the eight Main Knobs can be controlled here. This enables you to
quickly test different combinations of effects, by turning each effect on or off without
leaving the Edit Page. The controller of an active effect is illuminated in green and the
currently edited effect is illuminated red.

##### Effect Name/Menu

Right of the Main Controller Overview is the Effect Name. This drop-down menu enables
you to choose other effects for a particular slot right from the Edit Page.

Back To Table of Content


15


##### Effect Preset

Here you can chose a preset, sequentially using the arrow tabs, or from a drop-down
menu accessed by clicking on the Preset Name Display. With the Save function, you can
also save your own presets and modifications.

##### Key Sync

The Key Sync enables you to quantise Turnado effects to the beat. When set to “Off”
then the effect will activate as soon as you turn it on. If it is set to “¼” bar, then the effect
will activate at the beginning of the next beat regardless of when you turn the effect on.

##### Close

Click the close button in the top right corner to quit the Edit Page and return to the Main
Page.

##### Effect Parameters

The Effect Parameters of the chosen effect can be adjusted using the five red controllers
in the top half of the Edit Page. The red display to the right of each Effect Parameter
shows the current value, while the green display, when present, is a drop-down options
menu for that Effects Parameter.

##### Dry/Wet

All effects have the same Dry/Wet Effect Parameter. The five different modes give you
greater control over how Turnado works within the mix.
Equal: The cross-fade is shaped according to the “Equal Power Law”, which leads to
some signal attenuation at a 50/50 mix.
X-Fade: Source audio and effect signal are being mixed using a linear transformation.
Dry: The original signal is being mixed into the effect signal.
Wet : The effect signal is being mixed into the original signal.
Wet Only: Only the effect signal is audible and the Dry/Wet Effect Parameter becomes a
volume controller. This setting is particularly useful when using Turnado as a send effect.

##### Gain

The Gain fader lets you adjust the volume of the effected signal.


Back To Table of Content


16


##### Amount Controller

The Amount Controller, located underneath each parameter
controller, determines the influence of the Main Controller on
that parameter. Double clicking on any controller will return it
to centre, in this position nothing happens. If the Amount
Controller is turned anti-clockwise, then the Main Controller
has a subtractive relationship to the Effect Parameter. When
the Amount Controller is turned clockwise, then the Main
Controller has an additive relationship to the Effect Parameter.

In the middle of the Amount Controller is a waveform
illustrating the transformation curve, which the modulated
parameter will follow, in response to movement of the Main Controller. Underneath the
Amount Controller is a drop-down menu for choosing transformation curves. These
curves offer a range of transformation patterns allowing modulation to occur at a later
point in time, stop intermittently, follow steps, or follow logarithmic and exponential
curves.

On the right hand side of the Amount Controllers are the Modulator Allocation Switches.
When the Modulator Allocation Switches are in centre position, the Modulators have no
influence on the Effect Parameters. In position “+“ the modulator has an additive
relationship to the Effect Parameter. In the “–“ position the modulator has a subtractive
relationship to the Effect Parameter. The intensity of the Modulators is adjusted with the
Amount controller in the respective Modulator.

The parameter range, and therefore expected intensity of the modulation, is shown in
the middle of the Effect Parameter controller itself. The white band illustrates the defined
range of the modulation. The red indicator arm shows the real-time value, as well as the
influence of the Modulators and the Main Controller.

##### Main Controller

The Main Controller in the centre of the page is simply the Edit Page representation of
the corresponding Main Knob on the Main Page. The Main Controller shows the position,
and activity, of the Main Knob. It is useful for testing the current effect settings, as well as
keeping track of the current Main Controller position when using a MIDI control device.


Back To Table of Content


17


### Modulators

Turnado has three independent Modulators. There are two LFO’s, which can be used as
Step Sequencers or Envelope Generators. Between the LFO’s is an Envelope Follower,
which generates an envelope from the incoming audio signal. The Modulators can be
assigned to any Effect Parameter and can have an additive or subtractive influence on
the parameter value. You do not have to choose between the Modulators, all three
Modulators can be used on each Parameter at the same time.

#### LFO Function Panels


To the left and right of the Main Controller are the
LFO Function Panels for the two LFO’s. Here, LFO
curves or the Step Sequencer can be chosen and
edited by clicking/dragging values directly on the
panel itself.

##### Waveforms

In this menu the LFO Waveforms are selected. The Step Sequencer is at the bottom of
this list and can be edited directly on the LFO Function Panel.

##### One-shot/Loop/Host Sync

Here you can choose whether the LFO/Step Sequencer triggers only once or loops
continuously. When Host Sync is selected the LFO will run synced to the host clock.

##### Time Factor

Here you can choose between the three Time Factors; Sync (LFO Rate synchronized to
the beat), Hz (LFO Rate in Hz) and Triplet Sync (LFO Rate in synchronized to the beat in
triplet and dotted patterns).

##### Quantise

This setting defines the number of steps in the LFO Waveform and Step Sequencer data.
When Quantise is “Off” the LFO Waveform and Step Sequencer will allow the full data
range to be used. Changing the Quantise to “2” will reduce the data range to two values,
maximum and minimum. Increasing the Quantise value further increases the number of
data points between maximum and minimum, from “3” to “12”.


Back To Table of Content


18


#### Main Parameters of the Modulators

Each of the Modulators has three Main Modulator Parameters. The Main Controller can
influence the Main Modulator Parameters in the same way as Effect Parameters. There
are separate Amount Controllers for each of the Main Modulator Parameters, allowing
you to define the range of modulation and select different transformation curves.

##### LFO

The LFO (Low Frequency Oscillator) generates
modulation with a continuously repeated waveform.
In addition, the Turnado LFO offers a Step Sequencer,
which is also capable of triggering a sequence only
once, enabling you to generate many different types of
envelopes. The Main Controller also activates the LFO.

##### Rate

The LFO Rate determines the frequency of the LFO, or the speed of the Step Sequencer
pattern. Note that with the 1.5 update you have a rate multiplier in the waveform view,
which allows you to multiply the selected rate up to 8 times. This allows ultra slow
movements.

##### Phase

Here, the starting point within the LFO Waveform and the Step Sequencer is chosen.

##### Amount

Determines the intensity of the modulation being sent. Whether the modulation affects
the end Parameter in an additive or subtractive way, is determined with the “+” and “-”
buttons of the respective Effect Parameter.


Back To Table of Content


19


##### Envelope Follower

The Envelope Follower generates an envelope from the
source audio signal. This Modulator is very dependent
on the dynamics of the incoming signal. Whilst strong
beats create obvious modulations, signals without
significant dynamics will create more subtle
modulation.

##### Attack

Determines the lead-in time of the Envelope Curve. The shorter the lead-in time the
faster the reaction to the audio dynamics. While a longer lead-in time gives a slower
reaction it can also massively reduce the effect of the Envelope Follower.

##### Release

Determines the decay time of the envelope. Short decay times enable the Envelope
Follower to react quickly to the audio signal whereas long decay times create a more
sustained modulation.


Back To Table of Content


20


### Dictator

The powerful Dictator mode enables you to create an automation sequence for the 8
Main Knobs and assign the entire sequence to one fader.


The Dictator window shows eight vertical tracks,
which correspond to the 8 Effect. On the left is a
fader that enables you to move through the
sequence of Main Knob automations. To create
automation for one of the Main Knobs, simply click
on the vertical track corresponding to the effect you
want. A coloured bar will appear with a shadow, this
is an Automation Point. The intensity of the shadow’s
colour indicates the value of the Main knob at this
position. Holding the mouse button, and dragging up
or down, creates/selects an automation point and
moves it. Load the “HalfwayUp” Preset from the
Preset Menu at the top of the Dictator window.
Moving the Dictator fader up and down while
watching the Main Knobs will give you a good
indication of how the Dictator works.

Alternatively you can just put the Dictator fader at a
certain position, then move the Main knobs as you
want them to be at that Dictator position. This only
works if the Dictator window is open and the Lock
button is inactive.

Some of the key functions are:


  - Automation Points can be created and moved directly with the left mouse


  - Automation Points can be created and altered by moving one of the Main knobs


  - Right click to delete Automation Points


  - Shift click and move the mouse to alter the Main Knob value for the Automation Point


  - The Dice Buttons allow for random generation of automations for all or individual tracks


  - The X Buttons delete all or single tracks


  - The Lock Button inhibits the creation/modification of Automation Points by moving a
Main knob


  - The Preset Menu enables you to load and save Dictator Presets


Back To Table of Content


21


### The Effects

#### Delays

##### Pattern Delay

The Pattern Delay has 8 delay lines and offers a number of predefined Patterns, each with different timing and pitch. The first
Effect Parameter is Delay Time, which can be synchronised or
unsynchronised in relation to the tempo. The second Effect
Parameter selects the Pattern. Every pattern is individual so
you should test the various settings to get a feel for them.
Changing the Pattern option to “Fade” enables cross-fading
between patterns. The Amount Parameter determines the intensity of the pitch
component of the Pattern Delay, while the Decay Parameter determines the volume
relationship of the 8 delays. Alternate delay lines can be turned off using the Option
Settings 2 [nd] and 3 [rd], which respectively enable only every 2 [nd] or 3 [rd] delay line to be heard.

##### Reverse Delay

Reverse Delay layers a played-backward delay signal over the
source audio. The Time Left and Time Right Parameters control
the delay time as well as the length of the played-backwards
material. The reversed signal is blended in and out to avoid
clipping. The Fade Parameter determines the length of the
cross-fade, while the Feedback controls the intensity and
duration of the delay tails.

##### Pitch Delay

Pitch Delay is a classic delay with an integrated filter and the
additional option of modifying the pitch of the delay tails. The
Time Left, Time Right and Feedback Parameters are standard
delay controls. Along with synchronisation settings you can also
set up when the incoming signal is routed into the delay.
“¼ ...” Allows the incoming signal to pass only once for the
length of a quarter note.
“¼--- ...” Allows the incoming signal to pass once for the length of a quarter note and
then pauses for 3 quarter notes.
“¼- ...” Allows the incoming signal to alternate between passing and pausing for the
length of a quarter note.
Option settings for eighth note and sixteenth note denominations follow the same
pattern.


22


The Pitch Parameter adds a positive or negative pitch change to the delayed signal.
Furthermore you can add the filter to create special new Dub-style delay effects. There
are several filter settings available so you can decide whether the Pitch and Filter work
separately, together, or inversely. For every Filter Type there is a low and high (Q)
resonance setting. The first menu entry “Pitch” has no filter and only modifies the pitch. A
“+” in front of the menu entry gives an additive cutoff modification, when turned up the
Pitch Controller also increases the Filter Frequency. A “-” in front of the menu entry will
result in the Filter Frequency decreasing when turning up the pitch. If the menu entry
has no prefix then only the filter is active. With the 1.5 update there are new modes with
a constant filter-frequency, the knob will adjust the input level of the signal.

#### Modulation Effects

##### Flanger

This is a classic Modulation Effect using very short delay times
to create Flange and Chorus effects. The Delay Left and Delay
Right Parameters enable you to set independent delay times
for each of the respective channels. Using the Flanger/Chorus
settings you can select different delay time ranges. In Flanger
Mode the range is 1-20 milliseconds and in Chorus Mode the
range is 25-50 milliseconds.

The Feedback Parameter returns the signal back to the delay input to enhance the
effect. The “Inverse” Option of the Feedback Parameter inverts the phase of the
feedback by 180 degrees and creates a softer, more diffused sound. With a negative
setting the Filter Parameter works as a Low-pass filter and with a positive setting as a
High-pass filter. The menu on the Filter Parameter offers three different resonance
values to give different tonal qualities to the filter.

##### Phaser

As well as generating classic phase effects using the LFO’s, you
can also directly change the Phaser value. Assigning the Phase
Parameter to the Main Controller and applying different
transformation curves can create some interesting effects. The
intensity is modified with the Feedback and Depth Parameters.
Feedback can be inverted for a fluffier sound here too and the
Width Parameter shifts the phase of the left and right channel
creating stereo movement.

##### Tonalizer

The Tonalizer is a special delay that uses short, tonal delay
times and high feedback to create tuned delay tails. Note Right
and Note Left Parameters define the pitch of the left and right
channel, while the Option Menus enable you to choose
between various tonal intervals, from semi-tones through to
octaves. High settings of the Feedback Parameter will widen
and intensify the tonal effect. When turned clockwise of centre
position the Hold Parameter freezes the wet signal, creating a continuous tone.


23


In this position no incoming audio is being processed and only the frozen, Tonalized delay
will be heard.
In the Hold menu you'll find the root note option which let's you define a root-note.
The notes defined by the first 2 parameter are then on top of this one. For the first 2
parameter there are now scales available. This makes sure that the delay-tuning fits into
the selected scale. This gives you the possibilities to adjust the sound related to your
song tuning.

#### Reverbs

##### Reverb

The Reverb is a first class Echo Effect. The Size Parameter
controls the room size, while Reverb Time defines the length of
the reverb tail. The Reflectivity Parameter determines the
intensity of reflections from the virtual reverb space. The Input
Parameter determines the volume of the incoming signal being
sent to the effect. Special effects can be created through
dynamic activation of the Input Parameter. For example you
can set up an LFO to control the Input Parameter so the Reverb activates in a rhythmical
way. Taking this idea further you can assign a Step Sequencer to the Input Parameter to
trigger the Reverb effect in more complex patterns. There are some filter modes under
the reflectivity control. You can add a highpass filter with fixed cutoff or BP, Comp or HP
where the cutoff is controlled by the Reflectivity knob.

##### Freezeverb

The Freezeverb Effect is a special Echo Effect that freezes the
Echo signal. The Size Parameter defines the virtual room size
and the Damp Parameter dampens the reflection of the virtual
reverb space. Width Parameter creates a broader stereo picture
by slightly offsetting the left and right signals. The Freeze
Parameter has two positions, off and on. When turned anticlockwise of centre the Freeze is inactive, when turned
clockwise of centre it is active. Remarkable effects can be created by modulating the
Freeze Parameter with the Envelope Follower. Be aware that when the Freeze Parameter
is active no audio is being sent to the reverb. Freeze should be off when you start the
audio otherwise there will be silence when you play the source signal.


24


#### Transformation Effects

##### Ringmodulator

The Ringmodulator is an effect where an oscillator modulates
the amplitude of the audio signal. The VCA Parameter
transforms the Ringmodulator defining how the internal
oscillator is being amplified or the incoming signal multiplied.
The AMT Parameter determines the harmonisation between the
source signal and the oscillator. A major chord for example, has
4 ring modulators instead of one. Use the Waveform Parameter
to select from four available waveforms: Sine, Triangle, Pulse or Sawtooth.

##### Vocodizer

The Vocodizer is more an instrument than an effect as it can
create independent melodies, rhythms and sounds. The Sound
Parameter is the spectral-dynamic reaction to the incoming
signal. There are four base waveforms: Sawtooth, Triangle,
Pulse and Sine. In the sub-menu these are also available in
Unison Mode with the suffix “2” for a more powerful and
harmonically richer sound. The NOTE Parameter determines the
base note. The submenu defines the note range (one or two low or high octaves). The
Parameter SPREAD creates a chord and determines the number of voices. In the sub
menu, the chord type is chosen. The parameter ARP creates an arpeggio out of the
selected chord. In the sub menu the arp style and pattern is chosen. The “Trig”-Entries
make the Arp play the next note when the Arp Control gets above 50%. Therefore the
envelope follower should be used, but also using the stepsequencer is a good choice.
When the menu entry contains a „2“, duophonic arp melodies will be created.


Back To Table of Content


25


#### Amplifier

##### Levelizer

The Levelizer is a basic effect for modifying volume, panorama,
bit depth and sample rate. Although these parameters are
relatively simple, with the use of Modulators many classic
effects like Compression, Autopan, Tremolo or Gating can be
achieved. The Volume Parameter can double the amplitude of
the audio signal or reduce it to silence. The Pan Parameter
moves the signal into the left or right channel. The Crush
Parameter reduces the bit depth and has three options: “Normal” reduces the bit depth
to create a classic low-bit sound. “Hi” mode reduces the signal in a non-linear way,
resulting in loud signals being bit-reduced more than quiet ones. “Low” mode works
inversely, so quiet signal parts are being bit-reduced more than loud ones.

There are also three Options for the Sample Rate Parameter. “Hard” creates classic
sample rate reduction until complete destruction. “Dynamic” reduces the sample rate
dynamically according to the amplitude of the incoming signal. The louder a signal the
greater the reduction of the sample rate will be. In “Absurd” mode the sample rate will
drop towards zero, creating even harsher overtones than in “Hard” mode.

##### Guitar Amp

The Guitar Amp is an Amplifier/Distortion emulator with
integrated multi-band EQ. It allows for individual amplification
or distortion of the three EQ Bands and therefore offers greater
control of the amplifier overtones. The Drive Parameter controls
the total amplification. Stereo and Mono mode are available.
The Low, Mid and High Parameters define the frequency bands
which are to be amplified. Dynamic effects can be created
through modulation of the Effect Parameters using a fast Envelope Follower. Direct
assignment to the Main Controller also creates some interesting sound effects. With the
1.5 update there are now some options available to limit the output of the amp. The 3
limiting options will make sure the signal stays in 0db range.


Back To Table of Content


26


#### Loop Effects

##### Looper

Besides the classic looping, this effect can add swing to your
looped signal. The Size Parameter determines the length and
repetition rate of the loop. You can choose between the three
synchronisation styles in the Option Menu. “Sync”, “Sync TP”
and “Free” options dictate the synchronisation style. “Sync”
quantises the loop length into ½ to 1/128-bar steps. Triplet or
Dotted Note steps can be selected using “Sync TP”. “Free”
mode offers loop lengths from 1 to 500 milliseconds. SyncX mode ensures that Size
changes will only be activated at sync time. The Swing Parameter defines the relative
lengths of alternate loops, lengthening and shortening them in order to create swing
while maintaining synchronisation. The Trigger Parameter samples new audio material
into the Looper when turned clockwise from centre. Assigning this parameter to an LFO
or Step Sequencer can automate the sequential sampling of source audio producing
excellent beat and rhythm variations. The AMP Parameter determines the volume and
serves to gate loops or blend them in and out.

##### Pitch Looper

The Pitch Looper gives you the ability to add pre-defined pitch
sequences to the looped slice. The Size Parameter defines the
loop length and the Pattern Parameter selects the pitch
sequence. In the Options Menu you can select “Glide” to bend
between pitches in a similar way to Portamento. The Trigger
Parameter functions in the same way as the in the Looper. The
Decay Parameter sets the number of loop repetitions, and for
silencing individual slices it also has a few Options:
2nd Every second slice is being played
Triple 1 Two out of three slices are being played
Triple 2 Two out of three slices are being played (Variation)
Swing A swing is being generated

##### Pan Looper

In addition to the alteration of the stereo picture of the slices,
the Pan Looper can also manipulate the pitch. The Size and
Amp Parameters define the loop length and volume
respectively. The Pan Parameter changes the panorama of the
loop. The Pitch Parameter defines the pitch, while the Amp
Parameter offers additional options to create swing and
rhythmical elements.

##### Reactor

The Reactor effect is a Transient Looper and is therefore a self
activating loop tool. The Active Parameter adjusts the
responsiveness of the loop trigger. The Holdtime Parameter
defines the length of the sampling period. Parameters two and


27


three are switchable. Selecting “Freeze” from the Option Menu the Parameters Speed
and Pitch are operable. With the Option “Reverb”, Parameters Mix and Intensity are
available. The Intensity Parameter is a special Reverb Hold Level that produces some
great effects when combined with Modulators. With the 1.5 update there is a new sync
option available called SyncX. In this mode changes of the size will be done as if they had
run from the beginning. This means for example if you start with 1/8 size and then
change to 1/4, another 1/8 slice will be inserted in order to ensure correct alignment for
the 1/4 slice.

##### Slice Arranger

The Slice Arranger does exactly that, slicing the incoming signal
into new patterns. The audio signal is recorded in real-time,
then divided into slices and arranged according to the Pattern
and Fill Parameters. With the Pattern Parameter there are a
number of pre-defined patterns. You can choose from eight
pattern types in the Options Menu with 50 patterns for each
type. The two Fill Parameters incorporate Rolls and Microloops
into the selected Pattern. Furthermore, each pattern allocates different slices to the Fills.
Here are the Fill Options:

  - Repeat: The final phase of the slice is being looped

  - Up: Upwards-pitch

  - Down: Downwards-pitch

  - Hard: Dramatic repeat

  - Pong: Forwards and backwards repeat

  - Soft: Simple more subtle repeat
The Decay Parameter controls the length of the slice envelopes as well as highlighting
the end of the sliced audio with help of an amplitude envelope. With the Options “Beat”
and “2 Beats” the slice arranging can be applied to the audio over one or two beats.


Back To Table of Content


28


#### DJ Tools

##### Granulizer

The Granulizer is a Grain Effect with control over tempo and
pitch. The Amount Parameter has two Options: “Amount”
mode sets the tempo to be changed in relation to the original
audio signal. Full off is the original tempo and full on is stop. In
“Position” mode the Amount Parameter navigates you through
the recorded audio signal. The Grainsize Parameter defines the
length of each individual grain in milliseconds. There are also
several Options for cross-fading and the tempo of the individual grains is determined
using the Distance Parameter. To avoid gaps in the audio signal, the Grainsize value
should be larger than the Distance value. To change the play-direction of the grains, the
Distance Parameter has several Options, “Forward”, “Backward” and “Ping Pong”. The
Pitch Parameter determines the pitch of the grains. If no time-stretching is active and the
pitch is being moved upwards, then a minimal delay is being mixed into the audio signal
which may not be audible.

##### Stutter

The Stutter Effect continually adds an Amplitude Envelope to
the audio signal. The Size Parameter determines the repetition
rate of the envelope. As with all the other time based
parameters there are also synchronisation options. SyncX
mode ensures that size changes will only be activated at sync
time. The SyncPPQ mode will sync the stuttering to your host
clock. The Decay Parameter determines the absolute end of the
envelope and offers in the options “rhythmic”, “shuffled” and “swing” variations. The
Shape Parameter determines the waveform of the envelope. This parameter blends
continuously through the following waveforms: Downwards Sawtooth, Sine, Pulse and
Upwards Sawtooth. The Pan Parameter enables control of the stereo position of the
effect signal and can be combined with Modulators to create dynamic Panning effects.

##### Vinylizer

The Vinylizer Effect simulates the stopping and scratching of
vinyl discs. The Size Parameter defines the time interval of the
stops and scratches. If the value is set to OFF it will stop only
once. With the Slow Down Parameter the speed of the stopping
is determined and there are three options. “Stop” stops the
audio signal with the rate defined by the Slow Down parameter.
“Scratch” plays the audio signal alternately forward and
backwards while slowing down and speeding up the audio signal. This happens in relation
to the selected interval with acceleration rate controlled by the Slow Down Parameter.
The Downslope and Upslope Parameters define the shape of breaking and acceleration.
In full anti-clockwise position the slope becomes logarithmic this transforms into an
exponential curve as you rotate through to a fully clockwise position. Setting these two
parameters differently gives you the quick-stopping and slow-starting vinyl record sound.


Back To Table of Content


29


#### Filters

##### Filter

With the Filter Effect a quality, Stereo, Multi-mode-filter is
available. The Cutoff Parameter controls the cutoff frequency
and offers the modes “Highpass” (only allows frequencies
above the cutoff to get through), “Bandpass” (only allows the
frequencies around the cutoff to get through), “Lowpass” (only
allows frequencies below the cutoff to get through), and
“Comb” (a special delay which works with filter frequencies as
delay times). To synchronise the left and right channel there is a sub-menu on the Cutoff
R Parameter with the option to “Link”. The resonance for the left and right channel is set
with the Reso L and Reso R Parameters. Be careful with resonance values, high settings
can produce harmful volumes for you and your equipment.

##### Filter Pattern

The Filter Pattern Effect adds pre-defined Filter Patterns to the
audio signal in which filter settings run through a sequence.
The Pattern Parameter enables you to choose from 25 different
patterns, each with 10 variations. With the 1.5 update there is a
new variation called 'Beardyman', this variation will offer more
simple filter rides with only one filter type. The Resonance
Parameter controls the Q Factor. When in centre position the
Sweepspeed Parameter will set the filter sweep to complete once. Turned anti-clockwise
the speed of the sweep is reduced so it will only partially complete. Turned clockwise the
sweep will accelerate and complete more than one cycle. In this situation the option
setting dictates what happens to the sweep, either being repeated “Repeat”, passed
forward and backwards alternately “Ping Pong” or synced to the host clock “Synced”.
With the 1.5 update there is a new mode here called Synced X. In this mode the
sweepspeed is always aligned to the original clock. (see Looper for detailed description)

The Sweeprange Parameter defines the range of the frequency sweep. Be careful with
resonance values, high settings can produce harmful volumes for you and your
equipment.


Back To Table of Content


30


##### Vowel Filter Spectralizer



The Vowel Filter offers a powerful Talkbox sound, making the
audio signal sound as if it were being spoken. The Vowel A and
Vowel B Parameters identify the vowels between which the Mix
Parameter cross-fades. The Vowel A Parameter can have a filter
assigned to it from the sub-menu, “Highpass”, “Lowpass”,
“Bandpass” and “Comb”. Keeping the Resonance Parameter
settings high will ensure you get a rich vowel sound.



The Spectralizer is a filter-bank with 32 delays. Every delay has
its own delay time and filter frequency. The delay time and
density are determined by the Delay Time Parameter. Available
modes are “Tonal”, “Sync” and “Free”. The Frequency
Parameter adjusts the cutoff frequency with which the delays
work, the available sub menu offers different relations of the
delaylines and their frequencies. The Resonance Parameter
controls the resonance of all the filters. You can select 2 Pan modes here which will bring
some space into the sound. The Bands Parameter determines the number of delays used.
Be aware that this effect is quite complex and results depend greatly on the source
audio. With drum parts for example, a high resonance value with full delay size produces
a very bizarre effect. Test the various presets to get an overview of the variety of sounds
that you can create with this effect. With the 1.5 update there are 2 pan modes (under
the resonance parameter) available which offers stereo distribution of the bands.


Back To Table of Content


31


### MIDI Program Change

Deactivate the 'ignore PrgChange' option in the Turnado setting screen.
Then create a folder called 'Midi Programs' beside the other presets folder (Factory 1,...)
in Documents/Sugar Bytes/Turnado/Global Presets/

Put the patches you want to load in this folder.
You should see the MIDI Programs folder in the Turnado preset menu after restarting
Turnado.

Then you can send MIDI prgchange messages to load the patches from that folder.

They should load via program change according to their alphabetical order.


Back To Table of Content


32


### FAQ

#### Silence




- Take note that some effects sample the audio signal and then replace it with the



sampled signal. For example if a Looper or Slice Arranger controller is turned on, or
the Freeze in Freezeverb active before audio is played, you will hear nothing.

- Turnado produces no audio if the serial number is wrong. This can be checked and



corrected in the About Screen.

- If the standalone does not process audio the audio settings should be checked, it



is possible that the wrong input or output driver is selected.


#### Noise


  - If the laptop microphone is selected in the audio settings of the Standalone

version you may experience feedback and a lot of noise. Audio settings should
always be chosen carefully.

#### Licence




- The Turnado Licence includes both macOS and PC version and can be used on



two computers at the same time. For use on more than two computers an
additional licence needs to be acquired.

- Sale of the software and the involved licence transfer is only possible from 3



months after purchase of product.


#### Compatibility / Returns Policy


  - Please check compatibility by downloading the demo version before purchasing.

  - Return of the software is on a goodwill basis, and only within one week of

purchase.

### Contact


Sugar Bytes GmbH | Made of passion
Robert Fehse, Rico Baade | Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395 | Str.-Nr. 37/207/21266 | HR-Nr. HRB 124199 B
[info@sugar-bytes.de | www.sugar-bytes.com](mailto:info@sugar-bytes.de)


Back To Table of Content


33


