from models import Pattern
from controllers import LearnMatrix
from utils import bit_map_to_arr, image_to_bitmap


def test_case():
    p1 = Pattern([1, 0, 0], [1, 0, 1, 0, 1])
    p2 = Pattern([0, 1, 0], [1, 1, 0, 0, 1])
    p3 = Pattern([0, 0, 1], [1, 0, 1, 1, 0])
    m = LearnMatrix([p1, p2, p3])
    print(m.mat)
    print(m.eval([1, 0, 1, 0, 1]))
    print(m.eval([1, 1, 0, 0, 1]))
    print(m.eval([1, 0, 1, 1, 0]))
    m.add_to_learn(Pattern([1, 0, 0], [0, 1, 0, 1, 1]))
    print(m.mat)
    print(m.eval([1, 0, 1, 0, 1]))
    print(m.eval([1, 1, 0, 0, 1]))
    print(m.eval([1, 0, 1, 1, 0]))
    print(m.eval([0, 1, 0, 1, 1]))
    m.add_to_learn(Pattern([0, 0, 1], [0, 0, 1, 0, 1]))
    print(m.mat)

if __name__ == "__main__":
    p0 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 0, 1], bit_map_to_arr(image_to_bitmap("./bitmaps/cero.bmp")))
    p1 = Pattern([0, 0, 0, 0, 0, 0, 0, 0, 1, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/uno.bmp")))
    p2 = Pattern([0, 0, 0, 0, 0, 0, 0, 1, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/dos.bmp")))
    p3 = Pattern([0, 0, 0, 0, 0, 0, 1, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/tres.bmp")))
    p4 = Pattern([0, 0, 0, 0, 0, 1, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/cuatro.bmp")))
    p5 = Pattern([0, 0, 0, 0, 1, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/cinco.bmp")))
    p6 = Pattern([0, 0, 0, 1, 0, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/seis.bmp")))
    p7 = Pattern([0, 0, 1, 0, 0, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/siete.bmp")))
    p8 = Pattern([0, 1, 0, 0, 0, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/ocho.bmp")))
    p9 = Pattern([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], bit_map_to_arr(image_to_bitmap("./bitmaps/nueve.bmp")))
    m = LearnMatrix([p1, p2, p3, p4, p5, p6, p7, p8, p9,])
    print(m.mat)
    print(m.eval(bit_map_to_arr(image_to_bitmap("./bitmaps/uno.bmp"))))