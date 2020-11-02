from tkinter import Frame


class ClassView(Frame):

    items = []

    def __init__(self, master=None):
        super().__init__(master=master)
        
        