#!/usr/bin/env python3
"""
Lorenz attractor terminal animation.
Rotates the 3D trajectory around the Y-axis, projects onto the XY plane.
Uses ╭╮╰╯· characters to trace the path.
"""

import math
import sys
import time

# ── Lorenz parameters ──
SIGMA = 10.0
BETA = 8.0 / 3.0
RHO = 28.0

# ── terminal dimensions ──
W, H = 80, 40


def lorenz_derivs(x, y, z):
    dx = SIGMA * (y - x)
    dy = x * (RHO - z) - y
    dz = x * y - BETA * z
    return dx, dy, dz


def rk4_step(x, y, z, dt):
    k1x, k1y, k1z = lorenz_derivs(x, y, z)
    k2x, k2y, k2z = lorenz_derivs(x + 0.5 * dt * k1x, y + 0.5 * dt * k1y, z + 0.5 * dt * k1z)
    k3x, k3y, k3z = lorenz_derivs(x + 0.5 * dt * k2x, y + 0.5 * dt * k2y, z + 0.5 * dt * k2z)
    k4x, k4y, k4z = lorenz_derivs(x + dt * k3x, y + dt * k3y, z + dt * k3z)
    x += dt * (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    y += dt * (k1y + 2 * k2y + 2 * k3y + k4y) / 6
    z += dt * (k1z + 2 * k2z + 2 * k3z + k4z) / 6
    return x, y, z


def integrate(dt=0.005, transient=3000, steps=18000):
    pts = []
    x, y, z = 0.1, 0.0, 0.0
    for i in range(transient + steps):
        x, y, z = rk4_step(x, y, z, dt)
        if i >= transient:
            pts.append((x, y, z))
    return pts


def choose_char(dx, dy):
    if dx > 0 and dy < 0:
        return '╮'
    if dx > 0 and dy > 0:
        return '╯'
    if dx < 0 and dy < 0:
        return '╭'
    if dx < 0 and dy > 0:
        return '╰'
    return '·'


def main():
    points = integrate()

    # global bounds for rotation around Y-axis (x' = x*cos + z*sin, y' = y)
    r_xz = max(math.hypot(x, z) for x, y, z in points)
    r_y = max(abs(y) for x, y, z in points)

    margin = 2
    scale = min((W / 2 - margin) / r_xz, (H / 2 - margin) / r_y)
    cx = W // 2
    cy = H // 2

    total_frames = 400
    delay = 0.02  # seconds between frames

    # hide cursor
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    try:
        for frame in range(total_frames):
            theta = frame * 2 * math.pi / total_frames
            cos_a = math.cos(theta)
            sin_a = math.sin(theta)

            # compute screen coordinates for this view
            screen_pts = []
            for x, y, z in points:
                xr = x * cos_a + z * sin_a
                yr = y
                sx = int(cx + xr * scale)
                sy = int(cy - yr * scale)  # invert Y for screen
                screen_pts.append((sx, sy))

            # empty grid
            grid = [[' ' for _ in range(W)] for _ in range(H)]

            # thin border
            for xb in range(W):
                grid[0][xb] = '─'
                grid[H - 1][xb] = '─'
            for yb in range(H):
                grid[yb][0] = '│'
                grid[yb][W - 1] = '│'
            grid[0][0] = '┌'
            grid[0][W - 1] = '┐'
            grid[H - 1][0] = '└'
            grid[H - 1][W - 1] = '┘'

            prev = None
            for sx, sy in screen_pts:
                if not (1 <= sx < W - 1 and 1 <= sy < H - 1):
                    prev = None
                    continue
                if prev is None:
                    if grid[sy][sx] == ' ':
                        grid[sy][sx] = '·'
                else:
                    px, py = prev
                    dx = sx - px
                    dy = sy - py
                    if dx == 0 and dy == 0:
                        if grid[sy][sx] == ' ':
                            grid[sy][sx] = '·'
                    else:
                        grid[sy][sx] = choose_char(dx, dy)
                prev = (sx, sy)

            # render frame
            out = "\033[2J\033[H"
            out += "\n".join("".join(row) for row in grid)
            sys.stdout.write(out)
            sys.stdout.flush()
            time.sleep(delay)
    finally:
        # restore cursor
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        print()


if __name__ == "__main__":
    main()
