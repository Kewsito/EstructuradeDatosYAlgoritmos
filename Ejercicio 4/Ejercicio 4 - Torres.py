from Ejercicio4 import Torre

class Torres:
    __numDisco: int
    __torres: list[Torre]
    
    def __init__(self, disco):
        self.__torres = [Torre(),Torre(),Torre()]
        for i in range(disco, 0, -1):
            self.__torres[0].agregardisco(i)
        self.__numDisco = disco
        
    def moverdisco(self, desde, hacia):
        try:
            #Guarda el disco en la torre destino y saca el disco de la torre elegida
            value= self.__torres[desde].eliminardisco()
        except:
            return
        
        try:
            self.__torres[hacia].agregardisco(value)
        except:
            print('SALIO POR EL SEGUNDO TRY, OPC EXCEPT')
            
            #Guarda en la torre saliente el valor sacado
            self.__torres[desde].agregardisco(value)
    
    def final(self):
        return self.__torres[2].tamaño() == self.__numDisco
    
    def __repr__(self):
        string: str = '\n'

        for i in range(self.__numDiscos, 0, -1):
            string += '    {}|{}         {}|{}         {}|{}    \n'.format(
                self.__torres[0].TamañoDisco(i),
                self.__torres[0].TamañoDisco(i),
                self.__torres[1].TamañoDisco(i),
                self.__torres[1].TamañoDisco(i),
                self.__torres[2].TamañoDisco(i),
                self.__torres[2].TamañoDisco(i),
            )

        string += '=================================='

        return string

if __name__ == '__main__':
    cdisco = int(input('Ingrese cantidad de discos: \n'))
    juego = Torres(cdisco)
    
    while not juego.final():
        desde = int(input('Mover disco de torre: \n'))
        hacia = int(input('Hacia torre: \n'))
        
        if 1<=desde<=3 and 1<=hacia:
            juego.moverdisco(desde-1, hacia-1)
        else:
            print('Ingrese un valor valido')
            print(juego)