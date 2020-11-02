import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("", self.contents.get())

root = tk.Tk()
window = App(root)
window.master.title("Clasificador Bayersiano")
window.mainloop()