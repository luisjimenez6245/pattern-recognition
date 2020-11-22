import numpy as np
from .base_classifier import BaseClassifier


class MetricClassifier(BaseClassifier):

    r: int

    def compare(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.distance(x, item.z)
        return result

    @classmethod
    def distance(cls, x, y):
        if(len(x) == len(y)):
            return cls.calc(cls.r, x, y, len(x))
        return -1

    @staticmethod
    def calc(r, x=[], y=[], n=0):
        r = 1/r
        helper = np.subtract(x, y)
        transpose = np.transpose(helper)
        d = np.dot(transpose, helper)
        d = np.power(d, r)
        return d
