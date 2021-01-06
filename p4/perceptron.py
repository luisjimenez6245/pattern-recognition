class percept:

    def __init__(
        self,
        umbral = 0,
        taza_apren = 0,
        pesos  = [],
        conjunto = []
    ):
        super().__init__()
        self.umbral = umbral
        self.taza_apren = taza_apren
        self.pesos = pesos
        self.conjunto = conjunto

    """ Operaciones """

    # devuelve la suma de los productos de muestra * peso
    def producto_punto(self, valores):
        resultado = sum(valor * peso for valor, peso in zip(valores, self.pesos))
        return resultado

    def hardlim(self, val):
        if(self.umbral >= val):
            return self.umbral
        else:
            return 1

    # Modifica los pesos n veces para lograr aprender
    def aprender(self):
        print(" Aprendiendo...")
        ciclo = 0
        while True:
            ciclo += 1
            contador_de_errores = 0
            for vector_de_entrada, salida_deseada in self.conjunto:
                resultado = self.hardlim(
                    self.producto_punto(vector_de_entrada)
                )
                error = salida_deseada - resultado
                if error != 0:
                    contador_de_errores += 1
                    for indice, valor in enumerate(vector_de_entrada):
                        self.pesos[indice] += self.taza_apren * error * valor
            if contador_de_errores == 0:
                break
        print("Ya aprendí, los pesos obtenidos son: ")
        print(self.pesos)

    # Clasifica el elemento con los pesos ya aprendidos
    def clasificar(self, desconocido):
        resultado = self.hardlim(
            self.producto_punto(desconocido)
        )
        if resultado <= self.umbral:
            print("\n\n*** Pertenece a la region del cielo ***\n\n")
        else:
            print("\n\n*** Pertenece a la region de la zona boscosa ***\n\n")
