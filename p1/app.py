from utils.data import apple, orange, mango
from utils.menu import is_int, is_float
from models import Model, Characteristic
from controllers import Classifier
from collections import OrderedDict

def get_models(names = [], characs = []):
    size = 0
    char_dict = {}
    for charc in characs:
        key = ""
        opc = "Y"
        keys = []
        print("A continuación se te pediran los valores para la caracterítica  " + charc )
        while(opc == "Y"):
            key = input("Ingresa uno de los posbiles valores para la caracterítica:\n")
            if(key  not in keys):
                keys.append(key)
            if(len(keys) > 1):
                opc =  str(input("Deseas agregar otro valor? (Y es si y cualquier otra tecla es no):\n")).upper()
        char_dict[charc] =  keys
    models = []
    for name in names:
        size = 0
        print("A continuación se te pediran los valores para las caracteristicas de la clase  " + name)
        char_dict_model = {}
        for charc in char_dict:
            data =  char_dict[charc]
            result_data = {}
            for item in data:
                value =  str(input("Ingresa la cantidad para el valor "+ item +" de la muestra de la caracteristica " + charc + " de la clase " +  name + ": \n"))
                while(not is_int(value)):
                    value =  str(input("Ingresa la cantidad para el valor "+ item +" de la muestra de la caracteristica " + charc + " de la clase " +  name + ": \n"))
                size += int(value)
                result_data[item] = int(value)
            char_dict_model[charc] = Characteristic(
                name = charc,
                data = result_data
            )
        models.append(
            Model(
                name = name,
                size = size,
                characteristics = char_dict_model
            )
        )
    return models


def print_table(data, models):
    table = []
    for key in data:
        helper = [""]
        items = data[key]
        items:dict = data[key]
        items = OrderedDict(sorted(items.items()))
        for item in items:
            helper.append(str(item))
        table.append(helper)
        for model in models:
            name = model.name
            helper = [name]
            for item in items:
                d= items[item]
                if(name in d):
                    helper.append(d[name])
                else:
                    helper.append(str(0))
            table.append(helper)
    for row in table:
        to_print = ""
        for col in row:
            to_print += str(col) + "\t"
        print(to_print)  
    

def main(models = []):
    classifier = Classifier(models)
    data = classifier.data
    for model in models:
        print(model.name)
    should_continue = True
    key = list(models[0].characteristics.keys())[0]
    while(should_continue):
        print("Datos:")
        print_table(data, models)
        _data = str(input("Ingresa el valor de la caractetistica " + key + " a sacar su probabilidad:\n"))
        p = classifier.get_probability(_data, key)
        if(len(p) == 0):
            print("No hay probabilidad para esa caracteristica")
        for item in p:
            print("Existe el "+ str(p[item]) + " de probalidad  de que sea " + str(item))
        should_continue =  (str(input("Deseas agregar otro dato? (Y es si y cualquier otra tecla es no)\n")).upper() == "Y")
        


if __name__ == "__main__":
    models = []
    print("Bienvenido al clasificador bayesiano")
    opc = input("Presiona 1 para ver el programa con los valores de prueba o cualquier otra tecla para ingresar los valores propios:\n")
    while (not is_int(opc)):
        opc = input("Presiona 1 para ver el programa con los valores de prueba o cualquier otra tecla para ingresar los valores propios:\n")

    opc = int(opc)
    if(opc == 1):
        print("Seleccionaste los valores de prueba")
        print("Este programa, se basa en el peso de las siguientes frutas:")
        models = [apple, mango, orange]
    else:
        print("Seleccionaste ingresar los valores")
        objs_names = []
        char_names = []
        models = []
        opc = "Y"
        while(opc == "Y"):
            print("Vas a ir creando poco a poco los objetos a clasificar (mínimo son dos clases):")
            name  = ""
            should_continue = True
            while(should_continue):
                name = str(input("Escribe el nombre de la clase "+ str(len(objs_names) + 1 )+ " del clasificador: \n"))
                if(len(name) == 0  or name in objs_names):
                    print("Nombre no valido, puede que tu nombre valido o que hayas ingresado otro igual")
                else:
                    objs_names.append(name)
                if(len(objs_names) >= 2):
                    should_continue =  (str(input("Deseas agregar otra clase? (Y es si y cualquier otra tecla es no)\n")).upper() == "Y")
            should_continue = True
            while(should_continue):
                name =  str(input("Escribe el nombre del rasgo a clasificar: \n"))
                if(len(name) == 0  or name in char_names):
                    print("Nombre no valido, puede que tu nombre valido o que hayas ingresado otro igual")
                else:
                    char_names.append(name)
                should_continue = not (len(char_names) == 1)
            should_continue = True
            models = get_models(objs_names, char_names)
            opc = "N"
            
    main(models)
    print("Gracias por usar el programa")