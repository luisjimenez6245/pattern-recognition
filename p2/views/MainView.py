from tkinter import Frame, Entry, Label, END
from collections import OrderedDict
from controllers import EuclidianClassifier, MahalanobisDistance, NormalClassifier, CityBlockClassifier, InfinityClassifier


class TableView(Frame):

    def __init__(self, classes=[], master=None):
        super().__init__(master=master)
        self.pack()
        column_width = 3
        self.e = Label(self, width=column_width,  fg='blue',
                           text=("").upper())
        self.e.grid(row=0, column=0)
        characs = classes[0].characteristics
        total_char = 2
        for c in characs:
            self.e = Label(self, width = column_width, text = c)
            self.e.grid(row = total_char, column = 0)

            total_char += 1

        total_items = 1
        for cl in classes:
            items = cl.items 
            self.e = Label(self, width = column_width, text = cl.name)
            self.e.grid(row = 0, column = total_items)

            item_counter = 1
            for item in items:
                l = "X" + str(item_counter)
                self.e = Label(self, width=column_width,
                               fg='blue', text= l)
                self.e.grid(row  = 1, column = total_items)
                char_count = 0
                for data in item:
                    self.e = Label(self, width=column_width,
                               fg='red', text=str(data))
                    self.e.grid(row = 2 + char_count, column = total_items)
                    char_count += 1
                item_counter +=1
                total_items += 1


class MainView(Frame):

    items = []
    classifiers = {}

    def __init__(self, classes=[], master=None):
        super().__init__(master=master)
        self.pack()
        self.classifiers = {
            'Euclidiano': EuclidianClassifier(classes),
            'Mahalanobis': MahalanobisDistance(classes),
            'Normal': NormalClassifier(classes),
            'CityBlock': CityBlockClassifier(classes),
            'Infinity': InfinityClassifier(classes)
        }
        TableView(classes= classes, master=self).pack()
