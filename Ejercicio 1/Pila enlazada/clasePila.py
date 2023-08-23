
#CLASE NODO

class Nodo:
    __siguiente = None
    __dato = None

    def __init__(self,dato):
        self.__siguiente = None
        self.__dato = dato

    def setSiguiente(self,dato):
        self.__siguiente= dato

    def getSiguiente(self):
        return self.__siguiente

    def setDato(self,dato):
        self.__dato= dato
    
    def getDato(self):
        return self.__dato

#CLASE PILA

class pila:
    __cabeza = None
    __tamaño = 0 

    def __init__(self):
        self.__cabeza = None
        self.__tamaño = 0


    def ingresar(self,dato):
        nodo = Nodo(dato) # Genera una instancia de nodo y guarda el dato
        nodo.setSiguiente(self.__cabeza)  #El siguiente guarda la cabeza que esta vacia
        self.__cabeza = nodo #guarda la cabeza en el nodo
        self.__tamaño += 1 # Aumenta el tamaño en 1

    def getTamaño(self):
        return self.__tamaño
    
    def delete(self):
        if self.__cabeza == None: #Si la cabeza esta vacia
            raise exception("Cabeza vacia") 
        aux = self.__cabeza #Guarda la cabeza en una variable auxiliar
        self.__cabeza = self.__cabeza.getSiguiente() # En la cabeza guarda el siguiente dato
        return print('dato eliminado:'+ aux.getDato()) #devuelve el dato eliminado

if __name__ == '__main__':
    P = pila()
    P.ingresar('Hola1')
    P.ingresar('Hola2')
    P.delete()
