from Ejercicio4 import Torre

class Torres:
    __numDisco: int
    __torres: list[Torre]
    
    def __init__(self, disco):
        self.__torres = [Torre(),Torre(),Torre()]
        for i in range(disco, 0, -1):
            self.__torres[0].agregardisco(i)
        self.__numDisco = disco
        
    def 