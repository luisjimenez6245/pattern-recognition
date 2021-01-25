from tkinter import *
from controllers import LearnMatrix
from PIL import Image, ImageTk
from utils import image_to_bitmap, bit_map_to_arr, add_noise, replace_from_bitmap
from tkinter.filedialog import askopenfilename


column_width = 10


class MainView(Frame):

    percentage = 5

    def __init__(self, learn_matrix: LearnMatrix,
                 selected_image="/Users/luis/Documents/GitHub/pattern-recognition/final/bitmaps/tres.bmp",
                 master=None, action=None):
        super().__init__(master=master)
        self.pack()
        self.selected_image = selected_image
        self.learn_matrix = learn_matrix
        self.w = Scale(self, from_=0, to=10, orient=HORIZONTAL,
                       command=self.change_percentage)
        self.w.grid(row=3, column=2)
        self.load_image(selected_image)
        Button(self, text="Cambiar Archivo", command=self.change_file).grid(
            row=3, column=0)
        Button(self, text="Calcular ruido", command=self.calc_percentage).grid(
            row=3, column=1)
        

    def change_percentage(self, e):
        self.percentage = int(e)
    
    def calc_percentage(self):
        bm_arr = image_to_bitmap(self.selected_image)
        self.images_noise(bm_arr)

    def change_file(self):
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename()
        print(filename)
        if(self.selected_image != filename):
            self.selected_image = filename
            self.load_image(filename)

    def images_noise(self, bm_arr):
        self.w.set(self.percentage)
        pl_bm_arr = add_noise(bm_arr, to_add=1, percentage=self.percentage)
        ms_bm_arr = add_noise(bm_arr, to_add=0, percentage=self.percentage)
        pl_bm_image = replace_from_bitmap(pl_bm_arr, before=1, after=254)
        ms_bm_image = replace_from_bitmap(ms_bm_arr, before=1, after=254)
        self.e = Label(self, width=column_width,
                       text="Con ruido +")
        self.e.grid(row=1, column=0)
        self.canvas_ms = Canvas(master=self, bg="white", width=100, height=100)
        self.canvas_ms.grid(row=1, column=1)
        self.e = Label(self, width=column_width * 2,
                       text=str(
                           self.learn_matrix.eval(
                               bit_map_to_arr(
                                   pl_bm_arr
                               )
                           )
                       ))
        self.e.grid(row=1, column=2)
        self.e = Label(self, width=column_width,
                       text="Con ruido -")
        self.e.grid(row=2, column=0)
        self.canvas_pl = Canvas(master=self, bg="white", width=100, height=100)
        self.canvas_pl.grid(row=2, column=1)
        self.e = Label(self, width=column_width * 2,
                       text=str(
                           self.learn_matrix.eval(
                               bit_map_to_arr(
                                   ms_bm_arr
                               )
                           )
                       ))
        self.e.grid(row=2, column=2)
        self.img_pl = ImageTk.PhotoImage(image=Image.fromarray(
            pl_bm_image
        ))
        self.img_ms = ImageTk.PhotoImage(image=Image.fromarray(
            ms_bm_image
        ))
        self.canvas_pl.create_image(0, 0, anchor="nw", image=self.img_pl)
        self.canvas_pl.image = self.img_pl
        self.canvas_ms.create_image(0, 0, anchor="nw", image=self.img_ms)
        self.canvas_ms.image = self.img_ms

    def load_image(self, selected_image):
        bm_arr = image_to_bitmap(selected_image)
        bm_image = replace_from_bitmap(bm_arr, before=1, after=254)

        self.e = Label(self, width=column_width,
                       text="Original")
        self.e.grid(row=0, column=0)
        self.canvas = Canvas(master=self, bg="white", width=100, height=100)
        self.canvas.grid(row=0, column=1)
        self.e = Label(self, width=column_width * 2,
                       text=str(
                           self.learn_matrix.eval(
                               bit_map_to_arr(
                                   bm_arr
                               )
                           )
                       ))
        self.e.grid(row=0, column=2)

        self.img = ImageTk.PhotoImage(image=Image.fromarray(
            bm_image
        ))
        
        self.canvas.create_image(0, 0, anchor="nw", image=self.img)
        self.canvas.image = self.img
        self.images_noise(bm_arr)
        
