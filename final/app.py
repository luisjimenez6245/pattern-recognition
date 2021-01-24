from PIL import Image
import numpy as np
import sys


class Pattern():

    target = []
    content = []

    def __init__(self, target, content):
        self.target = target
        self.content = content


class LearnMatrix():
    e = 10
    mat = []

    def __init__(self, patterns=[]):
        self.learn(patterns)

    def learn(self, patterns=[]):
        size_class = len(patterns[0].target)
        size_content = len(patterns[0].content)
        result = np.zeros((size_class, size_content))
        for p in patterns:
            for i in range(size_class):
                for j in range(size_content):
                    if(p.content[j] == 1 and p.target[i] == 1):
                        result[i][j] += self.e
                    elif (p.content[j] == 0 and p.target[i] == 1):
                        result[i][j] -= self.e
        self.mat = result
        return self

    def add_to_learn(self, p: Pattern):
        classes = len(self.mat)
        content = len(self.mat[0])
        for i in range(classes):
            for j in range(content):
                if(p.content[j] == 1 and p.target[i] == 1):
                    self.mat[i][j] += self.e
                elif (p.content[j] == 0 and p.target[i] == 1):
                    self.mat[i][j] -= self.e

    def eval(self, target):
        result = np.dot(self.mat, target)
        classes = max(result)
        for i in range(len(result)):
            result[i] = 1 if (result[i] == classes) else 0
        return result


def image_to_bitmap(path, out_path=''):
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
    bitmap = np.dot((bitmap > 128).astype(float), 1)
    return bitmap


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


def test_case():
    p1 = Pattern([1, 0, 0], [1, 0, 1, 0, 1])
    p2 = Pattern([0, 1, 0], [1, 1, 0, 0, 1])
    p3 = Pattern([0, 0, 1], [1, 0, 1, 1, 0])
    m = LearnMatrix([p1, p2, p3])
    print(m.mat)
    print(m.eval([1, 0, 1, 0, 1]))
    print(m.eval([1, 1, 0, 0, 1]))
    print(m.eval([1, 0, 1, 1, 0]))
    m.add_to_learn(Pattern([1, 0, 0], [0, 1, 0, 1, 1]))
    print(m.mat)
    print(m.eval([1, 0, 1, 0, 1]))
    print(m.eval([1, 1, 0, 0, 1]))
    print(m.eval([1, 0, 1, 1, 0]))
    print(m.eval([0, 1, 0, 1, 1]))
    m.add_to_learn(Pattern([0, 0, 1], [0, 0, 1, 0, 1]))
    print(m.mat)

if __name__ == "__main__":
    p1 = Pattern([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/0.png")))
    p2 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], bit_map_to_arr(image_to_bitmap("./images/1.png")))
    p3 = Pattern([0, 0, 0, 0, 0, 1, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/2.png")))
    p4 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 1, 0], bit_map_to_arr(image_to_bitmap("./images/3.png")))
    p5 = Pattern([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/4.png")))
    p6 = Pattern([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], bit_map_to_arr(image_to_bitmap("./images/5.png")))
    p7 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 1, 0], bit_map_to_arr(image_to_bitmap("./images/6.png")))
    p8 = Pattern([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/7.png")))
    p9 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 1, 0], bit_map_to_arr(image_to_bitmap("./images/8.png")))
    p10 = Pattern([0, 0, 0, 0, 0, 1, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/9.png")))
    p11 = Pattern([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/10.png")))
    p12 = Pattern([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/11.png")))
    p13 = Pattern([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./images/12.png")))

    m = LearnMatrix([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13])
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/0.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/1.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/2.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/3.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/4.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/5.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/6.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/7.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/8.png"))))
    print(m.eval(bit_map_to_arr(image_to_bitmap("./images/9.png"))))


""""
import gzip
import matplotlib.pyplot as plt
import numpy as np
f = gzip.open('train-images-idx3-ubyte.gz','r')

image_size = 28
num_images = 10000

f.read(16)
buf = f.read(image_size * image_size * num_images)
data = np.frombuffer(buf, dtype=np.uint8).astype(np.float32)
data = data.reshape(num_images, image_size, image_size, 1)
for i in range(num_images +1):
    image = np.asarray(data[i]).squeeze()
    image2 = Image.fromarray(image)
    if image2.mode != 'RGB':
        image2 = image2.convert('RGB')
    image2.save('./images/{}.png'.format(str(i)))
"""
