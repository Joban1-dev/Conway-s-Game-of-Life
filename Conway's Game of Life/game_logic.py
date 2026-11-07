import numpy as np

def next_generation(current_gen):
    next_gen = np.empty(current_gen.shape)

    for row in range(current_gen.shape[0]):
        for column in range(current_gen.shape[1]):
            count = 0

            if 0 <= row - 1 < current_gen.shape[0] and 0 <= column - 1 < current_gen.shape[1] and current_gen[row - 1][column - 1] == 1:
                count += 1
            if 0 <= row - 1 < current_gen.shape[0] and 0 <= column < current_gen.shape[1] and current_gen[row - 1][column] == 1:
                count += 1
            if 0 <= row - 1 < current_gen.shape[0] and 0 <= column + 1 < current_gen.shape[1] and current_gen[row - 1][column + 1] == 1:
                count += 1

            if 0 <= row < current_gen.shape[0] and 0 <= column - 1 < current_gen.shape[1] and current_gen[row][column - 1] == 1:
                count += 1
            if 0 <= row < current_gen.shape[0] and 0 <= column + 1 < current_gen.shape[1] and current_gen[row][column + 1] == 1:
                count += 1

            if 0 <= row + 1 < current_gen.shape[0] and 0 <= column - 1 < current_gen.shape[1] and current_gen[row + 1][column - 1] == 1:
                count += 1
            if 0 <= row + 1 < current_gen.shape[0] and 0 <= column < current_gen.shape[1] and current_gen[row + 1][column] == 1:
                count += 1
            if 0 <= row + 1 < current_gen.shape[0] and 0 <= column + 1 < current_gen.shape[1] and current_gen[row + 1][column + 1] == 1:
                count += 1

            if count < 2 and current_gen[row][column] == 1:
                next_gen[row][column] = 0
            elif 1 < count < 4 and current_gen[row][column] == 1:
                next_gen[row][column] = 1
            elif count > 3 and current_gen[row][column] == 1:
                next_gen[row][column] = 0
            elif count == 3 and current_gen[row][column] == 0:
                next_gen[row][column] = 1
            else:
                next_gen[row][column] = current_gen[row][column]

    return next_gen