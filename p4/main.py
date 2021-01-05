"""
# Creado por:
# Jovanny Wilver Cortez Enriquez
# 
# 
###### Algoritmo del perceptron simple ######
"""

from perceptron import percept

if __name__ == '__main__':
    p = percept()

    ### inicializando ###
    umbral = 0
    taza_apren = 10**(-4)
    pesos = [0,0,0,0]
    conjunto = [ ( ( 1, 200, 160, 120 ), 0 ), 
                ( ( 1, 210, 170, 130 ), 0 ), 
                ( ( 1, 215, 172, 133 ), 0 ),
                ( ( 1, 210, 165, 134 ), 0 ),
                ( ( 1, 198, 177, 138 ), 0 ),
                ( ( 1, 90, 130, 60 ), 1 ), 
                ( ( 1, 92, 138, 54 ), 1 ),
                ( ( 1, 87, 128, 66 ), 1 ),
                ( ( 1, 91, 134, 60 ), 1 ),
                ( ( 1, 85, 123, 55 ), 1 ),]

    #### Aprendiendo #####
    p.set_Umbral( umbral )
    p.set_Aprendizaje( taza_apren )
    p.set_pesos( pesos )
    p.set_conjunto( conjunto )
    p.aprender()

    #### clasificar desconocido ####
    desconocido = [1]
    while True:
        desconocido = [1]
        print( "Introduzca la palabra 'cerrar' para finalizar o de lo contrario" )
        vectord = input("Introduzca los valores separados por comas: \t")
        if vectord == "cerrar":
            print( '*' * 20 )
            print( "*   NOS VEMOS!!!!  *")
            print( '*' * 20 )
            break
        else:
            desconocido.extend( vectord.split(",") )
            desconocido = [ int(x) for x in desconocido ]
            p.clasificar( desconocido )
