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
