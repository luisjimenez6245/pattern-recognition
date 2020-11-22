import numpy as np
import itertools


def multiple_matrix(x):
    res = ""
    for i in range(len(x)):
        res += ("(" + str(x[i]) + '*X' + str(i) + ")+")
    return res


class EuclidianClassifier():

    def __init__(self, classes):
        self.classes = {}
        self.length = len(classes[0].z)
        for c in classes:
            self.classes[c.name] = c
            if(self.length != len(c.z)):
                raise Exception("length exception")
        pairs = list(itertools.combinations(self.classes, 2))
        self.pairs = {}
        for i, j in pairs:
            self.pairs[i+j] = self.get_discriminant_functions(
                self.classes[i].z, self.classes[j].z
            )

    def train(self, key, val):
        self.classes[key]

    def compare(self, x):
        result = {}
        for c in self.classes:
            item = self.classes[c]
            result[c] = self.distance(x, item.z)
        res = {}
        for item in self.pairs:
            res[item] = self.eval_discriminant_functions(
                self.pairs[item], x
            )
        print(res)
        return result

    @classmethod
    def distance(cls, x, y):
        r = 2
        if(len(x) == len(y)):
            return cls.calc(r, x, y, len(x))
        return -1

    @staticmethod
    def get_discriminant_functions(zi, zj):
        zi = np.array(zi)
        zj = np.array(zj)
        helper = zi-zj
        transpose = np.transpose(helper)
        d_r = (-1/2) * np.dot(transpose,  (zi + zj))
        d_l = multiple_matrix(transpose)
        res = d_l + str(d_r)
        return res

    @staticmethod
    def eval_discriminant_functions(func, val):
        helper = {}
        i = 0
        for item in val:
            helper['X' + str(i)] = str(item)
            i += 1
        func_helper: str = func
        for item in helper:
            func_helper = func_helper.replace(item, helper[item])
        res = eval(func_helper)
        return res

    @staticmethod
    def calc(r, x=[], y=[], n=0):
        r = 1/r
        helper = np.subtract(x, y)
        transpose = np.transpose(helper)
        d = np.dot(transpose, helper)
        d = np.power(d, r)
        return d


class NormalDistribution():

    def __init__(self, classes):
        self.classes = {}
        self.length = len(classes[0].z)
        for c in classes:
            self.classes[c.name] = c
            if(self.length != len(c.z)):
                raise Exception("length exception")


class MahalanobisDistance():

    def __init__(self, classes):
        self.classes = {}
        self.coovariances = {}
        self.length = len(classes[0].z)
        for c in classes:
            if(self.length != len(c.z)):
                raise Exception("length exception")
            self.classes[c.name] = c
            self.coovariances[c.name] = self.get_coovariance_matrix(c)

    def compare(self, x):
        x = np.array(x)
        result = {}
        for key in self.classes:
            cl = self.classes[key]
            x_mu = x - cl.z
            h = []
            inv_cov = np.linalg.inv(self.coovariances[key])
            helper = np.dot(x_mu, inv_cov)
            res = np.dot(helper, x_mu.T)
            h.append(res)
            result[key] = res
        return result

    @staticmethod
    def get_coovariance_matrix(cl):
        m = cl.items
        items = [[m[j][i] for j in range(len(m))]
                 for i in range(len(m[0])-1, -1, -1)]
        cov = np.cov(items)
        return cov
