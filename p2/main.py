from views import MainView
from utils.data import classes
import tkinter as tk


root = tk.Tk()
root.geometry("800x800")
window = MainView(master = root, classes= classes)
window.master.title("Clasificador Bayersiano")
window.mainloop()
window.mainloop()