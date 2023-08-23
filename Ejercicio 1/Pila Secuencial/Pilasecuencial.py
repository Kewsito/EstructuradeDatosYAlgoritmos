import numpy as np

class Pila:
    __arreglo = None
    __tope = 0
    __tamaño : int

    def __init__(self, tamaño : 20):
        self.__arreglo = np.empty(tamaño, dtype= int)
        self.__tope = 0 
        self.__tamaño = tamaño

    def insertar (self,dato):
        if self.__tope == self.__tamaño: # Si el tope es igual al tamaño
            raise Exception ("PILA LLENA") # la pila esta llena
        self.__arreglo[self.__tope] = dato  # pone el dato en la punta de la pila
        self.__tope =+1 # Aumenta en uno el tope del arreglo

    def getTamaño(self):
        return self.__tamaño
    
    def deleteValue(self):

        if self.__tope == 0:
            raise Exception("PILA VACIA")
        self.__tope=-1 # descuenta en 1 la pila
        return self.__arreglo[self.__tope] # devuelve el valor de la punta de la pila
    
if __name__ == '__main__':
    P = Pila()
    P.insertar("Kevinsito")
    P.insertar("Kevinsito2")
    P.deleteValue()
    