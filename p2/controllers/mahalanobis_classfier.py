import numpy as np

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
