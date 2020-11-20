import tkinter as tk

class ClassView(tk.Frame):

    items = []

    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack(expand=True)
        self.class_name = tk.Entry()
        self.class_name.pack()
        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        self.class_name["textvariable"] = self.contents
        self.class_name.bind('<Key-Return>', self.print_contents)