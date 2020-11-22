import numpy as np


class EuclidianClassifier():

    def __init__(self, classes):
        self.classes = {}
        self.length = len(classes[0].z)
        for c in classes:
            self.classes[c.name] = c
            if(self.length != len(c.z)):
                raise Exception("length exception")

    def train(self, key, val):
        self.classes[key]

    def compare(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.distance(x, item.z)
        return result

    @classmethod
    def distance(cls, x, y):
        r = 2
        if(len(x) == len(y)):
            return cls.calc(r, x, y, len(x))
        return -1

    @staticmethod
    def calc(r, x=[], y=[], n=0):
        r = 1/r
        helper = np.subtract(x, y)
        transpose = np.transpose(helper)
        d = np.dot(transpose, helper)
        d = np.power(d, r)
        return d
