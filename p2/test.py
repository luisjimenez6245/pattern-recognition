from controllers import EuclidianClassifier, MahalanobisDistance, NormalClassifier, MetricClassifier
from utils.data import classes

if __name__ == "__main__":

    classfier = NormalClassifier(classes)
    x = [85, 123, 55]
    res = (classfier.compare(x))
    print(res)
    classfier = EuclidianClassifier(classes)
    res = (classfier.compare(x))
    print(res)
    classfier = MahalanobisDistance(classes)
    res = (classfier.compare(x))
    print(res)
    classfier = NormalClassifier(classes)
    res = (classfier.compare(x))
    print(res)
    classfier = MetricClassifier(classes)
    res = (classfier.euclidian(x))
    print(res)
    res = (classfier.city_block(x))
    print(res)
    res = (classfier.infinity(x))
    print(res)