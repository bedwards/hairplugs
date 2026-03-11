# THESYS

## User Manual



1


### Table of contents

##### About this Manual 5 What is Thesys? 5 Installation and Authorization 5

Installation 5
WINDOWS 6
macOS 6
Uninstalling 7
Authorization 7

##### Getting Started 8

Setting up Thesys 8
Getting Some Sound 8
Loading Presets 9
Routing to Another Instrument 9
MIDI File Drag and Drop 10

##### Host Integration 10

Cubase 10
Ableton Live 11
Studio One 12
ProTools 13
Sonar 14
Logic X 15
FL Studio 16

##### Control Section 18

Global Controls 18
Logo/About Screen 18
Open Manual 18
MIDI Activity Indicators 18
MIDI IN/MIDI OUT transposition 18
Transpose Mode 19
Synthesizer/MIDI Settings toggle switch 19
Sequencer Settings 19
Trigger By 19
Trigger Mode 20
Loop 20
Tempo Division Unit 20
Swing Amount 20
Action Section 21
Gate Time 21
Velo Gate 22


2


Looper 22
Slow Down 22
Retrigger 23
Half Speed 23
Manual Step 23
Mute 23
Start/Stop Button 24
Pattern Sequencer 24
on/off 24
Loop Bar 24
Pattern Change Speed 25
Pattern Select 25
Number of Repeats 25
Keyboard Control Section 25
Keyboard Control Quantization Value 27
Pattern Select 27
Action Section (Keys) 27
Pitch Transposition 27

##### Sequencer Section 28

Sequencer Preset 28
Preset vs. Pattern 28
Global Sequencer Controls 28
Global Shift 28
Copy & Paste 29
Random 29
Pattern Edit Selector 29
Common Controls and Functions 30
General Editing Features 30
Step Direction and Interval 31
Step Shift Control 31
Copy and Paste 32
Reset, Random and Mutate 32
Loop Bar 33
Global Sequencer Controls 33
Pitch 34
Root Key Set 34
Scale Selector 35
Recording Input Mode 35
Note Name Display 36
Lock 36
Velocity 36
Sequencer Area 36
Mute 36
Gate Time 37
Performance 37
Octave 38
Bend 38
Chord 38


BACK 38
Roll 39
Random 39
Modulation 40
Internal Modulation 40
MIDI CC number 41
On/Off Button 41
MIDI Value 41

##### Built-in Synthesizer 42

Synthesizer Preset Manager 42
On/Off 42
Oscillator Settings 43
Level 43
Pan 43
Waveform 43
Detune 43
Volume Envelope 43
Filter 44
Cutoff 44
Reso(nance) 44
Peak 44
Attack 44
Decay 44
Sustain 44
Release 45
Delay 45
Delay L(eft) Delay R(ight) 45
Feedback 45
Mix 45

Appendix 46
Scales 46
Chords 48

Impressum 55


### About this Manual

This manual includes a detailed reference guide as well as a Getting Started tutorial to
help you start laying down patterns right away. If you have a question that is not
[answered in the manual, please go to the Sugar Bytes Support Forum.](http://www.kvraudio.com/forum/viewforum.php?f=108)

### What is Thesys?


Thesys is an extremely powerful and intuitive MIDI sequencer, giving you control over just
about all aspects of your favorite MIDI devices. Use Thesys to create varied and organic
bass lines, screaming leads, pulsating chords, and organic pad sounds in the studio or on
stage. Sequence and send patterns of just about any MIDI data you want, not just pitch
and velocity. For example, you can include things like Program Change, Portamento,
Aftertouch, and any other MIDI CC in your sequences.


For live musicians, Thesys provides an extremely versatile palette of performance options
which can be triggered right from your MIDI keyboard: you can transpose, manipulate,
twist up, mutate, and mangle your patterns without even getting near your computer.


Thesys is a plugin which can be used with any major Windows or OS X VST or AU host.
This includes Cubase, Logic, Kore, and Ableton Live, among others.


No other MIDI sequencer plugin offers you the ease and power of Thesys. It is 100% MIDI
compliant and therefore provides the ultimate MIDI sequencing solution.

### Installation and Authorization

#### Installation


[Download (requires login) the latest version here.](http://www.sugar-bytes.de/account)


The standalone version and the manual will be installed into:


Windows: C:\Program Files\Sugar Bytes\Thesys
macOS: /Applications/Sugar Bytes/Thesys


Presets will be installed into Documents\Sugar Bytes\Thesys.


Do not move the Thesys presets after installation!


BACK
TO TABLE OF CONTENT


5


Default installation paths


WINDOWS


Default installation paths:


VST2 C:\Program Files\VSTPlugins
VST3 C:\Program Files\Common Files\VST3
AAX C:\Program Files\Common Files\Avid\Audio\Plug-Ins


macOS


The Audio Unit, the VST Plugin and the AAX Plugin will be automatically installed into the
correct folders.


Default installation paths:


VST2 /Library/Audio/Plug-Ins/VST/
VST3 /Library/Audio/Plug-Ins/VST3/
AU /Library/Audio/Plug-Ins/Components/
AAX /Library/Application Support/Avid/Audio/Plug-Ins


BACK
TO TABLE OF CONTENT


6


#### Uninstalling

In order to uninstall Thesys, please take the following steps:


Windows: Uninstall Thesys under Control Panel/AddRemove Software.


macOS: Here is the way to delete everything regarding Thesys


/Applications/Sugar Bytes/Thesys
/Library/Audio/Plug-Ins/VST/Thesys.vst
/Library/Audio/Plug-Ins/VST3/Thesys.vst3
/Library/Audio/Plug-Ins/Components/Thesys.component
/Library/Audio/Plug-Ins/Components/Thesys MidiFX.component

/Library/Application Support/Avid/Audio/Plug-Ins/Thesys.aaxplugin
~/Documents/Sugar Bytes/Thesys
~/Library/Preferences/com.sugar-bytes.Thesys.plist


~ means: /Users/YOURLOGINNAME (your home folder)


(Please note that since OSX 10.7.x the library folder is a hidden folder.


Therefore please use the "Go To Folder" menu and then enter ~/Library.)

#### Authorization


The serial number is requested for installation.

If the serial number validation fails, the plugin will show that in the Thesys settings page.


BACK
TO TABLE OF CONTENT


7


### Getting Started

This section will show you how to get a few sounds out of Thesys to give a feel for how
things work. All of the functions mentioned in this section are described in detail in the
sections in this manual which then follow.


Thesys is a plugin, which means it will only work within a host environment. After
installation, you should be able to find Thesys in the VST (Windows & macOS) and Audio
Unit (macOS only) folders in the host application you are using.


While the VST standard allows full functionality of MIDI sequencers like Thesys "out of the
box," the Audio Unit (AU) format requires a workaround which is described below. Even
without the workaround, you should be able to produce sound from Thesys using its
internal synthesizer. If have a choice between AU and VST formats — when using Ableton
Live on macOS, for example — it will be easiest for you to use the VST version.
To begin with, this is exactly what we will do.

#### Setting up Thesys


Getting Some Sound


In this example, we'll get Thesys going using Ableton Live (macOS) as our host. Insert or
drag the Thesys VST onto a MIDI channel. If you do not know how to do this, please
consult your host application manual.


To start with, make sure the outputs of the MIDI channel are routed like any other
software instrument so that you can hear the audio on your speakers or headphones in
your studio.


The first time you open an instance of Thesys in your host, the Default preset will be
shown. Click on the Start button in the lower right corner. The sequencer engine begins
to run, but you won't hear any sound because the Default preset's Velocity sequencer is
filled with 0 values. Draw or click in the Velocity sequencer area and you'll hear some
16th notes.


Create a more melodic pattern by changing the values in the Pitch Sequencer. You may
want to slow the step speed down by selecting eighth notes instead of sixteenth notes
with the Tempo Selector in the Sequencer Settings section.


In the Default preset, the Sequencers' loop lengths are all set to 8 steps. To keep things
all synced up, in the Sequencer Settings section, set the "Loop" toggle to global. This just
means that all the different sequencers will all have Loop lengths which will be identical
to that of the Pitch sequencer at the very top. Grab the right-hand edge of the Loop Bar
and drag it out towards the right to create a longer loop (try 16 steps, for example). For
the additional steps, you'll have to draw in some Velocity Sequencer steps in order to get
sound for the whole length of your pattern.

BACK
TO TABLE OF CONTENT


8


Now try playing with the Gate Time Sequencer. By default, each step is set to a value of
1.0, meaning that the note will be "on" for the duration of the step. To understand how
the Gate Sequencer works, slide a few steps way up to the maximum of 4.0. If there are
consecutive steps with this value, you'll hear overlapping notes, because steps will be
triggered while the gate is still "open" for previous notes. This works with the internal
synth as well as any other polyphonic synth being driven by Thesys.


Pull some other steps way down and notice the short impulse-like sounds which result.
Using intermediate values closer to 1.0 will give your lines more variety and make them
sound more organic.


Once you've tweaked your pattern a bit, try out some Actions:


With the sequencer engine running, click on the Looper in the Action Section. Adjust the
length of the Looper with the Steps knob. Try Half Speed, Mute, and the other Actions to
get a feel of the some of the performance possibilities.


Loading Presets


At the top of the Thesys Window (to the right of the Thesys logo), you'll see the current
preset name. Click on the name to open the preset chooser to choose a preset from
within one of the preset categories.


The folder containing the presets is located in your Applications folder under Sugar
Bytes. The Sugar Bytes folder will have an Thesys folder where you'll find "Content." This
is where the presets are located. Once you load a preset from this folder, you will not
have to re-point Thesys to find any other presets; it will open automatically to this folder
when you click on "Load Preset" in the Preset Manager at the top of the Thesys window.


To the left and right of the Preset Manager are arrows allowing you to step through
presets consecutively.


Routing to Another Instrument


The fun with Thesys really begins when you start using its MIDI output to drive other
instruments. The first thing we'll do is turn off the internal synthesizer. To do this, open
the synth by clicking on the Loudspeaker icon just to the right of the Velocity Sequencer
to toggle to the Synthesizer section. Just under the Sugar Bytes logo in the top right
area, click on the on/off switch to turn the Synthesizer off.


Create another MIDI channel in Live and then insert your favorite soft synth. In this case,
we're using Sugar Bytes' own Unique.In the MIDI channel where Unique (or the synth of
your choosing) is plugged in, set the "MIDI From" drop down to the channel containing
Thesys. In the Post/Pre FX drop down menu just below, also choose Thesys. You should
now be hearing your pattern being played! You can open other MIDI channels with other
soft synths (or samplers) and set similarly. This way you can achieve layers of sounds, all
triggered by Thesys.

BACK
TO TABLE OF CONTENT


9


Midi File Drag and Drop


The Midi data generated by Thesys can be saved to a Midi File. Just drag and drop the
« Hand/Note » Icon to a Midi track in your sequencer or to your desktop and the file will
be created. Use the control below to set the length of the Midi file. The maximum length
is 64 bars. Since the file will be written on the fly, Thesys will not produce sound while the
file is generated.

### Host Integration

#### Cubase


In order to route the midi output of Thesys to other virtual instruments
go to devices->VST Instruments.


Then choose Thesys and in a further instance the synth you want to control.


Choose Thesys as midi input in the MIDI track for your synth (here Cyclop)


BACK
TO TABLE OF CONTENT


10


#### Ableton Live

The workaround with Live is quite simple. Your setup should look like this.
In the receiving track of your target instrument make sure to select Thesys twice as
input.


BACK
TO TABLE OF CONTENT



11


#### Studio One

Create an Instrument track and load Thesys as insert on that track.


In order to route the midi output of Thesys to other virtual instruments choose the synth
you want to control in a further Instrument Track.


Then set up Thesys as midi input and activate record in the Instrument Track for your
synth (here Unique).


BACK
TO TABLE OF CONTENT


12


#### ProTools

In order to connect Thesys to another instrument in Pro Tools, create an Instrument track
and load Thesys as insert on that track.


If you only want to hear the sound of the synth of your target instrument please


BACK
TO TABLE OF CONTENT


13


#### Sonar

Insert Thesys as a Soft Synth. Make sure to activate the Midi output option in the Insert
Soft Synth Options Box.


BACK
TO TABLE OF CONTENT



14


#### Logic

Choose Thesys as an MIDI FX-Instrument from the MIDI FX dialogue of a Software
Instrument track.


If you are using an older version of Logic than LogicX as a host, you won't be able to
directly trigger external synths. The AU format does not send and receive MIDI data "out
of the box," but alternatively you can at least use the MIDI Drag and Drop feauture.


BACK
TO TABLE OF CONTENT


15


#### FL Studio

Plugin Thesys in the mixer section of your audio track (here it is insert1)


To control Thesys via midi you have to setup a midi out channel.


Go to Channels->Add one->More...


Doubleclick on MIDI Out to setup a midi out channel.



16


Make sure to setup the correct input and output port in the Thesys midi section of
Thesys.


BACK
TO TABLE OF CONTENT



17


### Control Section

#### Global Controls

The Global Controls section consists of all parameter controls in
the dark area located outside of the main Sequencer window.


Logo/About Screen


Click on the Sugar Bytes or Thesys logos in the upper left and right-hand corners of the
interface in order to enter or check your serial number or find out which version of Thesys
you are using. The About screen also contains the IAC MIDI driver selector (for macOS
versions only). Controllermaps which contain the MIDI controllers assigned to Thesys, can
be loaded and saved here.


The “Ignore Program Change” Option allows you to filter incoming Program Changes to
avoid unwanted preset changes in Thesys.


With “Zoom“ you can adjust the Thesys Gui to your monitor screen size or click into an
empty area in Thesys, then hold down the Ctrl key and press the + to increase the size or

- to decrease the size.


Open Manual


Clicking on the Open Manual button automatically opens the Thesys manual which was
installed with the software. The manual is located within the Thesys application folder
and can be copied or moved elsewhere. Keep in mind, however, that the manual cannot
be automatically opened with the Open Manual button if it is moved from the original
location.


MIDI Activity Indicators


The MIDI Activity Indicators light up when MIDI is either received by or transmitted from
Thesys.


MIDI IN/MIDI OUT transposition
Just under the MIDI Activity Indicators, the Transposition controls allow you to transpose
incoming MIDI notes as well as the MIDI notes transmitted by Thesys. MIDI IN
transposition is useful for setting up your controller keyboard for pattern selection and
action triggering. Click and drag to change values.


BACK
TO TABLE OF CONTENT


18


The MIDI OUT octave transposition moves the outgoing MIDI notes up or down up to two
octaves. Underneath the octave transposition control, step transposition allows you to
move pitches up to 12 half-steps (semi-tones) up or down.


Transpose Mode


The Transpose Mode switch toggles between ROOT KEY and IN SCALE and determines if
incoming MIDI notes transpose the pitch sequence by just moving the root key
chromatically (set by the Root Key Control) or are forced into the closest possible note on
the scale (determined by the Scale Control).

#### Synthesizer/MIDI Settings toggle switch


Click on the speaker icon (on the right edge of the Pitch Sequencer) to toggle between
Synthesizer controls and Sequencer Global Settings panel.

#### Sequencer Settings


Trigger By
The Trigger By switch toggles between the Pattern Keys and Pitch Keys as input triggers.
In other words, you can set Thesys into motion with either the pitch keys or the pattern
keys on your external MIDI keyboard. The keyboard mapping of the pitch keys and
pattern keys is shown at the lower edge of Thesys in the Keyboard Control Section (see
below: "Keyboard Control Section"). You can also trigger Thesys by simply clicking on the
keys.


BACK
TO TABLE OF CONTENT


19


Trigger Mode


This three-state toggle switch determines how Thesys responds to a trigger signal. The
first option is Host. This means that Thesys is slaved to the host clock and will start when
the host clock is started.


Note On triggers (starts) Thesys as soon as a note is played. Thesys continues to play as
long as the note is held.


Note Toggle toggles (starts and stops) Thesys with any incoming MIDI note. The first note
starts the sequencer and the next incoming note stops it.


Loop


This setting determines if all sequencers have individual Loop Bars (Individual), or if they
share the same loop bar (Global). When Global is chosen, the loop from the Pitch
Sequencer is used as the Global Loop.


Tempo Division Unit


Choose between ten different note values to determine the step rate. The quarter note
will advance the sequencer one step per (quarter note) beat; an eighth note rate is twice
as fast and a half note half as fast. The default setting is the eighth note. This means that
at a clock speed of 120 BPM, the step speed will be at an eighth note pace, or at 240
steps per minute. Setting at the half note value (also at 120 BPM) would then result in a
rate of 60 steps per minute. Thesys can run in triplet divisions as well.


Swing Amount


This slider determines the amount of swing which varies from completely straight (even)
at the far left, to a dotted rhythm (75%/25% relationship) at the far right. Pulling the
slider to the half-way point results in a ternary (triplet) swing.


BACK
TO TABLE OF CONTENT


20


#### Action Section

The Action Section is a fast and intuitive way to "mutate" your patterns, either on stage
or in the studio. All of the functions in the Action (Button) Section correspond to those in
the Action (Key) Section, found along the lower edge of the Thesys GUI. The main
difference is that the Action Key Section shows a keyboard map allowing you to "play"
the actions on your MIDI keyboard controller, while the Action Button Section gives you
mouse and MIDI CC control.
In addition, the Action Section provides four additional parameter adjustment knobs
corresponding to certain Actions (see below).
Each action button (and key) behaves as a "push-on" switch. In other words, the
particular Action is only active as long as a button or key is pushed or played. When the
button or key is released, the Action stops and the sequence continues as usual.


Gate Time


The Gate Time button immediately forces the gate time (length) to a single, uniform
value for all steps. If this button is not activated, then the gate time of each step is
determined by the height of that step in the Gate Time Sequencer. When you click on the
Gate Time Button (or play the corresponding key on your MIDI keyboard controller), then
the gate times of all the steps will be exactly the same as long as you push the button (or
hold down the key). The Gate Time value is set with the Time knob to the left of the Gate
Time button. Extremely short gate times (staccato) can be created by turning the knob
completely to the left. Legato gate times — resulting in a connected melodic line — are
achieved by turning the knob to the right of the center position.


BACK
TO TABLE OF CONTENT


21


Velo Gate


When pushed, the Velo(city) Gate Action only triggers notes which are higher than the
velocity set at the Threshold knob to the right of the Velo Gate. Notes with a velocity
setting (determined by the Velocity Sequencer) below the threshold value will not be
triggered and the step will be "empty," behaving as if there was no velocity trigger at all.
This is a good way of thinning out and "relaxing" your pattern for a while.


Looper


As its name implies, this Action loops a section of a sequence. The length of the loop (in
steps) is set by the Steps knob. When the Looper is activated, the Loop cycle begins on
whichever (Pitch) step happens to be active at that time. Once the number of steps is
reached, the loop begins again. This continues until the Looper button (or key) is
released.


Upon release, the sequence continues where it would have been if the Looper had not
been activated. In other words, instead of just finishing the loop and continuing forward
in the sequence, releasing the Looper brings the sequence position right back in step.
This can be very useful for jumping in and out of melodic riffs or harmonic progressions
without missing a beat.


Slow Down


Think of the Slow Down Action as a handbrake for your sequence. When activated, it
progressively slows the speed of the sequence down. The rate of slowing is set with the
Slew Rate knob. Turn the knob to the left for a very gradual and long "decelerando" and
turn to the right for quicker slow downs.

BACK
TO TABLE OF CONTENT


22


Retrigger


Use the Retrigger Action to retrigger all the sequencers at once. Retrigger forces all the
sequencers back to their first step while maintaining the step speed. When you release
Retrigger, the sequences continue where they would have been if they had not been
retriggered. This behavior is similar to that of the Looper Action.


Half Speed


As its name implies, Half Speed doubles the length of time between each step for all
sequencers and creates a half-tempo feeling.


Manual Step


This action button overrides the clock and triggers the sequencer one step at a time.
Activate the button to stop the sequence; you can then manually move forward in the
sequence using the Pattern Keys and the Pitch Keys one step at a time.


Mute


The Mute Action mutes all notes, without stopping the sequencer. This is the same as
sending a series of zeroes from the velocity sequencer. As with Looper and Retrigger, the
sequencers continue to run when Mute is activated.

BACK
TO TABLE OF CONTENT


23


#### Start/Stop Button

The Stop/Start Button turns the internal sequencer clock on and off. When lit, it indicates
that either the internal or the host clock is running and the sequencers are on.

#### Pattern Sequencer


This module is the top-level sequencer which determines which pattern will be played
and how long that pattern will be played.


A pattern consists of all sequences (Pitch, Velocity, Gate Time, Performance, Modulation)
and their settings.


You can choose from the 16 patterns in the Pattern Sequencer, which plays up to 8
different patterns in any order. In addition, each pattern can be repeated up to 16 times
before moving on to the next one.


You can think of each pattern as a kind of snapshot of all the sequences visible in the
Thesys window at any one time.


on/off


When off, the currently displayed pattern will simply be looped continuously, without
switching to another pattern. When activated, the Pattern Sequencer steps through the
patterns determined by Pattern Sequencer Parameters:


Loop Bar


Determines the total length of the Pattern Sequencer sequence. As with any step
sequencer, after playing the last step in its sequence, the Sequencer will loop back to the
beginning and continue playing through the pattern steps in order. The Pattern Length
bar can be extended to the left or right and moved from the center, depending on the
position of the mouse pointer.


BACK
TO TABLE OF CONTENT


24


Pattern Change Speed


The note value input of the Pattern Speed Control determines how long a pattern is
played before either repeating (see "Number of Repeats" below) or moving on to the
next Pattern. Setting this value to a quarter note (one beat per change) will result in
extremely frequent Pattern changes (at BPM=120, this would be twice per second!). In
most cases, you will probably set this to at least a whole note (four beats per change) or
more. The maximum value is four whole notes = 16 beats.


Pattern Select


Pattern Select determines which Pattern is played on that particular step. Patterns can
be played and repeated in any order. This makes it possible to set up repeating song
structure elements (refrains, bridges, choruses, breaks, etc.) in your performances or
productions.


Number of Repeats


You can repeat a Pattern step up to 16 times. With a low Pattern Change Speed (see
above) and a large number of repetitions, Patterns can be made to run a long time before
moving on to the next Pattern step.

#### Keyboard Control Section


The Keyboard Control Section offers you extensive live-performance-oriented control
over Thesys. Here you can select a Pattern, trigger an Action, or transpose sequences up
or down by hitting the corresponding key on your MIDI keyboard/controller. The keys can
also be triggered by clicking on them with your mouse.Note that the Keyboard Control
Section is split into three distinct key ranges, each with a different function:


Pattern Select, Action Section, and Pitch.


There are two keyboard mappings available. Select the keyboard mode with the triangle
icon above the keyboard. The standard mapping offers all Patterns and Actions and a +/12 seminote transpostion zone.


The extended Pitch range offers transposing by +/-24 seminotes. Pattern- and Action
Keys are still available, 2 octaves below the standard mapping. You can shift these
control keys up or down your keyboard, depending on the MIDI In transpose control in
the Global MIDI Settings section of Thesys. You might consider routing a dedicated
keyboard through an unused MIDI channel into Thesys so that playing notes (melodies,


25


chords) on your master keyboard don't affect the control aspects of Thesys.


BACK
TO TABLE OF CONTENT



26


Keyboard Control Quantization Value


Here you can choose a quantization value for Keyboard Control input. For example, if you
want to trigger the Looper, but make sure it starts right on the beat, choose the quarter
note symbol. Or, if you want to transpose your sequence at the beginning of the measure
and don't want to miss a beat, set the value to whole notes.


Pattern Select


Each of the sixteen keys in this range corresponds to one of the sixteen Patterns. Play the
corresponding key on your MIDI controller to trigger or change Patterns. As with all the
other keys on the Keyboard Control Section, you can also click them with your mouse.


Pattern Select should not be confused with the Pattern Edit Selector (see above) which is
for editing patterns, not selecting them to play.


Action Section (Keys)


The Action Section of the keyboard shows the keyboard mapping of the Action Keys on
your MIDI controller/keyboard. For a detailed description of each Action, see the Action
Section description above.


Pitch Transposition


In addition to selecting Patterns, triggering Actions, and Transposing, the keyboard can
also be used to start or stop the sequencer. You can use the Pitch Transposition keys (hit
C3 or "0" to start/stop without transposition) or the Pattern Select keys to do this
depending on the setting of the "Triggered By" switch in the Global MIDI Settings section
(see above).


BACK
TO TABLE OF CONTENT


27


### Sequencer Section

#### Sequencer Preset

The Sequencer Preset Manager located at the very top of the Sequencer area of Thesys.
Here you can load, save, and step through presets (using the arrow buttons). Each preset
can contain up to 16 different patterns. In addition, a preset contains MIDI Settings and
Action Section knob settings (Time, Threshold, Steps, and Slew Rate).


All other parameters are stored in individual Patterns within the preset.


Note that the Synthesizer Section has its own Preset Manager for loading Synthesizer
presets (see below) and works independently from the Sequencer Preset Manager.

#### Preset vs. Pattern


It is important to be clear on the difference between Sequencer Presets and Patterns.
While Presets represent the highest level of the "parameter hierarchy," you can change
practically all parameters of the Sequencer Section by changing Patterns.


This is because each Pattern contains the information stored in the five sequencers:
Pitch, Velocity, Gate Time, Performance, and Modulation (see above: "Pattern
Sequencer"). In addition, a Pattern contains the root key, scale, sequencer play direction,
master tempo settings, modulation CC assignments, and the swing factor. All of these
parameters can change when changing from one pattern to another (either by manually
keying the change or by using the Pattern Sequencer). This gives you an immense
amount of real-time control and expressive possibility over your music.

#### Global Sequencer Controls


Global Shift


The Global Shift button moves the steps located within the corresponding sequencer's
Loop either left, right, up, or down (for changing Loop length, see below).


BACK
TO TABLE OF CONTENT


28


Copy & Paste


The Copy button copies the entire sequence. After copying, choose another preset slot,
then press the paste button.


Random


The Random button creates a complete random situation.
The Min/Max controls define the randomize amount. If Max is set lower than Min, so
values will be created within the difference.


Pattern Edit Selector


All the information contained in the five sequencers can be stored as a Pattern. Up to
sixteen Patterns can be stored in a single preset.


The Pattern Edit Selector allows you to edit each of these patterns individually. Click on
the Pattern you wish to edit (the Pattern Edit Selector button for that Pattern turns blue)
and make the desired changes. When you finished editing, click on the Pattern Edit
Select Button again. Once you have created different Patterns, you can trigger them
automatically with the Pattern Sequencer (see below). You can also trigger different
Patterns manually by clicking on the Pattern Select on the Keyboard Control Layout (at
the bottom of the Keyboard) or by playing the corresponding keys on your MIDI
keyboard. Use the Pattern Edit Selector only for editing patterns, not for triggering them
(because of the toggle-editing behavior). For Pattern triggering, use the Pattern Select
keys in the Keyboard Control Section by either clicking on them or using your MIDI
keyboard controller (see above: "Keyboard Control Section").


BACK
TO TABLE OF CONTENT


29


#### Common Controls and Functions

General Editing Features


A number of editing features have been implemented for the sequencer areas:


   - Click and drag on a step to create or change a value. Alternatively, you can use
your mouse scrollwheel to change values in individual steps.


   - Shift-click on a step to edit for finer adjustments.


   - Cmd-click (OS X) or Ctrl-click (Windows) a step to create a straight line across all
other steps.


   - Alt-click and drag a step to move the whole sequence up or down.


   - Rightclick a step to assign a CC via MIDI Learn


   - The performance section features advanced mousing modes as well:


   - Click on a step or step area to create or change a value.


   - Right-click to delete steps. Right-click and drag to delete consecutive steps.


   - Shift-click and move an active step to spread (copy) that value with the mouse.


   - Alt + left click to increase a step value; alt + right click to decrease the value.


   - Shift-Rightclick a step to assign a CC via MIDI Learn


BACK
TO TABLE OF CONTENT


30


Step Direction and Interval


Clicking on the Step Direction and Interval control opens up a drop-down menu with the
following choices:


Forward: Plays the sequence from left to right. This is the default setting.


Backward: Plays the sequence from right to left.


Random: Plays the steps in a random order.


Each 2nd: Plays every other step. For sequences with an even number of steps, only
steps 1, 3, 5... etc. will be played. For sequences with an odd number of steps, the first
run through the sequence will be as above (1, 3, 5... etc.), but on the first repeat, steps 2,
4, 6... will be played.


Each 3rd: Same as Each 2nd, but instead one out of every three steps will be played.


Each 4th: Same as Each 2nd and Each 3rd, but instead one out of every four steps will be
played.Note that if the Loop switch in the Sequencer Settings section is set to Global,
only the Pitch Sequencer gives you a choice of direction and interval, since in this case,
the Pitch Sequencer (and its Loop) act as a "Master Sequencer" for all the other
sequencers.


If you desire individual Step Direction and Interval control for each sequencer, then set
the Loop switch to "Individual."


Step Shift Control


The Step Shift Control moves the steps in the looped area one step forward (right), back
(left), up, or down. In the performance sequencer, you may only move the sequence
forward (right) or back (left).


BACK
TO TABLE OF CONTENT


31


Copy and Paste


Copies the steps in the looped area (as determined by the sequencer's Loop Bar (see
below). Use the Sequence Length Bar as a way of selecting the part of the sequence you
want to copy. Then, move the bar to the area of the sequence where you would like to
paste the copied part of the sequence.


This can be very useful in duplicating short riffs or patterns within the entire sequence.


A nice feature makes it easier to copy and paste several sequences at once:
The Pitch Sequencer, the Performance Sequencer and the Velocity, Gate Time, and
Modulation Sequencers work on individual "Copy & Paste Layers." This makes it possible:


1)to copy and paste the contents of Velocity, Gate Time and Modulation sequencers
between each other;


2)to copy and paste the Pitch, Performance and Velocity OR Gate Time OR
Modulation sequencers at once. Therefore just set the loop bar to define the
sequence range you like to copy, then hit copy in the Pitch sequencer, in the
Performance sequencer, and the Velocity Sequencer. Then move the loop bar to the
desired paste position and hit paste in Pitch, performance and Velocity. You will now
see that each sequencer content has been copied on its individual "Copy & Paste
Layer."


Reset, Random and Mutate


Reset (x) sets the Sequencer to its default value.
Random (dice) creates a completely randomized situation.
Mutate (arrows) changes existing values.


BACK
TO TABLE OF CONTENT


32


Loop Bar


The Sequence Loop bar is at the top of each of the five sequencers. It determines both
the length of the sequence in steps and the beginning and start steps.


The Loop Bar also serves as the selection to be copied and then pasted within any given
sequence (see "Copy & Paste" above).


Click and drag at the beginning or end of the bar to shorten or lengthen either end. Click
and drag in the middle of the bar to move the entire bar without changing its length.


In the Global Settings, you can choose between individual Loop Bars for each sequencer,
or a shared Loop Bar for all sequencers.


With the "Individual" setting in the Global Settings (Loop), rich patterns can be built
quickly by staggering the lengths of the different sequencers. For example, you could
have a five-step pitch sequence playing along with a seven-step gate sequence and an
eleven-step performance sequence; together, they would result in a quasi non-repeating
overall pattern. In addition, the "Individual" setting makes it possible to have one
sequencer running forwards, another backwards, and yet another in random mode or
skipping every other step, for example.


Global Sequencer Controls


The four Global Sequencer Controls are at the bottom left of the Sequencer window, just
above the Pattern Select of the Keyboard Control Section.


The Copy & Paste buttons work just the individual sequencer Copy & Paste buttons (see
above), except that the copying and pasting is for the all of the entire sequences, not just
the looped areas. In addition, you can copy and paste between presets and even
different instances of Thesys.


To Shift button moves all the sequences either one step to the left or one step to the
right each time you click on the corresponding arrow.


For real adventure, click the Global Random button !


BACK
TO TABLE OF CONTENT


33


#### Pitch

The Pitch Sequencer is the heart of any step sequencer, providing the pitch information
for the synth or sampler being played.


Each sequencer step gives you 12 increments of pitch increase or decrease with respect
to the root key. In a standard chromatic tone framework (12 half-steps in an octave), this
means that you have a two-octave range (+/- 1 octave), which corresponds to the range
in most standard step sequencers.


However, if you set the Mode to Major, for example, then an octave will be covered in
seven steps, not twelve. In this case, if your root key is C3, the highest note (without
octave transposition) on each step will be 12 scale steps above C3, or A4. Similarly,
counting 12 scale steps below C3, you arrive at E1. Pentatonic (5-note) scales provide
even more reach, because fewer scale steps (only five in this case) are required per
octave.


Root Key Set


The Root Key Set control establishes the root key of the Pitch Sequencer. This
corresponds to the middle line along the window. It is also the note value of all the steps
when the sequencer is reset (Reset button to the right of the various sequencers). Think
of the root key as the key you want to play in. Used with the Scale Selector (see below),
the root key can help you quickly build tonal sequences that automatically confine
themselves to a particular scale, based on a particular root key for that scale.


BACK
TO TABLE OF CONTENT


34


Scale Selector


The Scale Selector gives you a broad choice of automatic scaling of the Pitch Sequencer.
If you do not want to be confined to a particular scale or mode, choose "Chromatic" and
the Pitch Sequencer will behave like any normal pitch sequencer module. However, if you
are building a pattern in, say, D minor, then setting the Root Key to "D" and the Scale
Selector to "minor" will make sure that all the steps in the Pitch Sequencer will be part of
a D minor scale.


In addition to major and minor scales, there is very large number of other scales.
Experimenting with the different scale types can yield unexpected and interesting
results.


Recording Input Mode


Although the standard way of building patterns is drawing on the various sequencers
with your computer mouse, you might find it easier to use one of the recording input
modes for creating pitch sequences which uses the MIDI notes produced by your MIDI
keyboard/controller to record into the pitch sequencer.


The Recording Input Mode gives you a choice between Live and Step recording:


When the Record button is activated in Live mode, the pitches will be recorded in real
time when you set Thesys in motion. In this case, each note you play will be quantized to
the clock rate (BPM x note value = step rate). Depending on the length set in the Pitch
Sequencer, the pattern will continue repeating and will record any incoming MIDI notes —
overwriting notes which were recorded on previous passes — until you press Record
again to stop the recording process or until the sequencer clock is stopped.


In Step mode, each each time you play a note, Thesys records that note on the current
step, advances to the next step, and then waits for you to play the next note. This is very
useful for building complex patterns that may be difficult to play in real time.


BACK
TO TABLE OF CONTENT


35


Note Name Display


Below each step is a Note Name Display which shows the note name of each step.


Lock


Under the Note Name Display, the red Lock buttons let you lock each individual step to
prevent any further changes affected by the pitchkeys. Just click on along the bar under
the step(s) you would like to lock and a small red bar appears. Right click on the buttons
to unlock them.

#### Velocity


The Velocity sequencer provides the gate signal that triggers each step in the Pitch
sequencer. The height of each step (amount of velocity) determines how loud the
triggered note on that step will be played. If you are using Thesys to trigger an external
synth, make sure that the external instrument or its preset also reacts to different
velocities if you want this to be effective.


Sequencer Area


The Velocity Sequencer default step value is 0 (on a scale of 0 to 127), which represents
the lowest possible position of each step, producing no trigger on that step (no sound).
Click and drag on each step to raise or lower velocity. Click and drag along multiple steps
to create velocity curves along consecutive steps.


Mute


Each Velocity Sequencer step has its own mute button represented by the dark area
below the step. When clicked, a red "x" indicates that a step is muted. This is equivalent
to setting the step to 0 velocity and is a handy way to quickly develop rhythms in your
patterns.


BACK
TO TABLE OF CONTENT


36


#### Gate Time

The Gate Time Sequencer determines the length of the individual notes. You can think of
Gate Time as being the length of time that a key is "held down" on a keyboard. The gate
time values of each step are displayed below the corresponding step. A value of 1 (in the
middle of the step) means that a note is held for the entire value of the step time, or
100% of the step time. Lower values (less than 1) turn the gate off before the next step
is triggered while higher values can make a single note play up to the length of four steps
(value of 4.0).


The Gate Time Multiplier Fader allows to divide and multiply the gate times by up to 8
times. That way a note can be as long as a whole sequence (32steps) or so short that is
can be used as a dead note.


Gate Time also depends on the amplitude envelope of the sound being triggered. If you
are using the internal synthesizer, the Sustain level should be all the way up (to the right)
in order to completely control the length of the triggered sound with the Gate Time
Sequencer.


Varying gate times is a great way to introduce quite a bit of variety in your patterns.
Depending on the settings of the synth you are triggering, you can use Gate Time to vary
between extremely short note "impulses" to long, overlapping note "clouds". In musical
terms, this means you can go from staccato to legato (and even layered, if your synth is
polyphonic).

#### Performance


The Performance Sequencer is actually five sequencers in one: Octave, Bend, Chord, Roll,
and Random, arranged in rows. The Performance Sequencer is the key to making your
patterns vibrant and interesting by introducing quite a bit of variety in the way they are
played.


BACK
TO TABLE OF CONTENT


37


Octave


The Octave row shifts the pitch up or down one or two octaves. Click on a step to open
the octave shift palette and then click again to choose. Right-click to reset any step.


Bend


Clicking on a step in the Bend row opens a palette of twenty different pitch bend shapes
and directions to choose from. This ranges from a simple bend up or down to multibends, which can create interesting pitch modulation effects (vibrato) over individual or
multiple steps.


Chord


BACK

TO TABLE OF CONTENT


38


A click on a step in the Chord row opens the Chord Palette with a vast choice of chord
types and inversions (see Appendix 1 for a list of the chords available).


The chord is based on the current note in the pitch sequencer.
In other words, if the pitch sequencer shows note C on a step with a minor chord on it,
the resulting chord will be C minor.


Roll


The Roll row provides a choice of 18 different articulation patterns for each step. The first
row of patterns on the palette repeat the note within a three or four note subdivision. The
second row performs the same rhythm, but instead of repeating notes, each successive
note of the roll is transposed up the next scale step (depending on the scale set in the
pitch sequencer). The third row of the palette behaves exactly the same except that the
successive step repetitions are transposed down to the next scale step (also determined
by the scale set in the pitch sequencer).


Random


The Random sub-sequencer lets you randomize any of the following parameters: Pitch,
Velocity, Trigger, Gate Time, Octave, Pitch Bend, Chord Major, Chord Minor, and Roll on
any step(s) you choose. Any of the eight Modulation Track parameters may also be
randomized. Used sparingly, the Random row can spice up your sequences without
making them go completely berserk.


BACK
TO TABLE OF CONTENT


39


#### Modulation

The Modulation Sequencer allows you to modulate any available MIDI CC parameter. For
example, you can send pan, filter cutoff, or even program change information to your
external synthesizer. In addition, if you are just using the Built-in Synthesizer, you can
also modulate a number of synth parameters as well.


The Modulation Sequencer consists of eight Modulation Tracks. These are selected by
clicking on the column of eight buttons located just to the left of the Modulation
Sequencer controls with the first track at the bottom and the eighth track at the top.


Each Track can have its own Loop settings (length, start, and end) and Play Direction. It is
assigned to both an internal (Built-in Synthesizer) modulation target and an external
MIDI CC number.


The modulator select buttons light up in relation to the data they play back. Each
modulation track can be deactivated independently. Use the “All Modulators Off” Button
below the modulations selectors to deactivate all modulators with one click.


Internal Modulation


Each of the tracks is pre-assigned to a specific modulation target parameter in the builtin Synthesizer. If you click on the Modulation Track 1 (the lowest of the column of buttons
to the left of the Modulation Sequencer), you'll see the internal assignment indicates
"Level." Just to the right of that, a button can be clicked on (green) or off (dark grey) to
activate or disactivate internal modulation for that track. The pre-assigned internal
modulation parameters are: Level, Pan, Wave, Detune, Cutoff, Reso, Peak, and Delay Mix.


BACK
TO TABLE OF CONTENT


40


MIDI CC number


Just above the Internal Modulation indicator is the external MIDI CC chooser. Click to
open a drop down menu containing all of the MIDI CC numbers with Aftertouch and
Program Change located in the last menu. The MIDI CC Modulation is organized in the
same way as Internal Modulation, except that you can assign the different MIDI CC
targets however you want to the eight Modulation Tracks.


Note that each Modulation Track contains the sequencer information (Loop parameters,
direction, and values) for both the Internal Modulation AND the external MIDI CC data
transmission. In other words, each track shares the same data for both internal and
external modulation. In general, this should not make any difference because in most
cases, you'll either be using the (internally modulated) built-in Synthesizer OR the Thesys
to drive an external synthesizer.


On/Off Button


Turn internal modulation of the built-in synthesizer on or off with the green indicatorbutton.


MIDI Value
The MIDI values of each step are indicated at the bottom of each step of the Modulation
Sequencer.


BACK
TO TABLE OF CONTENT


41


### Built-in Synthesizer

Thesys is designed to be the ultimate MIDI sequencer used within a host environment.
The MIDI output is typically used to drive a software synthesizer or sampler plugged into
your host alongside Thesys, or even external hardware you might want to control as well.


However, when building patterns, at first you may not want to set up MIDI routing to a
software instrument, but just need to get a general idea of how your pattern will sound.
This is why we have created a simple built-in synthesizer.


To access the synthesizer controls, click on the loudspeaker icon along the upper edge of
the Sequencer Section. This toggles to the synthesizer controls. These controls will be
familiar to anyone having some experience with hardware or software synthesizers.

#### Synthesizer Preset Manager


Located just under the Sugar Bytes logo, the Synthesizer Preset Manager works the same
as the Sequencer Preset Manager. Simply click on the name of the preset to open the
Preset Chooser in order to load or save a preset.

#### On/Off


The Oscillator On/Off button is located in the upper right corner of the Synthesizer
Control Area and activates or deactivates the internal synthesizer.


BACK
TO TABLE OF CONTENT


42


#### Oscillator Settings

Level


Sets the volume level of the synthesizer output.


Pan


Determines the position (panorama) in a left-right stereo field.


Waveform


The Waveform knob morphs between triangle, square, and narrow square wave forms.


Detune


The synthesizer oscillators generate two voices simultaneously; the Detune controls the
frequency spread between the voices on a scale from 0 to 100%. When set in the middle,
there is no detuning, when turned to the right or left, the voices are detuned with regards
to one another, creating a thicker sound.


Volume Envelope
The volume envelope can be formed using the classic parameters Attack time, Decay
time, Sustain level, and Release time.


BACK
TO TABLE OF CONTENT


43


#### Filter

The built-in synthesizer also has a low pass filter module. The filter envelope determines
the amount of time between the cutoff and the peak value. Envelope output 0
represents the cutoff value, envelope output 1 represents the peak value. This feature
ensures that filter modulation always occurs within the valid cutoff range to avoid
clipping. If cutoff and peak (which usually is the envelope amount) would be just added,
you would easily get above the valid cutoff range and so clipping would occur.


One way to think of these values is that cutoff is the minimum frequency and peak is the
maximum frequency, and the envelope modulates the output between these two values.


Cutoff


Determines the overall cutoff frequency of the filter. It is the base value of the filter
envelope, with Peak being the highest possible value.


Reso(nance)


Resonance sets the amount of Q or resonance of the cutoff frequency. Setting this
control completely to the left will produce a very smooth, non-resonant sounding filter
effect. As Resonance increases, the cutoff frequency becomes more pronounced,
eventually becoming self-resonating (whistling sound).


Peak


Peak is the upper frequency cutoff limit as determined by the filter envelope.


Attack


The length of time required to reach the Peak frequency, as set by the Peak parameter.


Decay


The amount of time to fall back from the Peak frequency.


Sustain
The frequency held (between Peak and Cutoff) after Decay time and before Release.


BACK
TO TABLE OF CONTENT


44


Release


The amount of time for the frequency to drop back down to the cutoff frequency level.

#### Delay


The simple delay module provides separate delay time controls for the left and right
stereo channels, a delay feedback control, and an effect mix control.


Delay L(eft) Delay R(ight)


Delay time for the left and right stereo channels


Feedback


Feeds the delayed signal back into the delay module input. Setting this to a higher level
(to the right) increases the amount of delay (the number of echoes) that you hear before
the signal dies out.


Mix
Mixes the proportion of delayed signal (to the right: "wet") and unprocessed signal (to
the left: "dry").


BACK
TO TABLE OF CONTENT


45


### Appendix

Scales


All Scales available in the scale menu, with C as rootnote:

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

```


46


```
Hungarian Major:  C D# E F# G A A#

Japanese:  C C# F G G#

Jewish:  C C# E F G G# A#

Neapolitan Major:  C C# D# F G A B

Neapolitan Minor:  C C# D# F G G# B

Oriental:  C C# D# F F# A A#

Persian:  C C# E F F# G# B

Spanish 8 Tone:  C C# D# E F F# G# A#

```

BACK
TO TABLE OF CONTENT



47


### Chords

All Chords available in the performance/ chord menu, with C a rootnote.


Maj Green


Major 6 Green


Major6+Green


Major 7 Green


Major 7+ Green


Major 9 Green


BACK
TO TABLE OF CONTENT



48


Major Blue


Major 6 Blue


Major 6+ Blue


Major 7 Blue


Major 7+ Blue


Major 9 Blue


Major Yellow



49


Major 6 Yellow


Major 6+ Yellow


Major 7 Yellow


Major 7+ Yellow


Major 9 Yellow


Major White


Major 6 White



50


Major 6+ White


Major 7 White


Major 7+ White


Major 9 White


Minor Green


Minor 6 Green


Minor 6+ Green



51


Minor 7 Green


Minor 7+ Green


Minor 9 Green


Minor Blue


Minor 6 Blue


Minor 6+ Blue


Minor 7 Blue



52


Minor 7+ Blue


Minor 9 Blue


Minor Yellow


Minor 6 Yellow


Minor 6+ Yellow


Minor 7 Yellow


Minor 7+ Yellow



53


Minor 9 Yellow


Minor White


Minor 6 White


Minor 6+ White


Minor 7 White


Minor 7+ White


Minor 9 White



54


Diminished / Vermindert


Quint / Quinte


Augmented / Übermässig


Fourth / Quarte


Cluster / Traube


Quint Stack / Quintschichtung


Impressum


Manual written by Brian Smith and Sugar Bytes 2009
Sugar Bytes GmbH | Made of passion
Robert Fehse, Rico Baade | Greifswalder Str. 29 | 10405 Berlin, Germany
phone:+493060920395 | Str.-Nr. 37/207/21266 | HR-Nr. HRB 124199 B
info@sugar-bytes.de | [www.sugar-bytes.de](http://www.sugar-bytes.de/)

BACK
TO TABLE OF CONTENT



55


