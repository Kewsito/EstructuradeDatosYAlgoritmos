'''Implementar el TDA  Cola, con sus operaciones Abstractas en Representación secuencial y encadenada.'''
import numpy as np

class Cola:
        __tamaño: int
        __arreglo: None
        __tope: int
        __base:int

        def __init__(self, tamaño: int=10):
            self.__tamaño = tamaño
            self.__arreglo = np.empty(tamaño,dtype=int)
            self.__tope = -1
            self.__base = 0
        
        def agregar(self,dato):
            if self.__tope < self.__tamaño:
                self.__tope += 1
                self.__arreglo[self.__tope] = dato
                return print(dato, ': Dato agregado a la cola')
            else:
                raise Exception('Cola llena')
            
        def eliminar(self):
            if self.__tope==self.__base:
                print('Cola vacia 1')
            elif self.__base < self.__tope:
                self.__base += 1
                return self.__arreglo[self.__base -1]
        
        def tamaño(self):
            return self.__tope
    
if __name__ == '__main__':
        cola = Cola(5)
        cola.agregar(1)
        cola.agregar(2)
        cola.agregar(3)
        cola.agregar(4)
        cola.agregar(5)
        print(cola.eliminar(),': Se elimino de la cola')
        print(cola.eliminar(),': Se elimino de la cola')
        print(cola.eliminar(),': Se elimino de la cola')
        print(cola.eliminar(),': Se elimino de la cola')
        print(cola.eliminar(),': Se elimino de la cola')
        