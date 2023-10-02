class Nodo:
    __dato: int
    __izquierdo: None
    __derecho: None

    def __init__(self,dato):
        self.__dato = dato
        self.__izquierdo = None
        self.__derecho = None

    def getDato(self):
        return self.__dato
    
    def getIzq(self):
        return self.__izquierdo
    
    def getDer(self):
        return self.__derecho
    
    def setDato(self,dato):
        self.__dato = dato

    def setIzquierdo(self,dato):
        self.__izquierdo = dato

    def setDerecho(self,dato):
        self.__derecho = dato
