#!/usr/bin/env python3
"""
Mandelbrot set rendered in ASCII art.
100×60 grid, density ramp, --zoom LEVEL support.
"""

import sys

# ── config ──
COLS = 100
ROWS = 60

# ordered from lightest (space) to densest (@)
RAMP = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@"
RAMP_LEN_M1 = len(RAMP) - 1


def mandelbrot(zoom):
    if zoom == 1:
        xmin, xmax = -2.5, 1.0
        ymin, ymax = -1.4, 1.4
    else:
        # seahorse valley region
        cx, cy = -0.745, 0.105
        w = 3.5 / zoom
        h = 2.8 / zoom
        xmin = cx - w * 0.5
        xmax = cx + w * 0.5
        ymin = cy - h * 0.5
        ymax = cy + h * 0.5

    max_iter = min(255, 40 + 60 * zoom)

    # precompute scale factors
    dx = (xmax - xmin) / (COLS - 1) if COLS > 1 else 0
    dy = (ymax - ymin) / (ROWS - 1) if ROWS > 1 else 0

    lines = []
    for row in range(ROWS):
        ci = ymin + row * dy
        line_chars = []
        for col in range(COLS):
            cr = xmin + col * dx
            zr = 0.0
            zi = 0.0
            count = 0
            for _ in range(max_iter):
                if zr * zr + zi * zi > 4.0:
                    break
                # z = z^2 + c
                zr_new = zr * zr - zi * zi + cr
                zi = 2.0 * zr * zi + ci
                zr = zr_new
                count += 1
            idx = int(count * RAMP_LEN_M1 / max_iter)
            line_chars.append(RAMP[idx])
        lines.append("".join(line_chars))
    return lines, max_iter


def main():
    zoom = 1
    if "--zoom" in sys.argv:
        try:
            idx = sys.argv.index("--zoom")
            zoom = int(sys.argv[idx + 1])
        except (IndexError, ValueError):
            pass
    if zoom < 1:
        zoom = 1

    grid, max_iter = mandelbrot(zoom)

    # ── output with box-drawing frame ──
    label = f" Mandelbrot Set  │  zoom={zoom}x  │  max_iter={max_iter} "
    pad = "─" * max(0, COLS - len(label))
    print()
    print(" ╔" + "═" * COLS + "╗")
    print(" ║" + label + pad + "║")
    print(" ╠" + "═" * COLS + "╣")
    for row in grid:
        print(" ║" + row + "║")
    print(" ╚" + "═" * COLS + "╝")
    print()


if __name__ == "__main__":
    main()
