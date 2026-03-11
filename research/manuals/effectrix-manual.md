# Effectrix

## User Manual


### **Table of contents**

##### What Is Effectrix 4 Installation 5

Windows 5
macOS 6

###### Uninstalling 7

##### Authorization 7 Effectrix structure 8 The Header 8
###### Global Presets 8 About Screen 9 Bypass 9

##### The Effect Sequencer 10
###### Tempo 10 Swing 10 Trigger By MIDI 10 Use Pattern Keys 11 Copy/Paste Buttons 11 Chaos Button 11 Init Button 11 Loop Bar 11 Tracks 12 Modulation Sequencer 12

##### Effect Controls 13
###### Effect Presets 14

##### Master 14 Effects 15
###### X-Loop 15 Loop 15 Scratchloop 16 Reverse 16 Stretch 17 Vinyl 18


2


###### Tonal Delay 18 Stutter 19 Crush 19 Filter 20 Phaser 21 Chorus 21 Delay 22 Reverb 24

##### Host integration 25 MIDI remote 31 MIDI program change 31 Questions? 32 Effectrix makes no sound 32 Have I found a bug? 32 Impressum 32

3


### What is Effectrix

Effectrix is an effect sequencer which has been made for applying effects using a step
sequencer environment.

You can use Effectrix to completely mash up your tracks, turn them into grainclouds or
just do some slight alternations to your beats.

Using the 12 subsequences triggered by MIDI notes, you always have some stunning
effect performances at your fingertips.

Let´s dive a bit deeper into this source of new ideas and styles.


4


### Installation

[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)

The standalone version and the manual will be installed into
Windows: C:\Program Files\Sugar Bytes\Effectrix
macOS: /Applications/Sugar Bytes/Effectrix

Presets will be installed into Documents\Sugar Bytes\Effectrix.

Do not move the Effectrix presets after installation!

#### WINDOWS


Default installation paths:

VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins


BACK

TO TABLE OF CONTENT



5


#### macOS

The Audio Unit, the VST and the AAX Plugin will be automatically installed into the
correct folders.

Default installation paths:

VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins


BACK

TO TABLE OF CONTENT



6


### Uninstalling

In order to uninstall Effectrix, please take the following steps:

Windows: Uninstall Effectrix under Control Panel/AddRemove Software.

macOS: Here is the way to delete everything regarding Effectrix

/Applications/Sugar Bytes/Effectrix
/Library/Audio/Plug-Ins/VST/Effectrix.vst
/Library/Audio/Plug-Ins/VST3/Effectrix.vst3
/Library/Audio/Plug-Ins/Components/Effectrix.component
/Library/Application Support/Avid/Audio/Plug-Ins/Effectrix.aaxplugin

~/Documents/Sugar Bytes/Effectrix
~/Library/Preferences/com.sugar-bytes.Effectrix.plist

~ means: /Users/YOURLOGINNAME (your home folder)

(Please note that since OSX 10.7.x the library folder is a hidden folder.
Therefore please use the "Go To Folder" menu and then enter ~/Library.)

### Authorization


The serial number is requested for installation.

If the serial number validation fails, the plugin will show that in the Effectrix About
Screen.


BACK

TO TABLE OF CONTENT



7


### EFFECTRIX Structure

#### The Header

##### Global Presets

You will find the Global Presets in the upper left corner of the plugin.

The Global Presets recall all Effectrix settings, including all
sequences, subsequences and effect settings.

The top line shows the current preset name and offers different file operations.

You can add your own preset folders, subfolders are not allowed.

Find the Effectrix presets in Documents/Sugar Bytes/Effectrix/Presets.


BACK

TO TABLE OF CONTENT



8


##### About Screen

Click on the ABOUT Button to open the About Screen.


In the About Screen you have some useful information and settings as follows:


Version
Current version number.


Open Manual
Start the Effectrix manual from here and visit the Sugar Bytes website to look for
updates for example.


Master Mix Curve
The Mix control offers two curves in the About Screen. Linear mode for a linear blending
between dry and wet signal, in this mode the audio level might be a bit too weak at
50/50. The EPL mode (Equal Power Law) cares for a stronger sound at 50/50 mix.
Follows the amplitude of the incoming audio signal to produce a control curve.


Retrigger On Wraparound
If a sequencer step goes over the whole sequence length, the effect will be retriggered
at the first step.
Using this feature, internal envelopes, Loop startpoints etc. will be retriggered.


Serial Number
Your serial number is shown here, along with its validation status.

##### Bypass


The BYPASS button deactivates Effectrix. This button is saved with presets,
but cannot be automated.

BACK

TO TABLE OF CONTENT


9


#### The Effect Sequencer

Now let´s start with the deeper stuff, the Effectrix sequencer:

##### Tempo


Effectrix runs at your host bpm, using the Tempo controls you can divide the host
tempo, so that Effectrix runs at /32, /16 or even at triplet speed. That way you can
determine the actual resolution of the 32step sequencer.

##### Swing


With the swing control you can let the Effectrix sequencer swing along with your host
sequencer. The swing actually delays
each second note, so using swing makes only sense when the Tempo control is set to
the resolution of your host sequencer.

##### Trigger By MIDI


The sequencer has two inbuilt clocks. It can run along your songposition, or it can be
fired with a MIDI note, only applying the effect sequence as long as you hold a note.
Activate "Midi Trigger" to trigger the sequencer with MIDI notes.


BACK

TO TABLE OF CONTENT


10


##### Use Pattern Keys

This setting activates the 12 subpatterns. A little keyboard will appear, it shows the
current note and you can use it as well to call a subpattern with the mouse. Right
beside the keyboard the current pattern number (1-12) is displayed.
The pattern keyboard can be automated with host automation,
so you can call patterns without MIDI as well.

##### Copy/Paste Buttons


When you work with the subsequences, it´s very convenient to use the COPY/PASTE
system. Hit the C button to copy the whole sequence. Then choose another sequence
(with a MIDI note or just by clicking into the little screen keyboard) and hit P to paste
the sequence onto the chosen key. Using COPY/PASTE you can easily create variations
from existing material.

##### Chaos Button


Press this button to create chaos in the pattern sequencer. Random steps will be
created every time you hit this button.

##### Init Button


This button completely erases all sequences, also the subpatterns, so you can create
new sequences from scratch.

##### Loop Bar


Use the Loopbar on the top of the sequencer to define your own playback loop. Pick it
on the edges to resize it, pick it in the middle to move it.


BACK

TO TABLE OF CONTENT


11


##### Tracks

Each effect has its own sequencer track. The little cross-button erases the sequence on
this track. The little ON-button can bypass the effect.


Step Handling

###### Draw sequence steps into the sequencer matrix with left click/drag. Erase steps with a double-click on the step. Move a step by grabbing it´s center. You can then move the step anywhere within its

effect track. Steps cannot be moved between different effect tracks.

###### Resize a step by grabbing it´s ends. The red part of Effectrix includes the actual filter

section.

##### Modulation Sequencer


Each effect has two modulation sequencers (A and B).

These can be assigned to all effect parameters giving you another dimension for
creating life within your effect sequences. You can also record knob movements to it,
turning the knob with the mouse or via MIDI / automation.


BACK

TO TABLE OF CONTENT


12


A/B
Use the A/B button to select one of the two sequencers.


ASSIGN
The ASSIGN menu is used to assign a knob for being modulated or recorded with the
selected modulation track (A or B).


SMOOTH
The SMOOTH control will turn the stepped modulation into a smooth modulation curve
with a lag time up to one second.


REC
The REC button activates recording for the assigned knob.
While REC is enabled, the assigned knob will not receive modulations until REC is
disabled.


RND
The RND button creates a random sequence.

#### Effect Controls


Below the sequencer you find the Effects section.
Each effect has it´s own color and it´s own page.

The effect page is called with a click into it´s track, also when editing it´s sequence it will
be called, so you always see the effect which is currently edited in the sequencer.

Nearly all effects have the same DRY/WET mix system, using
an envelope (triggered by the sequencer step) which gives you the possibility to fade in
and out effects using the ATTACK and RELEASE controls. So when a sequencer step is
reached, it fades in according to the Attack time, then stays at the MIX level. When the
step has ended, the effect fades out according to it´s release time.

Delay and Reverb have a slightly different system. Here you have no DRY/WET mix but
individual DRY Level and WET Level controls which results in ideal control of the audio
level.
The effects are running in series, from top to bottom, so first the XLOOP works your
audio, feeding it´s output signal into the LOOP, which feeds it´s output into the
Scratchloop.This gives you crazy possibilities from relooping looped stuff up to creating
complex grainclouds which leave no clue what the initial material sounded like.

BACK

TO TABLE OF CONTENT


13


##### Effect Presets

Each single effect has it´s own preset system, so its very easy to store and recall your
favorite settings.

#### MASTER


In the MASTER section you can set the Master Level and the Master Mix which blends
the incoming clean signal with the Effectrix output signal. The Mix control offers two
curves in the About Screen. Linear mode for a linear blending between dry and wet
signal, in this mode the audio level might be a bit too weak at 50/50. The EPL mode
(Equal Power Law) cares for a stronger sound at 50/50 mix.


BACK

TO TABLE OF CONTENT


14


#### EFFECTS

##### X-Loop

For Effectrix we developed a more advanced looptool called XLoop. It changes loopsize
and pitch over time and includes an envelope for shortening the loop.


SIZE
Defines the size of the looping buffer. It works in tempo values, so you can easily decide
how long the loop will be.


ENVELOPE
Cuts the loop short, so that only the beginning of the loop remains and silence takes
over.


SIZE CHANGE
A bipolar control. Negative settings make the loop size getting smaller over time.
Positive settings let the size grow over time.


PITCH CHANGE
A bipolar control which drops or rises the loop pitch according to its positive or negative
position.

##### Loop


A usual looper which repeats it´s buffer according to it´s loop size.


SIZE
Defines the size of the looping buffer. It works in tempo values, so you can easily decide
how long the loop will be.


XFADE
Fades the loop ends to create smooth loops, higher settings mix so much material that
the sound becomes weird and supersmooth.

BACK

TO TABLE OF CONTENT


15


SPEED
The Speed knob defines the speed of the LOOP.


DECAY
Fades out the loop at the given time. Using this feature you can make the sound vanish
before the step end is reached, giving you the possibility to create stuttering loops
using several short steps.

##### Scratchloop


Another innovative looper developed especially for Effectrix.
It plays the loop forward and backward like scratching a vinyl record. You can have
different speeds for fwd and bwd spin and individual slopes for the spinning change
between fwd and bwd and vice versa. This a very complex effect where all parameters
interact with each other, opening new worlds of scratching your audio signals.


SIZE
Defines the size of the looping buffer. It works in tempo values, so you can easily decide
how long the loop will be.


FWD SPIN
Controls the FWD playback speed.


FWD SLOPE
Controls the FWD playback speed curve. Actually this setting emulates the different
acceleration styles of the scratching hand.


BWD SPIN
Controls the BWD playback speed.


BWD SLOPE
Controls the BWD playback speed curve. Actually this setting emulates the different
acceleration styles of the scratching hand.

##### Reverse


A looper that plays always backward. It’s very simple, your audio will play backward as
long as a Reverse step is active.

BACK

TO TABLE OF CONTENT


16


SIZE
Defines the size of the looping buffer. It works in tempo values, so you can easily decide
how long the loop will be.


FADE
Fades the loop ends to create smooth loops, higher settings mix so much material that
the sound becomes weird and supersmooth.


DECAY
Fades out the loop at the given time. Using this feature you can make the sound vanish
before the step end is reached, giving you the possibility to create stuttering loops.

##### Stretch


A classical timestretcher which can slow down the audiosignal without changing it´s
pitch. Due to the fact that we work with realtime audio, it´s not possible to speed up the
audio signal because we don´t know the audio material of the future.


SPEED
Turn down the control to turn down the speed.


TEMPO-RELATIVE
Introduces a stepped speed mode where the
stretching always uses values relative to your bpm. That way your stretched beats will
always be in sync.


GRAINSIZE
Defines the size of a time window used for granulizing the audio signal. This control
provides you with different granular flavors.


FADE
Smoothes the granulizing of your audio material and gives you a choice between a
rather harsh or rather soft sound.


BACK

TO TABLE OF CONTENT


17


##### Vinyl

Another Scratching tool but with a different method. This effect gives you the sound of
scratching or stopping a record with your hands. You get that classical chicky-wicky
sound immediately.


TEMPO
The actual scratching speed / the time needed for slowing down the record until it
stops.


SIZE
Determines how much room is taken for scratching. Smaller settings just scratch a
small range of the audio material, larger settings scratch more contents, resulting in a
more aggressive scratch sound.


STOP MODE
Changes the VINYL Effect so that it stops the record. The SIZE parameter is not
required here and so it´s greyed out.

Since no looping is used here, always the current audiosignal becomes scratched and is
not repeated.

##### Tonal Delay


One of the most innovative effects created by Sugar Bytes.
A short delay is used to tonalize/synthesize anything fed into it.

You can make your drums play melodies, repitch harmonic signals and create stunning
mutations out of anything that makes sound in any way.


TUNE
Determines the note applied to your signal. It really makes sense to remote this knob
with the internal modulation sequencer or via MIDI/automation.


FEEDBACK
Controls the intensity and sustain of tonalisation. Higher settings give you a clearer
tone and a stronger signal.


BACK

TO TABLE OF CONTENT


18


WIDTH
Introduces stereo imaging for a larger sound.


HIGHPASS
Cuts off lower frequencies to avoid rumble and create a rather light tone.


LEVEL
Higher feedback settings raise the output level, so this control can be used to adjust
the output level.

##### Stutter


An amplification effect, useful for enveloping, gating and panning effects.

Two sequencers are running along your clock. The upper one starts an envelope at the
given amplitude, the lower one controls the stereo pan.


TEMPO
Determines the playback speed of LEVEL and PAN sequencer.


ATTACK
Belongs to the amplitude envelope, triggered by the Level sequencer and controls the
level-fade-in-time when a sequencer step starts the envelope.


DECAY
Belongs to the amplitude envelope, triggered by the Level sequencer and controls the
level-fade-out-time of the step.

##### Crush


Made to destroy. A first class sounding bitcrusher, sample rate reducer and distortion
effect.


BITCRUSH
Reduces the bitdepth and so introduces silver rain and crushed ice.


BACK

TO TABLE OF CONTENT


19


SAMPLERATE
Reduces the sample rate using an advanced technique which introduces new flavors
and octaving effects.


DISTORTION
Warm and deep, strong and wild.

##### Filter


The essence of Sugar Bytes´filter technology.
Contains 4 Filter Types known from our WOW Filterbox,
including the famous Vowel Mode which makes your audio talk. Also an AR envelope
and envelope follower are included for classic filter sweeps.


CUTOFF
Determines the filter frequency. In Vowel Mode this control selects vowels (A, A:, AE, E,
I, O, OE, UE, U).


RESO
Controls the Filter resonance, in Vowel Mode higher settings give you a clearer vocal
sound.


ENV PEAK
Determines the target-value of cutoff-modulation introduced by the internal envelope
and envelope follower. Modulation starts at the Cutoff frequency, reaches the Env Peak
value and goes back to the Cutoff frequency.


ATTACK
Fade-in-time of the envelope/envelope follower.


RELEASE
Fade-out-time of the envelope/envelope follower.


FILTERTYP
Choose from 4 filtertypes. The classic HP/BP/LP are included in 24db depth. Also a
strong COMB filter is included for stunning vowel- and micodelay sounds.


VOWEL MODE
Use that mode to make your audio talk. The cutoff control is then used to select the
vowel frequencies.


BACK

TO TABLE OF CONTENT


20


ENV TYPE
Select the envelope used for modulating the cutoff frequency according to Env-Peak,
Attack and Release settings. Envelope is a classic AR envelope started when a
sequencer step is reached. Env Follow creates an envelope from the transients of your
audio signal.

##### Phaser


The good old 70ies sound, deep and wide phasing at it´s best.


RATE
Phasing speed, always in sync to your song tempo.


STAGES
Number of Phaser stages, running in series.


DEPTH
Intensity of the actual phasing sound.


FEEDBACK
Introduces a stronger sweeping.


WIDTH
Stereo widening and left/right phasing offset.

##### Chorus


The classical detuning effect, makes it all bigger and wider.


RATE
Chorus speed, always in sync to your song tempo.


DEPTH
Chorus intensity, goes from slight widening to extreme detuning.


FEEDBACK
Introduces a flanger sound.


BACK


21


TO TABLE OF CONTENT


WIDTH
Stereo widening and left/right sweeping offset.

##### Delay


A usual Delay effect with synced delaytimes.


TIME
The delaytime, always in sync with your host tempo.


FEEDBACK
Determines how long the delayed signal will decay until it ends.


DIFFUSION
Introduces a slight mixup between left and right channel, for creating the impression of
a room.


WIDTH
Stereo imaging for a wider sound.


DRY LEVEL
Here you can control the level of the dry signal.


WET LEVEL
Here you can control the level of the wet signal.


BACK


22


TO TABLE OF CONTENT



23


##### Reverb

A usual Reverb effect.


ROOM
The roomsize, for bigger or smaller reverbs.


DECAY
Determines how long the reverb signal will last.


WIDTH
Stereo imaging for a wider sound.


HIGHPASS
Cuts off low frequencies to avoid rumble.


DRY LEVEL
Here you can control the level of the dry signal.


WET LEVEL
Here you can control the level of the wet signal.


BACK

TO TABLE OF CONTENT



24


### Host Integration

#### Logic

Use Effectrix as MIDI Controlled FX. Pick it up on an Instrument Track and choose it
from the MIDI Controlled FX list in the Plugins menu.


Then, in the Sidechain menu in the upper right corner, select the Audio track or Bus
that you want to use with Effectrix. Then, in the Logic mixer, turn down the level of the
audio track that you selected in the Effectrix Sidechain menu.

#### Live


Basically there are to 2 ways to work with Effectrix.
First way is to activate the 'trigger by MIDI' option.
Then Effectrix will run if you trigger it via a MIDI note.
If 'trigger by MIDI' is off, it will always run along with the host clock
but to trigger Effectrix via MIDI should give you the best timing.

That's how it works:
Please activate the 'use pattern key' option in Effectrix.
Set up an audio track and use Effectrix as effect.
Send MIDI to it using a MIDI track.
Select the Audio track which has got Effectrix on it in the MIDI TO dialogue of the MIDI
track.


BACK

TO TABLE OF CONTENT


25


Then switch to arrangement view and set MIDI Note events to trigger and select certain


So you can trigger the related key at the exact location you want.
*Effectrix is an audio effect, only!
You can send MIDI TO Effectrix, but Effectrix will only produce audio not MIDI.


BACK

TO TABLE OF CONTENT


26


#### Cubase

Make sure that the Effectrix.dll/Effectrix.vst3 (Win) or Effectrix.vst/Effectrix.vst3
(macOS) file is contained in Cubase‘s assigned VST Plugins folder. Load Effectrix as an
insert effect on an audio track or instrument track. Now create a MIDI track and choose
Effectrix as target for the MIDI track. This way you can trigger Effectrix with your MIDI
knobs and record controller movements in the MIDI track.

#### Pro Tools


Use Effectrix as effect.


Send MIDI to it using a MIDI track. Select the Audio track which has got Effectrix on it in


BACK TO TABLE OF CONTENT


27


#### Sonar

Depending on how you want to use Effectrix you have to configure it as 'soft synth' or
tempobased effect.


and open the plugin settings


Then configure it as synth
If you just want to let it run along with Sonar choose 'tempo based effect'


Plug it out. Plug it in an fx slot again but from the synthmenu


BACK

TO TABLE OF CONTENT


28


Then you will have a MIDI track assigned to it and from now on you can route a MIDI
track to Effectrix so that Effectrix can receive MIDI via this track.


Activate "Trigger by MIDI" to trigger the sequencer with MIDI notes.
To trigger the Patters with MIDI notes activate "Pattern Keys"

(If you should try to trigger a note which is out of the keys or haven't drawn a MIDI note
inthe Key Editor there might be no sound.)

BACK

TO TABLE OF CONTENT


29


#### Studio One

Go to the Studio One menu and choose Options, click on Locations, then VST Plug-Ins.


Click the Add button and select your VST
Plugin folder. Press OK then close and reopen Studio One. If you still don’t see your
plugin, go back into that screen and click
the “reset blacklist” button, then close
and open Studio One again.

Pick it up from the VST Effects list.
Create an instrument track and choose Effectrix as MIDI out target for that track.


BACK

TO TABLE OF CONTENT


30


### MIDI Remote

All relevant Effectrix parameters can be controlled via Host Automation.


All relevant Effectrix controls can be remoted via MIDI controllers.

You find the MIDI Learn function when you right click a control.

### MIDI Program Change


Create a Folder called 'Midi Programs' beside the Factory Preset folder.


Path should be like this:
Documents/Sugar Bytes/Effectrix/Presets/Midi Programs/


Put the preset you want to call in that folder.
You have to restart Effectrix after copying files into that folder in order to reflect the
changes.


All presets in the Midi Programs Folder can be called with MIDI Program Change
messages now.


BACK

TO TABLE OF CONTENT



31


### Questions? EFFECTRIX makes no sound

Are the level meters showing an Audio Signal?
If Audio In works, but Audio Out is silent, your filter setting might be filtering out all
audible frequencies (HP too high?, LP too Low?).

The Demo could be timed out or the serial number could be wrong. Both issues will be
displayed in the interface, left beside the Effectrix logo.

The Direction control of the Loop effect is set to zero. At zero speed, the audiowave
stands still and so will not move your speakers.

### Have I found a bug?


Please write to support@sugar-bytes.de

### Impressum


Sugar Bytes GmbH | Made of passion
Robert Fehse, Rico Baade | Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395 | Str.-Nr. 37/207/21266 | HR-Nr. HRB 124199 B
[info@sugar-bytes.de | www.sugar-bytes.com](mailto:info@sugar-bytes.de)


BACK

TO TABLE OF CONTENT


32


