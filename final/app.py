from PIL import Image
import numpy as np
import sys

def image_to_bitmap(path, out_path = ''):
    img = Image.open(path)
    ary = np.array(img)

    # Split the three channels
    r,g,b = np.split(ary,3,axis=2)
    r=r.reshape(-1)
    g=r.reshape(-1)
    b=r.reshape(-1)

    # Standard RGB to grayscale 
    bitmap = list(map(lambda x: 0.299*x[0]+0.587*x[1]+0.114*x[2], 
    zip(r,g,b)))
    bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
    bitmap = np.dot((bitmap > 128).astype(float),1)
    return bitmap


def print_bit_map(bm):
    for i in bm:
        res = ""
        for j in i:
            res += str(int(j)) +" "
        print(res)


if __name__ == "__main__":
    bm = (image_to_bitmap('./images/{}.png'.format(sys.argv[1])))
    print_bit_map(bm)

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