from controllers.metric_classifier import EuclidianClassifier, MahalanobisDistance
from utils.data import classes

if __name__ == "__main__":

    classfier = MahalanobisDistance(classes)
    x = [85, 123, 55]
    res = (classfier.compare(x))
    print(res)
    res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
    cl = list(res.keys())[0]
    result_class = res[cl]

    print(result_class)
