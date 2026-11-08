import numpy as np

def next_generation(current_gen):
    padded = np.pad(current_gen, 1)
    top_left = padded[:-2, :-2]
    top = padded[:-2, 1:-1]
    top_right = padded[:-2, 2:]
    left = padded[1:-1, :-2]
    right = padded[1:-1, 2:]
    bottom_left = padded[2:, :-2]
    bottom = padded[2:, 1:-1]
    bottom_right = padded[2:, 2:]

    count = (top_left + top + top_right + left + right + bottom_left + bottom + bottom_right)

    alive_dead = (current_gen == 1)
    survive = alive_dead & (
            (count == 2) | (count == 3)
    )

    revive = ~alive_dead & (
        (count == 3)
    )

    next_gen = survive | revive
    next_gen = next_gen.astype(int)
    print(next_gen)

    return next_gen