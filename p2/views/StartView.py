from tkinter import Frame, Entry, Label, END, Button

class StartView(Frame):

    items = []

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack(expand=True)
        p = Button(master=self, text = "Prueba")
        ingresar = Button(master=self, text = "Ingresar Datos")
        p.pack()
        ingresar.pack()
    