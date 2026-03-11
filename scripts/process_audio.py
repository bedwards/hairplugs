#!/usr/bin/env python3
"""Process an audio file through a VST3 plugin chain from the CLI.

Examples:
    python process_audio.py input.wav output.wav WOW2 cutoff=0.5 resonance=0.8
    python process_audio.py input.wav output.wav WOW2 cutoff=0.3 -- ValhallaRoom mix=0.3 decay=0.8
"""

import sys
from pedalboard import load_plugin, Pedalboard
from pedalboard.io import AudioFile

VST3_DIR = "/Volumes/Macintosh HD/Library/Audio/Plug-Ins/VST3"

def parse_chain(args):
    """Parse CLI args into plugin chain: name param=val param=val -- name param=val ..."""
    chains = []
    current = None

    for arg in args:
        if arg == '--':
            if current:
                chains.append(current)
            current = None
            continue

        if '=' in arg:
            if current is None:
                print(f"Error: parameter {arg} before plugin name")
                sys.exit(1)
            key, val = arg.split('=', 1)
            try:
                val = float(val)
            except ValueError:
                val = val.lower() in ('true', '1', 'yes')
            current['params'][key] = val
        else:
            if current:
                chains.append(current)
            current = {'name': arg, 'params': {}}

    if current:
        chains.append(current)

    return chains

def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    chain_args = sys.argv[3:]

    chain_spec = parse_chain(chain_args)
    plugins = []

    for spec in chain_spec:
        path = f"{VST3_DIR}/{spec['name']}.vst3"
        print(f"Loading {spec['name']}...")
        plugin = load_plugin(path)
        for key, val in spec['params'].items():
            setattr(plugin, key, val)
            print(f"  {key} = {val}")
        plugins.append(plugin)

    board = Pedalboard(plugins)

    with AudioFile(input_path) as f:
        audio = f.read(f.frames)
        sr = f.samplerate

    print(f"\nProcessing {input_path} ({audio.shape[1]} samples @ {sr}Hz)...")
    output = board(audio, sr)

    with AudioFile(output_path, 'w', sr, output.shape[0]) as f:
        f.write(output)

    print(f"Written to {output_path}")

if __name__ == "__main__":
    main()
