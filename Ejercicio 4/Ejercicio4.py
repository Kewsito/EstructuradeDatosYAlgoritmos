'''Realizar un programa que simule el juego de las torres de Hanoi. 
El juego de las tres torres de Hanoi   consiste en  una configuración de tres pilas numeradas como 1, 2 y 3, con ‘n’ discos de tamaño creciente. Los discos se representarán mediante  enteros. Los discos más grandes utilizarán valores mayores y los discos más pequeños valores menores.
El objetivo del juego es trasladar los discos de la pila 1, a la pila 3, usando la pila 2 como auxiliar. Para realizar este traslado se deben cumplir siempre los siguientes requisitos:

a) Sólo se puede mover una pieza cada vez; y para tomar una segunda pieza se debe dejar  primero la anterior en alguna torre.
b) Sólo puede apilar una pieza encima de una más grande.

Se deberá ingresar el número de discos con el que se va a jugar y mostrar por pantalla el estado inicial del juego (todas las piezas colocadas en la pila 1 y las pilas 2 y 3 vacías).
A partir de ahí, pedirá sucesivamente pares de números indicando la pila origen desde la que tomará la pieza y la pila destino a la que se  quiere realizar el movimiento. El programa analizará si la jugada es factible. Si el resultado del análisis es positivo moverá la ficha de una pila a otra. Si no lo es, indicará que es una jugada imposible, indicando el por qué y pedirá un nuevo movimiento.
El juego terminará cuando las pilas 1 y 2 estén vacías y todos los discos se encuentren en la pila 3,  mostrando el número de jugadas realizadas y el número mínimo de jugadas (2n–1) en el que se podría haber realizado.'''

import numpy as np

class Torre:
    __tamaño: int
    __arreglo: None
    __tope: int
    
    def __init__(self, tamaño: int):
        self.__tamaño = tamaño
        self.__arreglo = np.empty(tamaño, dtype=int)
        self.__tope = 0
        
    def agregardisco(self,disco):
        if self.__tope < self.__tamaño:
            if self.__arreglo[self.__tope] < disco or self.__arreglo[self.__tope] is None:
                self.__arreglo[self.__tope] = disco
                self.__tope=+1
                return print(disco,"agregado a la torre, en la posicion:",self.__tope-1)
        else:
            raise Exception('Torre Llena')
    
    def eliminardisco(self):
        if self.__tope== 0:
            raise Exception("No hay discos")
        else:
            self.__tope-=1
            return self.__arreglo[self.__tope]
    
    def mostrartorre(self,i):
        if self.__tope < i:
            return ' '
        return str(self.__arreglo[i-1])
    