import numpy as np

class Pila:
    __arreglo: None
    __tope: 0 
    __tamaño: int
    
    def __init__(self, tamaño: int=10):
        self.__arreglo = np.empty(tamaño,dtype=int)
        self.__tope = 0 
        self.__tamaño = tamaño
        
    def insertar(self,dato):
        if self.__tope < self.__tamaño:
            self.__arreglo[self.__tope] = dato
            self.__tope += 1
            return print(dato,'guardado existosamente')
        else:
            return print('PILA LLENA')
        
    def getTam(self):
        return self.__tope
    
    def eliminarvalor(self):
        if self.__tope > 0:
            self.__tope -= 1
            return self.__arreglo[self.__tope]
        else:
            return print('PILA VACIA')

def conversionabinario(num):
    P= Pila()
    while num>0:
        resto = num % 2
        P.insertar(resto)
        num = num // 2
        binario =+ resto
    string = ''
    while P.getTam() != 0: 
        val = P.eliminarvalor()
        string += str(val)
    print(string)
    
if __name__ == '__main__':
    num = int(input('INGRESE UN NUMERO EN DECIMAL:'))
    conversionabinario(num)
        