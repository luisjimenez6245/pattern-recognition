import numpy as np
import matplotlib.pyplot as plt
from utils import gen_count

class Grapher():

    @classmethod
    def graph(cls, data, size=100):
        x = gen_count()
        plt.figure(1)
        data.sort()
        plt.plot(x, data)
        ax = plt.gca()
        ax.set_xticklabels([])
        plt.show()

    @classmethod
    def bell_graph(cls, data, size =  100):
        data.sort()
        a = np.array(data)
        unique, counts = np.unique(a, return_counts=True)
        y = dict(zip(unique, counts))
        x =  gen_count(len(y))
        plt.plot(x, y.values())
        ax = plt.gca()
        ax.set_xticklabels([])
        plt.show()
        