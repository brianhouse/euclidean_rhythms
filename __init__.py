#!/usr/bin/env python


def bjorklund(steps, pulses):
    steps, pulses = _check(steps, pulses)
    if pulses == 0:
        return [0] * steps
    if pulses == steps:
        return [1] * steps
    pattern = []
    counts = []
    remainders = []
    divisor = steps - pulses
    remainders.append(pulses)
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


def bresenham(steps, pulses):
    steps, pulses = _check(steps, pulses)
    return [1 if (i * pulses) % steps < pulses else 0 for i in range(steps)]


def _check(steps, pulses):
    steps = int(steps)
    pulses = int(pulses)
    if steps < 1:
        raise ValueError("steps must be at least 1")
    if not 0 <= pulses <= steps:
        raise ValueError("pulses must be between 0 and steps")
    return steps, pulses


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    toussaint = "-t" in args
    args = [a for a in args if a != "-t"]
    try:
        steps, pulses = int(args[0]), int(args[1])
    except (IndexError, ValueError):
        print("[steps] [pulses] [-t]")
    else:
        generate = bresenham if toussaint else bjorklund
        print(generate(steps, pulses))
