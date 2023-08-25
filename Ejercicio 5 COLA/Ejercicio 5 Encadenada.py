class ColaEnlazada:
    __dato: None
    __siguiente: None
        
    def __init__(self,dato):
        self.__dato = dato
        self.__siguiente = None
        
    def setSiguiente(self,dato):
        self.__siguiente = dato

    def setDato(self,dato):
        self.__dato = dato
            
    def getSiguiente(self):
        return self.__siguiente
        
    def getDato(self):
        return self.__dato
        
class Cola:
    __primero = None
    __ultimo = None
    __tamaño = int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__tamaño = 0
    def estavacio(self):
        return self.__tamaño == 0
        
    def ingresarDato(self,dato):
        cola = ColaEnlazada(dato) #Genera una instancia de la cola enlazada e ingresa el dato
        if self.estavacio():
            self.__primero = cola
        else: 
            self.__ultimo.setSiguiente(cola)
        self.__ultimo = cola
        self.__tamaño =+1 
        
    def getTam(self):
        return self.__tamaño
        
    def eliminarDato(self):
        if self.estavacio():
            print('Cola vacia')
        else:
            el = self.__primero.getDato()
            self.__primero = self.__primero.getSiguiente()
            self.__tamaño -=1
            return el
            
    def recorrer(self):
        aux = self.__primero
        while aux != None:
            print('dato:', aux.getDato())
            aux = aux.getSiguiente()
                
if __name__ == '__main__':
    cola = Cola()
    print('Insertando elementos')
    cola.ingresarDato(1)
    cola.ingresarDato(2)
    cola.ingresarDato(3)
    print('Mostrando elementos')
    cola.recorrer()
    print('Eliminando elementos')
    print(cola.eliminarDato())
    cola.recorrer()