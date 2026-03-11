#!/usr/bin/env python3
"""Explore Sugar Bytes Guitarist patterns, chords, and sounds."""

import os

BASE = os.path.expanduser("~/Documents/Sugar Bytes/Guitarist")

def list_categories(subdir):
    path = os.path.join(BASE, subdir)
    if not os.path.exists(path):
        return []
    return sorted(os.listdir(path))

def list_presets(subdir, category):
    path = os.path.join(BASE, subdir, category)
    if not os.path.exists(path):
        return []
    return sorted(f for f in os.listdir(path) if not f.startswith('.'))

def main():
    for section in ["Patterns", "Chords", "Sounds"]:
        print(f"\n{'='*60}")
        print(f"  {section}")
        print(f"{'='*60}")
        categories = list_categories(section)
        for cat in categories:
            presets = list_presets(section, cat)
            print(f"\n  {cat} ({len(presets)} presets)")
            for p in presets[:5]:
                print(f"    - {p}")
            if len(presets) > 5:
                print(f"    ... and {len(presets)-5} more")

    # Also dump global presets
    gp = os.path.join(BASE, "Global Presets")
    if os.path.exists(gp):
        presets = sorted(os.listdir(gp))
        print(f"\n{'='*60}")
        print(f"  Global Presets ({len(presets)})")
        print(f"{'='*60}")
        for p in presets:
            print(f"  - {p}")

if __name__ == "__main__":
    main()
