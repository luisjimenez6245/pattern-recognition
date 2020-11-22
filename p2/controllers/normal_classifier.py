from .utils import BaseClassifier
import numpy as np
import itertools


class NormalClassifier(BaseClassifier):

    def __init__(self, classes):
        super().__init__(classes)
        self.pairs = itertools.combinations(self.classes, 2)

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