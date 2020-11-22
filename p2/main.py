from views import MainView
from utils.data import classes
import tkinter as tk


root = tk.Tk()
root.geometry("500x200")
window = MainView(master = root, classes= classes)
window.master.title("Clasificador Bayersiano")
window.mainloop()
window.mainloop()