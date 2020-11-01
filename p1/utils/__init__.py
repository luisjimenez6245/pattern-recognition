import random
from math import ceil

def gen_count(size=100):
    arr = []
    for i in range(1, size + 1):
        arr.append(i)
    return arr


def gen_random_arr(size, _from=0,  limit=0):
    arr = []
    for _ in range(0, size):
        arr.append(
            gen_random_numbers(_from, limit)
        )
    return arr


def gen_random_numbers(_from=0,  limit=0):
    x = ceil(random.uniform(_from, limit))
    return x
