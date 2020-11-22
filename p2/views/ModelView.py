from tkinter import Frame


class ModelView(Frame):

    model = None

    def __init__(self, name: str, characteristics: list, master=None):
        super().__init__(master=master)
        self.grid()
        self.master.title(name)
        self.model = Model(
            ''
        )
