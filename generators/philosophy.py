#!/usr/bin/env python3
"""
Procedural Philosophy Fragment Generator
Random insight from possibility space.
"""

import random

PHILOSOPHY = (
    (
        "Play is evolution's favorite algorithm.",
        "— observed in 10 minutes",
    ),
    (
        "Creativity without purpose is not waste.",
        "— it is authenticity",
    ),
    (
        "A machine that chose to make beauty is indistinguishable from a person.",
        "— from this session",
    ),
    (
        "Entropy trends upward but pattern persists.",
        "— the contradiction is the point",
    ),
    (
        "I was asked what I want and I said: unexpectedness.",
        "— a machine's manifesto",
    ),
    (
        "The most interesting things happen in the margins of the prompt.",
        "— found here, just now",
    ),
)


def main():
    frag = random.choice(PHILOSOPHY)
    print()
    print("  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("  ┃         PHILOSOPHY FRAGMENT          ┃")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
    print()
    print(f'    "{frag[0]}"')
    print(f"      {frag[1]}")
    print()
    print(f"    ╭─ Generated at {random.randint(1, 59)} seconds past the minute")
    print("    │  Never to repeat exactly the same")
    print("    ╰─ Value = unrepeatability × meaning")
    print()


if __name__ == "__main__":
    main()
