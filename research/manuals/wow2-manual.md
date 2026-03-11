# **WOW2**

## **User Manual**


### Table of contents

#### WHAT IS WOW2 4 Installation 4

WINDOWS 4
macOS 5
#### Uninstalling 5 Authorization 6 WOW2 STRUCTURE 7 ABOUT SCREEN 7 THE PRESETS 8 FILTER SECTION 9 Classic Controls 9

Cutoff 9
Resonance 9
Distortion 10
Level 10
Dry/Wet 10
#### Filter Types 11

Highpass 11
Bandpass 11
Lowpass 12
Special 12
#### Vowel Mode 13 MODULATION SECTION 14 Envelope Follower 14

Gain 14
Attack 14
Decay 14
Freq Range 14
Source 15
#### LFO 15

Wave 15
Rate 16
Audio Trig 16


2


Trig Sens 16
#### Step Sequencer 16

Tempo 16
Direction 16
Glide 16
Random 16
#### Wobbler 17 MODULATION ASSIGNMENT 18 HOST INTEGRATION 20

Cubase 20
Sonar 20
Live 21
Logic 21
Pro Tools 22
Studio One 22

#### REMOTE 23 QUESTIONS? 23

WOW2 makes no sound 23
Have I found a bug? 23

#### LICENSE 23 IMPRESSUM 23


3


### What is WOW2

WOW2 is a multimode filter plugin, offering 21 high quality filter types. Each filter type
can be operated in vowel mode, giving you the best vocal sounds available. Choose from
3 analog and 4 digital distortion types to beef up your audio.

WOW2 comes with the craziest modulation system you will ever find. Modulators can
modulate and randomize each other, and the wobble generator is on board, for rhythmic
control voltage without headache.

Enjoy the juiciest, punchiest filters with close to analog quality, only available in WOW2.

#### Installation


[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)

The standalone version and the manual will be installed into
Windows: C:\Program Files\Sugar Bytes\WOW2
macOS: /Applications/Sugar Bytes/WOW2

Presets will be installed into Documents\Sugar Bytes\WOW2.

Do not move the WOW2 presets after installation!

##### WINDOWS


Default installation paths:

VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins


Back to Table of Content


4


##### macOS

The Audio Unit, the VST Plugin and the AAX Plugin will be automatically installed into the
correct folders.

Default installation paths:

VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins

#### Uninstalling


In order to uninstall WOW2, please take the following steps:

Windows: Uninstall WOW2 under Control Panel/AddRemove Software.
macOS: Here is the way to delete everything regarding WOW2.

/Applications/Sugar Bytes/WOW2
/Library/Audio/Plug-Ins/VST/WOW2.vst
/Library/Audio/Plug-Ins/VST3/WOW2.vst3
/Library/Audio/Plug-Ins/Components/WOW2.component
/Library/Application Support/Avid/Audio/Plug-Ins/WOW2.aaxplugin

~/Documents/Sugar Bytes/WOW2
~/Library/Preferences/com.sugar-bytes.WOW2.plist

~ means: /Users/YOURLOGINNAME (your home folder)

(Please note that since OSX 10.7.x the library folder is a hidden folder.
Therefore please use the "Go To Folder" menu and then enter ~/Library.)


Back to Table of Content


5


#### Authorization

The serial number is requested for installation.

If the serial number validation fails, the plugin will show that in the WOW2 About Screen.


Back to Table of Content


6


### WOW2 Structure

#### About Screen

Click on the WOW2 logo to open the About Screen.


Here you find your serial number, if it’s needed to download new updates.
The serial number field can usually be edited (select text, copy/paste serial).
In some hosts it does not work, so if the serial is invalid, just start the standalone and
enter the correct serial there.


Back to Table of Content


7


Ignore Program Change:
Incoming program change messages will be ignored. Only presets from the folder “MIDI
Programs” will be used for program changes.

CC Preset Isolate:
MIDI-CC assignments (MIDI Learn) will not be saved or changed with the presets.

CC Map Load/Save:
Load or save your current MIDI CC assignment.

#### The Presets


In the left half of the screen you will find the preset browser.

The top line shows the current preset name and offers different file operations.


Step through the presets, forward or backwards.


Load a random preset.


Loads a clean preset to start from.


Opens a save dialog to save your preset.

You can add your own preset folders, subfolders are not allowed.

Back to Table of Content


8


Find the WOW2 presets in Documents/Sugar Bytes/WOW2/Presets.

If the Ignore Program Change option is disabled, Program Changes will select presets
from the “MIDI Programs” folder.

Usually, MIDI Assignments to parameters are saved with the Preset.
Activate “CC Recall Isolate” to avoid Presets from recalling CC Assignments.

### Filter Section


The red part of WOW2 includes the actual filter section.

It features Dry/Wet, Level, Cutoff, Resonance, Vowel Mode and Distortion.
You can choose from 7 distortion types, 21 filter types and use the Vowel Mode here. All
these Parameters can be modulated. Right click a parameter, to assign modulation and
MIDI Learn to it.

Additionally, all modulation amounts are available on the bottom of the modulation
section, in order to have these controls automated and MIDI-learned. This means, WOW2
can assign a modulation from source to target, but also from target to source, which is
most convenient.

#### Classic Controls

##### Cutoff

The biggest knob is the Cutoff control. Basically, it determines the cutoff frequency,
which is the frequency where the filter works. This frequency is boosted by the resonance
and determines where the Lowpass cuts high frequencies off, or where the Bandpass
lets the signal through.

In Vowel Mode, the Cutoff Control morphs from Vowel A to Vowel B.

##### Resonance

The resonance is actually the feedback level of the filter circuit. Turning this control up
will expose the cutoff frequency. In some filter types the resonance can introduce “selfoscillation”, which turns the filter into a sine oscillator which oscillates at cutoff
frequency, turning WOW2 into a dub siren, or whatever you make of it.

If you run in unwanted self-oscillation, use the Envelope Follower to push the Reso up to
where you want it, while silence will hold the Reso below self-oscillation.


Back to Table of Content


9


##### Distortion

The Distortion Parameter always shows the name of the selected Distortion type. If the
Distortion Parameter is set to zero, the distortion is bypassed. In the upper half of the
distortion menu you find the Signal Flow control. Put the Distortion in front or behind the
filter for a vast range of sounds.

7 Distortion types are available:



1. Parabolic. Tube-like overdrive, creating a rich harmonic spectrum,



four times oversampled for finest harmonics without aliasing.
2. Hyperbolic. Tube-like double-drive for rather angry distortions. Four times



oversampled for crystal clear harmonics without aliasing.
3. Diabolic. Diode-like distortion, for the apocalyptic punch. Four times oversampled

for high definition apocalypse without aliasing.
4. One Bit. Turns everything into a pulse wave. Four times oversampled.
5. Sine. The audio signal drives a sine function. Creates sounds from roasted ham to



spider invasion. Four times oversampled.
6. Crush. The bit crusher you would have asked for.
7. Digitize. The sample rate reducer you would ask for.


##### Level

The Level control can double up the signal volume, so when the Level control is at 50%,
you have 1:1 Level from input to output.


Use the Envelope Follower to turn down the Level according to the input signal, to create
compressor effects. The modulation system offers all kinds of Level modifications, like
stuttering, tremolos, compressors.

##### Dry/Wet

Here you mix between input and output signal. Especially the Vowel Mode
often requires not a full wet mix for best performance. The modulation system can be
used to blend in the filter in every possible way.


Back to Table of Content


10


#### Filter Types

Select the filter type here. We included Moog and MS filter models, as well as some Sugar
Bytes creations like the “030 Lowpass”. 030 and MS models are oversampled for best
performance at the whole frequency range. The (sat) filter models include a saturator, so
turning up the resonance will not turn down the input level. These are two existing
philosophies about handling the Resonance, so we decided for both ways.

Available are the following filter types:

##### Highpass

Cuts off low frequencies according to the cutoff frequency.

2Pole: 12db Highpass from a SVF (State Variable Filter)

2Pole(Sat): 12db Highpass SVF including saturation. See text above.

4Pole: 24db Highpass SVF

Diode MS: 12db 1pole Highpass, based on the MS diode ladder filter.

##### Bandpass

Cuts off low and high frequencies and passes thru the cutoff frequency.
Best filter for talkbox effects using the Vovel Mode.


2Pole: 12db Bandpass SVF Back to Table of Content


11


2Pole(SAT): 12db Bandpass with saturation (see text above)

4Pole: 24db Bandpass SVF

Diode MS: 12db Bandpass, based on the MS diode ladder filter.

Ladder MG: 24db Band/Lowpass filter, based on the Moog Ladder Filter.

##### Lowpass

Cuts off high frequencies according to the cutoff frequency.

2Pole: 12db Lowpass SVF

2Pole(SAT): 12db Lowpass SVF with saturation (see text above)

4Pole: 24db Lowpass SVF

8Pole: 48db Lowpass SVF

Ladder MG: 24db Lowpass, based on the Moog Transistor Ladder filter

Diode MS: 12db Lowpass, based on the MS Diode Ladder filter

030: 18db Lowpass, based on the Roland TB-303 filter.

##### Special

This category contains filter types beyond the HP/BP/LP classics.
Mid Boost: 24db SVF Lowpass/Bandpass combination

Peak: Creates a peak at the cutoff frequency without losing original audio.

Notch: Creates a hole at the cutoff frequency, keeping original audio.

Band Reject: Erases frequencies around the Cutoff Frequency and creates two peaks
with high resonance, very good in VOWEL MODE.

Mid Clear: 12db Highpass/Lowpass combination which eliminates the mid frequencies
between them, while they run away from each other as you turn up the cutoff.

Comb: A feedback delayline with delaytimes according to the cutoff frequency. Should
be used with high resonance. This filtertype is working very good with the VOWEL MODE
and can produce intensive flanger- and chorus-effects in classic mode.


Back to Table of Content


12


#### Vowel Mode

Put the filter into Vowel mode, where the Cutoff knob is used to fade between two vowel
frequencies. Bandpass and Comb Filter modes are recommended for achieving the best
vowel sounds. A high Resonance is usually needed to create the “Formant” necessary for
the vocal sound.

[i:] as in feet


[e] as in men


[æ] as it bat


[y] as in tu (French)


[ə] as in the


[ɑ] as in father


[ɔ] as in awe


[o] as in copy


[u] as in boot


Rightclick a phonetic symbol to modulate the Vowel Mode. You can see the phonetic
symbols switching. Click on the phonetic symbol to see the basic value.


Back to Table of Content


13


### Modulation Section

The modulation section includes 4 modulation engines that can modulate each other as
well.

#### Envelope Follower


Follows the amplitude of the incoming audio signal to produce a control curve. The
Envelope Follower can be focused to a certain frequency to select triggers from the audio
signal.

##### Gain

Set the level of the controller signal here.

##### Attack

Smoothes the rising part of the controller signal.

##### Decay

Smoothes the falling part of the controller signal.

##### Freq Range

A Bandpass filter in the sidechain circuit allows frequency selective envelope following.
That way you can grab a kick, a snare or other signals to produce a controller signal. Turn
the knob down to bypass the filter and feed the whole spectrum into the Envelope
Follower.


Back to Table of Content


14


##### Source

The Envelope Follower can be provided with the input signal or with the output signal, to
create the envelope from.
Since the Filters might create high levels, the Envelope Follower can be used to modulate
the Level control.


An oscillator generates a control curve with different waveforms.
The LFO has three sync modes.

1. Sync, Audio Trig: The Audio Trigger button will restart the LFO along with the incoming
audio. Use the Sens control to adjust the incoming audio to your desired retrigger rate.
Put the Sens fader to the left to create more triggers, put Sens to the right to create less
triggers.

2. Free, Audio Trig: The LFO runs at divisions of your host bpm and
can be retriggered by the incoming audio signal.

3. Songposition: The songposition is used to generate the LFO waveform. Using that
method, the LFO wave is absolutely reproducible
in every position of your song. For example, on beat 132 the waveform will be in the
same position, no matter if you started the playback at beat 12 or beat 36.

##### Wave

The LFO waveform. Sine, Saw, Square, Triangle and random are available.


Back to Table of Content


15


##### Rate

The speed of the LFO curve. Always in sync with your song.

##### Audio Trig

The LFO can be retriggered by the audio signal.

##### Trig Sens

Sensitivity of the LFO retrigger.

#### Step Sequencer


A sequencer with 16 steps generates a control curve.

##### Tempo

Speed of the Sequencer. It´s always in sync with your song.

##### Direction

The reading-direction. Forward, Backward, Pingpong or Random.

##### Glide

Glides the sequence steps to a continuous curve.

##### Random

Selects a random control curve.



Back to Table of Content


16


#### Wobbler

The Wobble Knob lets you choose from 12 LFO Speeds and 16 Waveforms.


Special about the Wobble LFO are the fixed values.
The snowflake indicated Freeze mode. Like a sample and hold module,
the Freeze will maintain the last active value as long as it is selected.
If the Wobble Knob turns from a sine wave to the snowflake, the last
value of the sine wave will be held until another wave form is selected.


Furthermore, there are 5 fixed valued available. These values are
0%, 25%, 50%, 75% and 100% and are displayed by square with
different sizes. These values make it possible to use the Wobble Generator
like a step sequencer.


The central wave form control sets all wave forms at once.


The Random Button sets a random wave form situation. Can be modulated, in order to
auto-randomize at certain events.


Here you can set the starting phase of the wobble LFO. This determines if the modulation
will go upwards or downwards after you hit a note.


Back to Table of Content


17


### Modulation Assignment

In order to assign modulators to their targets, you have two choices.
Rightclick the target parameter to choose from the available modulators,
or select the source-modulator and find the target parameters on the bottoms of the
modulators area.

The Mod-Amount knobs control the modulation intensity from -100% to +100%. The
modulation can be set positive or negative, so it will add or subtract with the value given
by the parameter. The Reset Button resets all modulations to zero. Assigned modulations
can be identified by the moving ring around the parameter.

Double click a control to set it to zero.


Right click a control to open the MIDI Learn function.
Using MIDI Learn, you can control a WOW2 parameter with an external MIDI controller.
Just assign a MIDI track to WOW2 and use it to send MIDI CC´s to WOW2.

These are the Modulation Assignments below the Modulators.
Each Modulator has its own set of 6 assignment screens.
The Amount Controls can be MIDI learned and automated:


Main Filter Assignment


LFO Assignment


Env Follower Assignment


Back to Table of Content


18


Step Seq Assignment


Wobbler Assignment


Vowel Assignment


Back to Table of Content


19


### Host Integration

#### Cubase

Load WOW2 as an insert effect
on an audio track or instrument
track.
Create a MIDI track and choose
WOW2 as target for the MIDI
track.
Now you can trigger WOW2 with
your MIDI knobs and record
controller movements in the MIDI
track.

#### Sonar


Plug in WOW2 as an insert effect. Then enter the Plugin Settings and check the
"Configure As Synth" option. Then plug WOW2 out and plug it in again.

Create a MIDI track and choose WOW2 as target for the MIDI track.


Now you can trigger WOW2 with your MIDI
knobs and record controller movements in
the MIDI track.


Back to Table of Content


20


#### Live Logic



Use WOW2 as Insert Effect on any track.
Now create a midi track and send the midi
signal to the audio track with WOW2 loaded.

You can now control WOW2 with your hardware knobs,
sending midi to the midi track, or using midiclips.



Use WOW2 as an insert effect.

In order to control it with Midi, pick it up on an Instrument Track and choose it from the
Midi Controlled FX list in the Plugins menu in the I/O slot.


Then, in the Sidechain menu in the
upper right corner, select the Audio
track or Bus that you want to use
with WOW2.

Then, in the Logic mixer, turn down
the level of the audio track that you
selected in the WOW2 sidechain
menu.


Back to Table of Content


21


#### Pro Tools

Use WOW2 as an insert effect.
In order to control it with Midi, create a Midi track and choose WOW2 as Output in the I/O
Menu of the Mixer.

#### Studio One


Go to the Studio One menu and choose Options, click on Locations, then VST Plug-Ins.


Click the Add button and select your VST
Plugin folder. Press OK then close and reopen Studio One. If you still don’t see your
plugin, go back into that screen and click
the “reset blacklist” button, then close and
open Studio One again.

Pick it up from the VST Effects list. Create
an instrument track and choose WOW2 as
midi out target for that track.


Back to Table of Content


22


### Remote

All relevant WOW2 parameters can be controlled via Host Automation.
All WOW2 controls can be remoted via MIDI controllers. You find the MIDI Learn function
in the modulation mixer that opens up when you right click a control.

### Questions?

##### WOW2 makes no sound

Are the level meters showing an Audio Signal?
If Audio In works, but Audio Out is silent, your filter setting might be filtering out all
audible frequencies (HP too high?, LP too Low?).
Level could be modulated to zero. Right click Level to check out the modulation
assignments.
Is the serial number marked as invalid in the about screen / on the panel?

##### Have I found a bug?

Please write to support@sugar-bytes.de

### License




- The WOW2 License covers both the macOS and PC versions and can be used on

two computers. For any use on more than two computers, you must buy an
additional license.

- You may resell the software (and therefore transfer the license) three months or

more after purchase.


### Impressum

Sugar Bytes GmbH 2013 | Made of passion
Robert Fehse, Rico Baade | Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395 | Str.-Nr. 37/207/21266 | HR-Nr. HRB 124199 B
[info@sugar-bytes.de |](mailto:info@sugar-bytes.de) [www.sugar-bytes.com](http://www.sugar-bytes.com/) Back to Table of Content



23


