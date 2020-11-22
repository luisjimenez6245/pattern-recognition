import numpy as np
import itertools


class MetricClassifier():

    def __init__(self, classes):
        self.classes = {}
        self.length = len(classes[0].z)
        for c in classes:
            self.classes[c.name] = c
            if(self.length != len(c.z)):
                raise Exception("length exception")

    def train(self, key, val):
        self.classes[key]

    def euclidian(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.euclidian_calc(x, item.z)
        return result
    
    def city_block(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.city_block_calc(x, item.z)
        return result


    def infinity(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.infinity_calc(x, item.z)
        return result
    

    @classmethod
    def city_block_calc(cls, x, y):
        r = 1
        if(len(x) == len(y)):
            return cls.calc(r, x, y, len(x))
        return -1
    
    @classmethod
    def euclidian_calc(cls, x, y):
        r = 2
        if(len(x) == len(y)):
            return cls.calc(r, x, y, len(x))
        return -1

    @classmethod
    def infinity_calc(cls, x, y):
        r = np.Infinity
        if(len(x) == len(y)):
            return cls.calc(r, x, y, len(x))
        return -1

    @staticmethod
    def calc(r, x=[], y=[], n=0):
        if(r != np.Infinity):
            r = 1/r
        helper = np.subtract(x, y)
        transpose = np.transpose(helper)
        d = np.dot(transpose, helper)
        d = np.power(d, r)
        return d
