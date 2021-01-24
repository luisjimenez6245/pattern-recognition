import numpy as np
from models import Pattern


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
