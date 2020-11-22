import numpy as np
import itertools


class NormalClassifier():

    def __init__(self, classes):
        self.classes = {}
        self.length = len(classes[0].z)
        for c in classes:
            self.classes[c.name] = c
            if(self.length != len(c.z)):
                raise Exception("length exception")
        self.pairs = itertools.combinations(self.classes, 2)

    def train(self, key, val):
        self.classes[key]

    def compare(self, x):
        res = {}
        for i, j in self.pairs:
            zi = np.array(self.classes[i].z)
            zj = np.array(self.classes[j].z)
            d_minus = np.transpose(zi-zj)
            d_plus = zi+zj
            rigth = -1 * (np.dot(d_minus, d_plus) / 2)
            left = np.dot(d_plus, x)
            res[i + j] = left + rigth
        return res