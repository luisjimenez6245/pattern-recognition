from .utils import BaseClassifier
import numpy as np
import itertools


class NormalClassifier(BaseClassifier):


    def __init__(self, classes):
        super().__init__(classes)
        pairs = itertools.combinations(self.classes, 2)
        self.pairs = []
        for i, j in pairs:
            self.pairs.append((i, j))


    def compare(self, x):
        res = {}
        for i, j in self.pairs:
            res[i + j] = self.calc(
                self.classes[i].z,
                self.classes[j].z,
                x
            )
        return res

    @staticmethod
    def calc(zi , zj, x):
        zi = np.array(zi)
        zj = np.array(zj)
        x = np.array(x)
        d_minus = np.transpose(zi-zj)
        d_plus = zi+zj
        rigth = -1 * (np.dot(d_minus, d_plus) / 2)
        left = np.dot(d_plus, x)
        return left + rigth