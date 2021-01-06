"""
# Creado por:
# Jovanny Wilver Cortez Enriquez
# 
# 
###### Algoritmo del perceptron simple ######
"""

from perceptron import percept

if __name__ == '__main__':

    ### inicializando ###

    conjunto = [
        ((200, 160, 120), 0),
        ((210, 170, 130), 0),
        ((215, 172, 133), 0),
        ((210, 165, 134), 0),
        ((198, 177, 138), 0),
        ((90, 130, 60), 1),
        ((92, 138, 54), 1),
        ((87, 128, 66), 1),
        ((91, 134, 60), 1),
        ((85, 123, 55), 1),
    ]

    p = percept(
        umbral=0,
        taza_apren=10**(-4),
        pesos=[0, 0, 0],
        conjunto=conjunto
    )

    #### Aprendiendo #####
    p.aprender()

    #### clasificar desconocido ####
    desconocido = []
    while True:
        desconocido = []
        print("Introduzca la palabra 'cerrar' para finalizar o de lo contrario")
        vectord = input("Introduzca los valores separados por comas: \t")
        vectord = vectord.replace(' ', '')
        if vectord == "cerrar":
            print('*' * 20)
            print("*   NOS VEMOS!!!!  *")
            print('*' * 20)
            break
        else:
            try:
                desconocido.extend(vectord.split(","))
                desconocido = [int(x) for x in desconocido]
                p.clasificar(desconocido)
            except:
                pass
