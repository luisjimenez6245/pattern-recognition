from controllers import EuclidianClassifier, MahalanobisDistance, NormalClassifier, CityBlockClassifier, InfinityClassifier
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
    classfier = CityBlockClassifier(classes)
    res = (classfier.compare(x))
    print(res)
    classfier = InfinityClassifier(classes)
    res = (classfier.compare(x))
    print(res)