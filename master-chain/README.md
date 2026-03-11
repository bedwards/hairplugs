# Master Chain

Mastering tools for the final mix bus and true mastering stage.

## Two-Stage Mastering Workflow

Brian uses a two-project approach in Bitwig:
1. **Mix Project**: Compose and mix. Master bus has a "playing" chain (not limiting/maximizing)
2. **Master Project**: Import the mixed stereo export. Apply true mastering chain.

This saves CPU and avoids glitching during the creative phase.

---

## Mix Bus Chain (for playing/monitoring)

Goal: Sound good while working, integrated loudness, but NOT maximized.

### Recommended Mix Bus Setup
```
1. soothe2 (subtle, tame resonances)
2. DynOne3 (gentle multiband compression, glue)
3. Oxford Inflator (warmth, perceived loudness)
4. iZotope Insight 2 (metering — LUFS, true peak, spectrum)
```

### Alternative Mix Bus (Ozone modules)
```
1. Ozone 11 Equalizer (surgical EQ)
2. Ozone 11 Dynamics (multiband compression)
3. Ozone 11 Exciter (subtle harmonics)
4. Ozone 11 Imager (stereo width)
5. iZotope Insight 2 (metering)
```

---

## True Master Chain (separate project)

Goal: Final loudness, tonal balance, stereo imaging, limiting to target LUFS.

### Chain A: Full Ozone
```
1. Ozone 11 Match EQ (reference track matching)
2. Ozone 11 Equalizer (tonal balance)
3. Ozone 11 Dynamics (multiband compression)
4. Ozone 11 Vintage Tape (analog warmth)
5. Ozone 11 Exciter (top-end air)
6. Ozone 11 Imager (stereo width per band)
7. Ozone 11 Low End Focus (bass clarity)
8. Ozone 11 Maximizer (final limiting, target LUFS)
9. iZotope Insight 2 (metering)
```

### Chain B: Hybrid
```
1. soothe2 (resonance control)
2. DynOne3 (multiband dynamics)
3. Oxford Inflator (harmonics/loudness)
4. Ozone 11 Imager (stereo)
5. Ozone 11 Maximizer (final limiting)
6. iZotope Insight 2 (metering)
```

### Chain C: Minimal/Transparent
```
1. Ozone 11 Equalizer (gentle tonal correction)
2. Ozone 11 Maximizer (transparent limiting)
3. iZotope Insight 2 (metering)
```

---

## Target Levels

| Format | Target LUFS | True Peak |
|--------|------------|-----------|
| Streaming (Spotify, Apple Music) | -14 LUFS | -1 dBTP |
| YouTube | -14 LUFS | -1 dBTP |
| CD / Bandcamp | -10 to -12 LUFS | -0.3 dBTP |
| Mixing reference (playing) | -16 to -18 LUFS | -3 dBTP |

## Available Ozone 11 Modules
- Clarity, Dynamic EQ, Dynamics, Equalizer, Exciter
- Imager, Impact, Low End Focus, Master Rebalance
- Match EQ, Maximizer, Spectral Shaper, Stabilizer
- Vintage Compressor, Vintage EQ, Vintage Limiter, Vintage Tape

## iZotope Metering
- **Insight 2**: Full metering suite (loudness, spectrum, stereo, history)
- **Relay**: Gain staging utility
- **Neutron 4 Elements**: Channel strip (EQ + compressor)

## Audio Repair (Pre-Master)
- **RX 10**: De-noise, de-click, de-hum, de-ess, breath control, de-reverb, etc.
- Use RX before mastering to clean up recordings
