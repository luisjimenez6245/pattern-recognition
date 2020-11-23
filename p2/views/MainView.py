from tkinter import Frame, Entry, Label, Button, END
from .utils import TableView
from collections import OrderedDict
from controllers import EuclidianClassifier, MahalanobisDistance, NormalClassifier, CityBlockClassifier, InfinityClassifier


class EntryView(Frame):

    entries = {}
    action = None

    def __init__(self, chars=[], master=None, action=None):
        super().__init__(master=master)
        self.pack()
        self.action = action
        total_char = 0
        for char in chars:
            Label(master=self, text=char).grid(row=total_char, column=0)
            self.entries[char] = Entry(master=self)
            self.entries[char].insert(0, '0')
            self.entries[char].grid(row=total_char, column=1)
            total_char += 1
        Button(self, text="Calcular", command=self.calc).grid(
            row=total_char + 1, column=0)

    def calc(self):
        res = {}
        for char in self.entries:
            res[char] = int(self.entries[char].get())
        if(self.action is not None):
            self.action(res)


class ClassifierResultView(Frame):
    res = None

    def __init__(self, master=None, classifier=None, name=''):
        super().__init__(master=master)
        self.pack()
        self.classifier = classifier
        Label(master=self, text=name).pack()
        self.res = Label(master=self, text='')
        self.res.pack()

    def calc(self, x):
        res = self.classifier.compare(x)
        c = self.classifier.get_first_element(res)
        text = "PERTENECE A:{} ".format(c)
        for item in res:
            pass
            #text += "{}:{:.2f} ".format(item, res[item])
        self.res['text'] = text


class MainView(Frame):

    items = []
    classifiers = {}
    entry_value = {}

    def __init__(self, classes=[], master=None):
        super().__init__(master=master)
        self.pack()
        classifiers = {
            'Euclidiano': EuclidianClassifier(classes),
            'Mahalanobis': MahalanobisDistance(classes),
            'Normal': NormalClassifier(classes),
            'CityBlock': CityBlockClassifier(classes),
            'Infinity': InfinityClassifier(classes)
        }
        Label(master=self, text="Datos").pack()
        self.table = TableView(classes=classes, master=self).pack()
        chars = classes[0].characteristics
        Label(master=self, text="Ingresa un Vector").pack()
        EntryView(chars=chars, master=self, action=self.calc).pack()
        for cl in classifiers:
            self.classifiers[cl] = ClassifierResultView(
                classifier=classifiers[cl], name=cl)
            self.classifiers[cl].pack()

    def calc(self, item):
        x = list(item.values())
        for cl in self.classifiers:
            self.classifiers[cl].calc(x)
