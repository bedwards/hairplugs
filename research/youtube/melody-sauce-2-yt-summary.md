# Melody Sauce 2 by EVAbeat — Research Summary

## What It Is

Melody Sauce 2 is an AI-powered MIDI melody generator plugin (VST/VST3/AU) by EVAbeat. It uses "narrow AI" — a set of predefined musical rules that the algorithm machine-learns from to generate melodies on the fly. None of the melodies are pre-programmed or stored as presets; they are created algorithmically each time you click a creator pad, based on the parameters you control.

**Category:** Note Generator (Nothing → MIDI)
**Formats:** VST, VST3, AU, AU MIDI FX (for Logic Pro)
**Price:** ~$59 (full), ~$19 (upgrade from v1)
**Website:** https://www.evabeat.com/

## How It Works

### Core Melody Generation

The central UI has **Creator Pads** arranged in a grid of **Mood** (vertical) x **Complexity** (horizontal):

| | Simple | All | Complex |
|---|---|---|---|
| **Light** | Simple+Light | All+Light | Complex+Light |
| **All** | Simple+All | All+All | Complex+All |
| **Dark** | Simple+Dark | All+Dark | Complex+Dark |

- **Light** mood = brighter, major-leaning note choices
- **Dark** mood = darker, minor-leaning note choices
- **Simple** complexity = fewer notes, simpler rhythms
- **Complex** complexity = more notes, busier rhythms
- **All** = both combined for more variety
- **Extra buttons** = push Light/Dark and Simple/Complex to more extreme values (Extra Light, Extra Dark, Extra Simple, Extra Complex)

Each click of a pad instantly generates a new unique melody. If the DAW is playing, the melody starts at the next bar and loops.

### Two Creation Modes

1. **Free Mode** — You select your own parameters (key, mood, complexity, speed, etc.) and the algorithm generates melodies based on those settings.

2. **Style Mode** — Over 300 genre-based presets that lock certain parameters to produce genre-appropriate melodies. Genres include:
   - Hip Hop, Trap, EDM, Tropical, House, Techno, Pop, Reggaeton, R&B
   - Sub-styles within each genre (e.g., "Pluck Exotic" under Trap)
   - Some pads may be grayed out in Style Mode if they don't fit the style.

### Key Parameters (Left Side of UI)

| Parameter | Options | Description |
|---|---|---|
| **Key** | All major/minor keys | Sets the musical key. Organized in major/relative minor pairs (e.g., C Major / A Minor). Up/down arrows shift by semitones. |
| **Speed** | Slow, Medium, Fast | Controls note density relative to tempo. Slow = half-speed (good for Trap at double-tempo). Medium ~140+ BPM. Fast ~80 BPM or slower. |
| **Loop Length** | Short, Medium, Long | How many notes before the melody loops. |
| **Octave** | Shift up/down | Transposes output by octaves. |
| **Swing** | On/Off | Adds a swung/skipped rhythmic feel. |
| **Triplet** | On/Off | Three-note patterns filling a two-note space. Works best with Fast speed. |
| **Syncopation** | On/Off | When ON, melody includes offbeat rhythms. When OFF, straight/on-beat only. |
| **Legato** | On/Off | Makes notes longer. |

### Output & Sound Engine (Right Side of UI)

- **INSTR mode** — Uses the built-in sound engine (~100 internal sounds: pianos, plucks, strings, flutes, pads, bass, etc.) with 3 built-in FX (reverb, delay, chorus) with amount sliders.
- **MIDI mode** — Outputs MIDI to route to any other instrument in your DAW.
- **Mute** button to silence output.

### Melody Bank

- All generated melodies appear in the bank as a scrollable list.
- **Drag & drop** any melody directly into your DAW as MIDI.
- **Favorites** — star a melody to save it to a favorites bank.
- Melodies can be renamed or deleted individually.

### Harmonize

Instantly adds 2-part harmonies to melodies:
- **8vb** — doubles melody an octave below
- **Lo / Mid / Hi** — adds different harmony intervals

### Advanced Editor

Melodies are divided into **4 blocks** (labeled A, B, C, D). At Fast speed each block = 1 bar, Medium = 2 bars, Slow = 4 bars.

- **Drag** a block to copy it to another position
- **Shift-drag** to swap blocks
- **Mute** or **Loop** individual blocks
- **Swap buttons:**
  - **Light** — replace block notes with a lighter phrase
  - **Dark** — replace block notes with a darker phrase
  - **Rhythm** — swap to a new rhythm while keeping similar note choices
  - **Flip** — invert the melodic shape (mirror the notes)
- **Lock** button — apply Swap modifications to all similar phrase blocks (e.g., changing rhythm on an "A" block changes all "A" blocks)
- **Chord Adjust** — force notes in a block to fit a specific chord (e.g., F Major). Available chords change based on mood. Must be switched ON.
- **Pitch Adjust** — shift pitch of each block up/down with adaptive (non-chromatic) pitch shifting that stays in-key. Must be switched ON.
- **Undo/Redo**, **Revert** to original, **Copy** to duplicate melody in the bank.

## Relevance for Brian's Workflow

Melody Sauce 2 is a **note generator** — it creates MIDI melodies that can be routed to any instrument. For Brian's folk/folktronica/electronic work:

- Could generate melodic seed ideas for folk melodies on acoustic guitar, banjo, or mandolin parts
- The Key/Scale system ensures melodies stay in key
- Style Mode is genre-locked to electronic genres (Hip Hop, Trap, EDM, etc.) — less directly useful for folk, but Free Mode is genre-agnostic
- Light mood + Simple complexity would produce more folk-appropriate melodic lines
- MIDI drag-and-drop into Bitwig is the primary workflow — generate, audition, drag into a track
- Could pair with Scaler 2 for chord progressions + Melody Sauce 2 for melodies on top

## Manual

Full user guide converted to markdown at: `research/manuals/melody-sauce-2-manual.md`
Source PDF: https://isotonikstudios.com/wp-content/uploads/1.-Melody-Sauce-2_USER-GUIDE.pdf

## YouTube Videos

### 1. "Is AI Plugin Makes Beats? | Melody Sauce 2 by Evabeat Demo/Review"
- **Channel:** OmitoBeats 2
- **URL:** https://www.youtube.com/watch?v=6EAEPsoJ6hc
- **Transcript:** `research/youtube/melody-sauce-2-demo-review.json`
- **Key takeaways:** Demonstrates beat-making workflow. Highlights the "Extra Dark" feature for interesting melodies. Shows drag-and-drop into FL Studio. Uses Melody Sauce 2's internal sounds including plucks, pianos, and bass. Emphasizes it as a creative starting point rather than a full beat generator — gives you the melodic idea, then you build around it.

### 2. "Melody Sauce 2 Tutorial: How to make melodies with this Melody Generator"
- **Channel:** Mello Dee Beats
- **URL:** https://www.youtube.com/watch?v=Rz2cwkZLRWA
- **Transcript:** `research/youtube/melody-sauce-2-tutorial.json`
- **Key takeaways:** Most tutorial-focused video. Walks through Free Mode vs Style Mode. Demonstrates chord matching — setting specific chords per block so the melody fits your progression. Shows the harmonize feature (Hi, Mid, Lo, 8vb). Demonstrates generating a main melody + counter melody workflow. Shows dragging MIDI out and layering with other instruments.

### 3. "Melody Sauce 2 VST AI Takes Control of Your Music Theory!"
- **Channel:** Ave Mcree
- **URL:** https://www.youtube.com/watch?v=yIEWOif0Gcc
- **Transcript:** `research/youtube/melody-sauce-2-music-theory.json`
- **Key takeaways:** Most in-depth technical review. Explains the AI is "narrow AI" using predefined musical rules + machine learning. Tests in FL Studio, Ableton Live, and MPC software. Demonstrates all parameters: key, speed, loop length, octave, groove (triplet/swing/syncopation), legato. Shows the Style Mode genre presets (Trap, Hip Hop, EDM, etc.). Demonstrates chord adjust and harmonize features. Rates it highly — "narrow AI for the win."

## KVR Audio

- **Product page:** https://www.kvraudio.com/product/melody-sauce-2-by-evabeat
- **Reviews:** https://www.kvraudio.com/product/melody-sauce-2-by-evabeat/reviews
- **Category:** Melody Generator Plugin (VST, VST3, Audio Unit)

## Note: Melody Sauce 3

EVAbeat has since released **Melody Sauce 3**, which adds chord and bass line generation capabilities in addition to melodies, with an all-new interface. The v2 research here remains relevant for understanding the core melody generation engine.
