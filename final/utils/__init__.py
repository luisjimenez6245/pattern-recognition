from PIL import Image
import numpy as np
from math import floor
import random

def image_to_bitmap(path, out_path='', x = 1):
    img = Image.open(path)
    ary = np.array(img)

    # Split the three channels
    r, g, b = np.split(ary, 3, axis=2)
    r = r.reshape(-1)
    g = r.reshape(-1)
    b = r.reshape(-1)
    # Standard RGB to grayscale
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2],
                      zip(r, g, b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float), x)
    return bitmap



def replace_from_bitmap(bitmap, before = 254, after = 1):
    result = bitmap.copy()
    for i in range(len(result)):
        for j in range(len(result[0])):
            if(result[i][j] == before):
                result[i][j] = after
    return result


def add_noise(bit_map, percentage = 5, to_add = 1,):
    x = len(bit_map[0]) - 1
    y = len(bit_map) - 1
    result = bit_map.copy()
    to_cover = floor((x * y) * (percentage / 100))
    print(x *y)
    print(to_cover)
    covered = 0
    while(covered < to_cover):
        to_x = random.randint(0, x)
        to_y = random.randint(0, y)
        if(result[to_y][to_x] != to_add):
            result[to_y][to_x] = to_add
            covered += 1
    return result


def print_bit_map(bm):
    for i in bm:
        res = ""
        for j in i:
            res += str(int(j)) + " "
        print(res)


def bit_map_to_arr(bitmap):
    res = []
    for row in bitmap:
        res.extend(row)
    return res
