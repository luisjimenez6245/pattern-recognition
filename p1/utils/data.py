from models import Model, Characteristic

apple_size = 2250
orange_size = 2300
mango_size = 2450

apple_weigth = Characteristic(
    name="weigth",
    data= {'80': 602, '85' : 1640, '90' : 8}
)

orange_weigth = Characteristic(
    name="weigth",
    data={'70': 627, '75': 1650, '80' : 23}
)

mango_weigth = Characteristic(
    name="weigth",
    data={'85': 10, '90': 2035, '95' : 405}
)

orange = Model(
    name="orange",
    size =  orange_size,
    characteristics={
        'weigth': orange_weigth
    }
)

apple = Model(
    name="apple",
    size = apple_size,
    characteristics={
        'weigth': apple_weigth
    }
)

mango = Model(
    name="mango",
    size = mango_size,
    characteristics={
        'weigth': mango_weigth
    }
)
