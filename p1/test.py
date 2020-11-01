from models import Model, Characteristic
from utils import gen_random_arr
from controllers import Grapher

apple_sizes = Characteristic(
    name="size",
    data=gen_random_arr(100, 180, 220)
)

apple_color = Characteristic(
    name="color",
    data=[]
)

apple_form = Characteristic(
    name="form",
    data=gen_random_arr(100, .1, .5)
)

apple = Model(
    name="apple",
    characteristics={
        'form':  apple_form,
        'color': apple_color,
        'sizes': apple_sizes
    }
)

orange_size = Characteristic(
    name="size",
    data=gen_random_arr(100, 257, 300)
)

orange_color = Characteristic(
    name="color",
    data=[]
)

orange_form = Characteristic(
    name="form",
    data=gen_random_arr(100, .8, 1)
)

orange = Model(
    name="orange",
    characteristic={
        'form': orange_form,
        'color': orange_color,
        'size': orange_size
    }
)

Grapher.graph(orange_size.data)