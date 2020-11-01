from models import Model, Characteristic
from utils import gen_random_arr
from controllers import Grapher

apple_size = 2000
orange_size = 1200

apple_weigths = Characteristic(
    name="weigth",
    data=gen_random_arr(apple_size, 180, 220)
)

apple_color = Characteristic(
    name="color",
    data=[]
)

apple_form = Characteristic(
    name="form",
    data=gen_random_arr(apple_size, .1, .5)
)

apple = Model(
    name="apple",
    size =  apple_size,
    p = 0,
    characteristics={
        'form':  apple_form,
        'color': apple_color,
        'weigths': apple_weigths
    }
)

orange_weigth = Characteristic(
    name="weigth",
    data=gen_random_arr(orange_size, 257, 300)
)

orange_color = Characteristic(
    name="color",
    data=[]
)

orange_form = Characteristic(
    name="form",
    data=gen_random_arr(orange_size, .8, 1)
)

orange = Model(
    name="orange",
    size =  orange_size,
    p = 0,
    characteristic={
        'form': orange_form,
        'color': orange_color,
        'weigth': orange_weigth
    }
)

total_objs =  orange.size +  apple.size

orange.p =  orange.size  / total_objs
apple.p = apple.size / total_objs


Grapher.bell_graph(orange_weigth.data, orange_size)
print(orange.p)