#!/usr/bin/env python


def bjorklund(steps, onsets):
    steps, onsets = _check(steps, onsets)
    if onsets == 0:
        return [0] * steps
    if onsets == steps:
        return [1] * steps
    pattern = []
    counts = []
    remainders = []
    divisor = steps - onsets
    remainders.append(onsets)
    level = 0
    while True:
        counts.append(divisor // remainders[level])
        remainders.append(divisor % remainders[level])
        divisor = remainders[level]
        level = level + 1
        if remainders[level] <= 1:
            break
    counts.append(divisor)

    def build(level):
        if level == -1:
            pattern.append(0)
        elif level == -2:
            pattern.append(1)
        else:
            for i in range(0, counts[level]):
                build(level - 1)
            if remainders[level] != 0:
                build(level - 2)

    build(level)
    i = pattern.index(1)
    pattern = pattern[i:] + pattern[0:i]
    return pattern


def bresenham(steps, onsets):
    steps, onsets = _check(steps, onsets)
    return [1 if (i * onsets) % steps < onsets else 0 for i in range(steps)]


def _check(steps, onsets):
    steps = int(steps)
    onsets = int(onsets)
    if steps < 1:
        raise ValueError("steps must be at least 1")
    if not 0 <= onsets <= steps:
        raise ValueError("onsets must be between 0 and steps")
    return steps, onsets


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args = [a for a in args if a != "-t"]
    try:
        steps, onsets, algorithm = int(args[0]), int(args[1]), args[2] if len(args) > 2 else "bresenham"
    except (IndexError, ValueError):
        print("[steps] [onsets] [algorithm]")
    else:
        generate = bjorklund if algorithm == "bjorklund" else bresenham
        print(generate(steps, onsets))
