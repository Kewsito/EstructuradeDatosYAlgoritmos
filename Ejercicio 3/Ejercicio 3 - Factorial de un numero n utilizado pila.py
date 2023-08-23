#Escriba un programa iterativo, que usando una pila, calcule el factorial de un número n. 

import numpy as np

class PilaSecuencial:
    __tope : int
    __tamaño: int
    __arreglo: None
    
    def __init__(self,tamaño):
        self.__arreglo = np.empty(tamaño, dtype=int)
        self.__tope=0
        self.__tamaño = tamaño
    
    def insertar(self,dato):
        if self.__tope < self.__tamaño:
            self.__arreglo[self.__tope] = dato
            print('tope =', self.__tope)
            self.__tope+=1
            return print(dato,'guardado existosamente.')
    
    def eliminar(self):
        if self.__tope == 0:
            raise Exception("Pila vacia")  
        else:
            self.__tope-=1
            return self.__arreglo[self.__tope]
    
    def getVal(self):
        return self.__arreglo[self.__tope - 1]
        
    def getTope(self):
        return self.__tope

def calcular(num):
    P = PilaSecuencial(num)
    while num>0:
        P.insertar(num)
        num -=1
    entero = P.getVal()
    while P.getTope() != 0:
            entero *= P.eliminar()
    print('entero factorial =',entero)    
    
if __name__ == '__main__':
    numero = int(input('Ingrese un numero para factoriar'))
    if numero>0:
        calcular(numero)
    elif numero == 0:
        print('Entero factorial = 1')
    else:
        print('Numero no factorial')