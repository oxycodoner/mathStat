import enum
import random
import numpy as np
import math
from scipy.stats import chisquare


def refresh_buffer(tmp, storage):
    index = len(tmp) - 1
    if len(storage) >= len(tmp):
        storage[index] += 1
    else:
        for i in range(len(tmp) - len(storage)):
            storage = np.append(storage, 0)
        storage[index] += 1
    tmp.clear()
    return storage


class Direction(enum.Enum):
    not_up = 0
    not_down = 1


def monotonicity_check(sample, direction: Direction):
    v = np.array([], int)
    tmp = []
    for number in sample:
        if len(tmp) == 0:
            tmp.append(number)
        elif (tmp[-1] >= number and direction == Direction.not_up) or (tmp[-1] <= number and direction == Direction.not_down):
            tmp.append(number)
        else:
            v = refresh_buffer(tmp, v)
    if len(tmp) != 0:
        v = refresh_buffer(tmp, v)
    sum_v = np.sum(v)
    exp = np.array([((1 / math.factorial(i)) - (1 / math.factorial(i + 1))) * sum_v for i in range(1, len(v) + 1)])
    print(v)
    print(len(v) - 1)
    return chisquare(v, exp)


n = 1000  # число испытаний
randomizedArray = []
for i in range(n):
    randomizedArray.append(random.random())  # псевдослучайные величины, вырабатываемые
    # датчиком случайных чисел
print(randomizedArray)

print(monotonicity_check(randomizedArray, Direction.not_up))
print(monotonicity_check(randomizedArray, Direction.not_down))
