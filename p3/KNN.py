
import math


class KNN:
    def __init__(self):
        super().__init__()
        self.clases = 0
        self.elemento = []
        self.muestras = []
        self.distancias = []
        self.ordenado = []

    #setters & getters
    def set_num_clases(self, clases):
        self.clases = clases

    def set_muestras(self, muestras):
        self.muestras = muestras

    def set_elemento(self, elemento):
        self.elemento = elemento

    """---------------operaciones------------"""
    # Calcula las ditancias de cada muestra

    def calcular_distancia(self):
        for d in self.muestras:
            n = d[1]
            x = self.elemento[0] - d[2][0]
            y = self.elemento[1] - d[2][1]
            dis = math.sqrt(x**2 + y**2)
            self.distancias.append([dis, n])

    # ordena las distancias calculadas
    def ordenar(self):
        self.ordenado = self.distancias
        self.ordenado.sort()

    # busca en las muestras un elemento
    def buscar(self, elemento):
        index = 0
        for n in self.muestras:
            if(elemento in n):
                return index
            index += 1

    # busca el elemento en una repeticion
    def buscar_ele(self, elemento, rango):
        index = 0
        for n in rango:
            if(elemento in n):
                return True, index
            index += 1
        return False, 0

    # busca la clase con mayor repeticion
    def buscar_mayor(self, rango):
        index = 0
        pos = 0
        mayor = rango[0][1]
        for n in rango:
            if(n[1] > mayor):
                mayor = n[1]
                index = pos
            pos += 1
        return index

    # busca la clase con menor distancia
    def buscar_menor(self, rango):
        index = 0
        pos = 0
        menor = rango[0][1]
        for n in rango:
            if(n[1] < menor):
                menor = n[1]
                index = pos
            pos += 1
        return index

    # Clasifica el elemento
    def clasificar(self, k):
        rangoK = []
        mensaje = ""
        repeticion = []

        if(k == 1):
            indice = self.buscar(self.ordenado[0][1])
            mensaje = "Pertenece a la clase {}".format(
                self.muestras[indice][0])

        else:
            for i in range(0, k):
                rangoK.append(self.ordenado[i])

            for i in rangoK:
                indice = self.buscar(i[1])
                if repeticion:
                    [existe, ind] = self.buscar_ele(
                        self.muestras[indice][0], repeticion)
                    if existe:
                        repeticion[ind][1] += 1
                    else:
                        repeticion.append([self.muestras[indice][0], 1])
                else:
                    repeticion.append([self.muestras[indice][0], 1])

            indice = self.buscar_mayor(repeticion)
            mensaje = "Pertenece a la clase {}".format(
                self.muestras[indice][0])
        # puede retornar el mensaje para que se visualize
        print(mensaje)

    """---------------Desempate----------------"""
    # distancia minima

    def distancia_minima(self, k):
        rangoK = []
        mensaje = ""
        repeticion = []
        distancias = []

        for i in range(0, k):
            rangoK.append(self.ordenado[i])

        for i in rangoK:
            indice = self.buscar(i[1])
            if repeticion:
                [existe, ind] = self.buscar_ele(
                    self.muestras[indice][0], repeticion)
                if existe:
                    repeticion[ind][1] += 1
                    repeticion[ind][2][0] += self.muestras[indice][2][0]
                    repeticion[ind][2][1] += self.muestras[indice][2][1]
                else:
                    repeticion.append(
                        [self.muestras[indice][0], 1, self.muestras[indice][2]])
            else:
                repeticion.append(
                    [self.muestras[indice][0], 1, self.muestras[indice][2]])

        for r in repeticion:
            x = r[2][0] / r[1]
            y = r[2][1] / r[1]
            dis = math.sqrt(
                ((self.elemento[0] - x)**2) + ((self.elemento[1] - y)**2))
            distancias.append([dis, r[0]])

        indice = self.buscar_menor(distancias)
        mensaje = "Pertenece a la clase {}".format(self.muestras[indice][0])
        # retorna mensaje si se requiere
        print(mensaje)

    # distancia media
    def distancia_media(self, k):
        rangoK = []
        mensaje = ""
        repeticion = []
        distancias = []

        for i in range(0, k):
            rangoK.append(self.ordenado[i])

        for i in rangoK:
            indice = self.buscar(i[1])
            if repeticion:
                [existe, ind] = self.buscar_ele(
                    self.muestras[indice][0], repeticion)
                if existe:
                    repeticion[ind][1] += 1
                    repeticion[ind][2] += i[0]
                else:
                    repeticion.append([self.muestras[indice][0], 1, i[0]])
            else:
                repeticion.append([self.muestras[indice][0], 1, i[0]])

        for r in repeticion:
            d = r[2] / r[1]
            distancias.append([d, r[0]])

        indice = self.buscar_menor(distancias)
        mensaje = "Pertenece a la clase {}".format(self.muestras[indice][0])
        # retorna mensaje si se requiere
        print(mensaje)

    # pesos

    # visualizar info
    def mostrar_muestras(self):
        for c in self.muestras:
            print("clase: {} numM: {} muestra: {}".format(c[0], c[1], c[2]))

    def mostrar_elemento(self):
        print(self.elemento)

    def mostrar_distancias(self):
        print(self.distancias)

    def mostrar_ordenado(self):
        print(self.ordenado)


if __name__ == "__main__":
    k = KNN()
