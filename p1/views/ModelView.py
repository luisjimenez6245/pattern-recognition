from tkinter import Frame


class ModelView(Frame):

    def __init__(self, master=None,):
        super().__init__(master=master)
        self.grid()
        self.master.title("Clase")

