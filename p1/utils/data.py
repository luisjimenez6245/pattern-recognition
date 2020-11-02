from models import Model, Characteristic

apple_size = 2250
orange_size = 2300

apple_weigths = Characteristic(
    name="weigth",
    data= {'80': 602, '85' : 1640, '90' : 8}
)

apple_color = Characteristic(
    name="color",
    data=[]
)

apple_form = Characteristic(
    name="form",
    data= {}
)


orange_weigth = Characteristic(
    name="weigth",
    data={'70': 627, '75': 1650, '80' : 23}
)

orange_color = Characteristic(
    name="color",
    data=[]
)

orange_form = Characteristic(
    name="form",
    data={}
)

orange = Model(
    name="orange",
    size =  orange_size,
    characteristics={
        'form': orange_form,
        'color': orange_color,
        'weigth': orange_weigth
    }
)

apple = Model(
    name="apple",
    size = apple_size,
    characteristics={
        'form':  apple_form,
        'color': apple_color,
        'weigth': apple_weigths
    }
)

