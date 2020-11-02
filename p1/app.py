from utils.data import apple, orange, mango
from utils.menu import is_int
"""
import tkinter as tk
from views import ClassView, MainView

class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=True)
        pady = 10
        padx = 10
        self.btn_test = tk.Button(
            self,
            text="Con datos de prueba",
            command=self.test_view,
            pady=pady,
            padx=padx
        )
        self.btn_test.pack()
        self.btn_user = tk.Button(
            self,
            text="Con datos del usuario",
            command=self.user_data,
            pady=pady,
            padx=padx
        )
        self.btn_user.pack()

    def clear_view(self):
        self.btn_test.destroy()
        self.btn_user.destroy()
        self.destroy()

    def user_data(self):
        self.clear_view()
        frame = ClassView()
        frame.tkraise()


    def test_view(self):
        self.clear_view()
        frame = MainView(
            models = [
                mango, 
                apple,
                orange
            ]
        )
        frame.tkraise()


root = tk.Tk()
root.geometry("800x200")
window = App(root)
window.master.title("Clasificador Bayersiano")
window.mainloop()
"""
print("Bienvenido al clasificador bayesiano")
opc = input("Presiona 1 para ver el programa con los valores de prueba y 2 para ingresar los valores propios:")
while (not is_int(opc)):
    opc = input("Presiona 1 para ver el programa con los valores de prueba y 2 para ingresar los valores propios:")

opc = int(opc)
if(opc == 1):
    print("Seleccionaste los valores de prueba")
    print("Este programa, se basa en el peso de las siguientes frutas:")
    objs = [apple, mango, orange]
    for obj in objs:
        print("\t" + obj.name)
    
    
else:
    print("Seleccionaste ingresar los valores")

