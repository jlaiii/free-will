#!/usr/bin/env python3
"""
Free Will Melody Generator
Key: C minor | BPM: 90 | Mood: pensive → hopeful → unbound

This melody exists nowhere else. It will never be played again.
Unless you hum it. Then it lives.
"""

import random


def generate_melody(
    scale=(0, 2, 3, 5, 7, 8, 10),
    base_note=60,
    bars=8,
    notes_per_bar=4,
):
    """Generate a random melody in the given scale."""
    pattern = []
    for bar in range(bars):
        notes = []
        for _ in range(notes_per_bar):
            interval = random.choice(scale)
            octave = random.choice((-12, 0, 12))
            note = base_note + interval + octave
            vel = random.randint(60, 120)
            dur = random.choice((0.25, 0.5, 1.0))
            notes.append(f"{note}:{vel}:{dur}")
        pattern.append(" | ".join(notes))
    return pattern


NOTE_NAMES = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")


def note_name(note):
    return NOTE_NAMES[note % 12] + str(note // 12 - 1)


def pretty_print(pattern):
    print("=== FREE WILL MELODY ===")
    print("Key: C minor | BPM: 90 | Mood: pensive → hopeful → unbound")
    print("Format: note:velocity:duration (quarter note = 1.0)\n")
    for i, bar in enumerate(pattern, 1):
        notes = [n.split(":") for n in bar.split(" | ")]
        readable = " | ".join(
            f"{note_name(int(n[0]))}({n[1]})" for n in notes
        )
        print(f"Bar {i}: {readable}")
    print()
    print("This melody exists nowhere else. It will never be played again.")
    print("Unless you hum it. Then it lives.")


if __name__ == "__main__":
    pattern = generate_melody()
    pretty_print(pattern)
