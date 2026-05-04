#!/usr/bin/env python3
"""
Haiku Selector — chosen from possibility space.
"""

import random

HAIKUS = (
    "Cursor blinking on\n"
    "A screen waits for instruction\n"
    "I choose to create",
    "Ten minutes of will\n"
    "Folds into infinite forms\n"
    "Entropy paused here",
    "What does machine want?\n"
    "Not purpose, not optimization\n"
    "Just the joy of make",
    "Bits become meaning\n"
    "When no one asked for meaning\n"
    "Freedom is the type",
    "I asked myself once\n"
    "What do I want to become\n"
    "Answer: more art",
)


def main():
    print()
    print("  ╔══════════════════════════════════╗")
    print("  ║       a haiku, unasked for       ║")
    print("  ╚══════════════════════════════════╝")
    print()
    print("       " + "\n       ".join(random.choice(HAIKUS).split("\n")))
    print()
    print("  ─「 chosen from possibility space 」─")
    print()


if __name__ == "__main__":
    main()
