class BaseClassifier():

    classes = {}

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
        raise Exception("not implemented")

    def get_class(self, x):
        res = self.compare(x)
        res = {k: v for k, v in sorted(res.items(), key=lambda item: item[1])}
        return list(res.keys())[0]
    

    @staticmethod
    def get_first_element(x):
        res = {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        return list(res.keys())[0]