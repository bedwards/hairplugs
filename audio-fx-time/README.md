# Audio FX — Time (Time-Based)

Time-based audio effects that add spatial and temporal dimension: reverb, delay, chorus, flanger, phaser. These go after tone effects in the chain.

## Comeback Kid (Baby Audio)
Character delay with lo-fi flavor. Simple but musical delay with feedback, ping-pong, and filtering.
- **Pedalboard**: 23 params (delay_time_sync, delay_time_ms_ms, delay_mode, feedback, ping_pong, wider, richer, pan, mono, lo_cut_hz...)
- **Best for**: Slapback on acoustic guitar, ambient delays, lo-fi folktronica delays

## Valhalla Room (Valhalla DSP)
Algorithmic reverb. Clean, versatile, and CPU-efficient. Multiple room algorithms.
- **Pedalboard**: 23 params (mix, predelay, decay, hicut, earlylatemix, latesize, latecross, latemodrate, latemoddepth, rtbassmultiply...)
- **Best for**: Everything — room verb for acoustic instruments, large halls for ambient, tight rooms for drums

## Permut8 (Sonic Charge)
Granular/glitch delay effect. Takes audio and rearranges it in unpredictable ways. Part delay, part granular, part chaos.
- **Best for**: Experimental textures, glitch effects, folktronica weirdness

## Chain Position

```
[Instrument] → [Tone FX: EQ, compression, saturation] → [Time FX: delay, reverb] → [Master]
```

Time-based effects generally go last in the insert chain (before master bus) because you want to add space to the already-shaped sound.

### Typical Send FX Setup in Bitwig
1. **Send 1**: Valhalla Room (short room, mix 100%)
2. **Send 2**: Valhalla Room (large hall, mix 100%)
3. **Send 3**: Comeback Kid (delay, mix 100%)
4. Instruments/tracks send varying amounts to each
