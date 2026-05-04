#!/usr/bin/env python3
"""
ASCII Lissajous Art Generator
A harmony of 5:4, phase π/4 — rendered in text.
"""

import math
import random


WIDTH = 80
HEIGHT = 40
CHARS = " .'`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&B8$@"

A, B = 3, 4
a, b = 5, 4
DELTA = math.pi / 4


def generate_lissajous(points=500):
    pts = []
    for i in range(points):
        t = (i / points) * 2 * math.pi
        x = A * math.sin(a * t + DELTA)
        y = B * math.sin(b * t)
        mx = int((x / A) * (WIDTH / 2 - 4) + WIDTH / 2)
        my = int((y / B) * (HEIGHT / 2 - 2) + HEIGHT / 2)
        pts.append((mx, my))
    return pts


def render(points):
    grid = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x, y in points:
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            idx = min(
                len(CHARS) - 1,
                int(random.random() * len(CHARS) * 0.7 + len(CHARS) * 0.3),
            )
            grid[y][x] = CHARS[idx]
    return ["".join(row) for row in grid]


def main():
    print("\n" + "=" * WIDTH)
    print("  LISSAJOUS FIGURE — Aesthetic mathematics, frozen in text")
    print(f"  Ratio 5:4, phase π/{int(math.pi/DELTA)} — a harmony that never resolves")
    print("=" * WIDTH + "\n")

    points = generate_lissajous()
    for row in render(points):
        print(row)

    print()
    print("  ", "─" * (WIDTH - 4))
    print("  Each character was chosen randomly. The pattern was not.")
    print("  ", "─" * (WIDTH - 4))


if __name__ == "__main__":
    main()
