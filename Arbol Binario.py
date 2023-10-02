import os
from Nodo import Nodo

class Arbol:
    __raiz: Nodo|None
    __cantidad: int

    def __init__(self):
        self.__raiz = None
        self.__cantidad=0

    def vacio(self):
        return self.__cantidad == 0
    
    def insertarotro(self, subarbol,dato):
        if dato == subarbol.getDato():
            return print("DATO YA AGREGADO")
        else:
            #Si el dato es menor al dato en la raiz

            if dato < subarbol.getDato():
                if subarbol.getIzq() == None:
                    subarbol.setIzquierdo(dato)
                else:
                    self.insertarotro(subarbol.getIzq(),dato)
            elif dato > subarbol.getDato():
                if subarbol.getDer() == None:
                    subarbol.setDerecho(dato)
                else:
                    self.insertarotro(subarbol.getDer(),dato)
            self.__cantidad +=1
    
    def mostrarArbolBin(self, sangria=4):
        if self.__raiz == None:
            print("El arbol esta vacio")
            return

        def mostrarArbolBinRec(nodo, cadena):
            print(str(nodo.getDato()))
            #Para el hijo derecho
            if nodo.getDerecho() != None:
                if nodo.getIzquierdo() != None:
                    print(cadena+ "├" + "─" * sangria, end="") 
                else:
                    print(cadena+ "└" + "─" * sangria, end="")
                mostrarArbolBinRec(nodo.getDerecho(), cadena + "│" + " " *sangria)
            #Para el hijo izquierdo
            if nodo.getIzquierdo() != None:
                print(cadena+ "└" + "─" * sangria, end="")
                mostrarArbolBinRec(nodo.getIzquierdo(), cadena + " " *sangria)

        mostrarArbolBinRec(self.__raiz, "")

    def insertar(self,dato):
        if self.vacio():
            self.__raiz = Nodo(dato)
            self.__cantidad +=1
        else:
            self.insertarotro(self.__raiz,dato)

if __name__ == '__main__':
    A = Arbol()
    A.insertar(5)
    A.insertar(6)
    A.insertar(3)
    A.insertar(7)
    A.insertar(9)
    A.mostrarArbolBin()