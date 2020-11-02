from tkinter import Frame, Entry, Label, END
from controllers import Classifier
from collections import OrderedDict

class MainView(Frame):

    items = []
    classifier = None

    def __init__(self, models=[], master=None):
        super().__init__(master=master)
        self.pack()
        total_rows = len(models)
        total_columns = 10
        column_width = 12
        self.classifier = Classifier(models)
        data = self.classifier.data
        for key in data:
            self.e  = Label(self, width =  column_width,  fg='blue', text = ("Modelo\\" + key).upper()) 
            self.e.grid(row=0, column=0) 
            items:dict = data[key]
            items = OrderedDict(sorted(items.items()))
            column_count = 1
            for item in items:
                self.e  = Label(self, width =  column_width, fg='red', text = str(item)) 
                self.e.grid(row=0, column=column_count)
                column_count +=1 
            count = 1
            for model in models:
                self.e  = Label(self, width =  column_width, fg='red', text = model.name.upper()) 
                self.e.grid(row=count, column=0) 
                column_count = 1
                for item in items:
                    d = items[item]
                    if(model.name  in d):
                        self.e = Label(self, width =  column_width, text = str(d[model.name]))
                    else:
                        self.e = Label(self, width =  column_width, text = str(0))
                    self.e.grid(row=count, column=column_count)
                    column_count +=1 
                count += 1
            