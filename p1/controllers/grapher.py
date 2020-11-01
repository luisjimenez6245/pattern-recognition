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
