import numpy as np


def count_encountered_trees():
    data = np.genfromtxt("input", dtype=str, delimiter="\n", comments=None)
    configs = [1, 1, 7, 5, 3]
    total = 1
    for index, value in enumerate(configs):
        count, column = 0, 0
        i = 0
        while i < len(data):
            if data[i][column % 31] == "#":
                count += 1
            column += value
            i += 2 - -value & 8 >> 3
        if index == 4:
            print(count)
        total *= count
    print(int(total / 2))


if __name__ == "__main__":
    count_encountered_trees()
