import tkinter as tk


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

    def user_data(self):
        self.clear_view()
        self.destroy()
        

    def test_view(self):
        self.clear_view()
        print("prueba")


root = tk.Tk()
root.geometry("500x200")
window = App(root)
window.master.title("Clasificador Bayersiano")
window.mainloop()
