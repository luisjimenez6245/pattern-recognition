
class percept:
    def __init__(self) -> None:
        super().__init__()
        self.umbral = 0
        self.taza_apren = 0
        self.pesos = []
        self.conjunto = []

    """ Getters and setters """
    def set_Umbral( self, umbral ):
        self.umbral = umbral

    def set_pesos( self, pesos ):
        self.pesos = pesos    

    def set_conjunto( self, conjunto ):
        self.conjunto = conjunto

    def set_Aprendizaje( self, aprender ):
        self.taza_apren = aprender

    """ Operaciones """

    ### devuelve la suma de los productos de muestra * peso
    def producto_punto( self, valores, pesos):
        return sum( valor * peso for valor, peso in zip(valores, pesos))

    ### Modifica los pesos n veces para lograr aprender
    def aprender( self ):
        print( " Aprendiendo..." )
        ciclo = 0
        while True:
            ciclo += 1
            contador_de_errores = 0
            #print( '-' * 60 )
            #print( "ciclo: {}".format( ciclo ) )
            for vector_de_entrada, salida_deseada in self.conjunto:
                #print( vector_de_entrada )
                #print( self.pesos )
                error = 0
                if self.producto_punto( vector_de_entrada, self.pesos ) <= self.umbral and salida_deseada == 0:
                    error = 1
                if self.producto_punto( vector_de_entrada, self.pesos ) >= self.umbral and salida_deseada == 1:
                    error = -1
                if error != 0:
                    contador_de_errores += 1
                    for indice, valor in enumerate(vector_de_entrada):
                        self.pesos[indice] += self.taza_apren * error * valor
            if contador_de_errores == 0:
                break
        print( "Ya aprendí, los pesos obtenidos son: " )
        print( self.pesos )
            
    ### Clasifica el elemento con los pesos ya aprendidos
    def clasificar( self, desconocido ):
        if self.producto_punto( desconocido, self.pesos ) > self.umbral:
            print( "\n\n*** Pertenece a la region del cielo ***\n\n" )
        if self.producto_punto( desconocido, self.pesos ) < self.umbral:
            print( "\n\n*** Pertenece a la region de la zona boscosa ***\n\n" )