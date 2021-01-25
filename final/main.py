from views import MainView
import tkinter as tk
from models import Pattern
from controllers import LearnMatrix
from utils import bit_map_to_arr, image_to_bitmap

classes = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

p0 = Pattern(classes[0] , bit_map_to_arr(
    image_to_bitmap("./bitmaps/cero.bmp")))
p1 = Pattern(classes[1], bit_map_to_arr(
    image_to_bitmap("./bitmaps/uno.bmp")))
p2 = Pattern(classes[2], bit_map_to_arr(
    image_to_bitmap("./bitmaps/dos.bmp")))
p3 = Pattern(classes[3], bit_map_to_arr(
    image_to_bitmap("./bitmaps/tres.bmp")))
p4 = Pattern(classes[4], bit_map_to_arr(
    image_to_bitmap("./bitmaps/cuatro.bmp")))
p5 = Pattern(classes[5], bit_map_to_arr(
    image_to_bitmap("./bitmaps/cinco.bmp")))
p6 = Pattern(classes[6], bit_map_to_arr(
    image_to_bitmap("./bitmaps/seis.bmp")))
p7 = Pattern(classes[7], bit_map_to_arr(
    image_to_bitmap("./bitmaps/siete.bmp")))
p8 = Pattern(classes[8], bit_map_to_arr(
    image_to_bitmap("./bitmaps/ocho.bmp")))
p9 = Pattern(classes[9], bit_map_to_arr(
    image_to_bitmap("./bitmaps/nueve.bmp")))
m = LearnMatrix([ p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, ] ,classes=classes)
root = tk.Tk()
root.geometry("800x500")


window = MainView(master=root, learn_matrix = m)
window.master.title("Clasificador Bayersiano")
window.mainloop()
window.mainloop()
