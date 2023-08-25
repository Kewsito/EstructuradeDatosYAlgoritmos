'''Una entidad bancaria que realiza el cobro de servicios, habilita una caja que atiende a una cola de clientes. Cada cliente avanza para realizar su pago cuando la caja está desocupada.

Considerar que el tiempo de atención del cajero es de 5 minutos y la frecuencia de llegada de los clientes es de 2 minutos. Realizar un programa que simule esta realidad.
Obtener el tiempo máximo de espera de los clientes en la cola.
Nota: Ingresar el tiempo de atención de cajero y la frecuencia de llegada de los clientes a la cola.'''


#Tiempo de atencion cajero = 5 min
#Frecuencia de clientes = 2 min
import datetime as dt
class Nodo:
    __dato: None
    __siguiente: None
    
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
        
    def getDato(self):
        return self.__dato
    
    def getSiguiente(self):
        return self.__siguiente
    
    def setDato(self, dato):
        self.__dato = dato
        
    def setSiguiente(self,dato):
        self.__siguiente = dato
        
class ColaEncadenada:
    __primero = None
    __ultimo = None
    __cantidad = 0
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cantidad = 0

    def getCant(self):
        return self.__cantidad
    def estaVacio(self):
        return self.__cantidad == 0

    def Insertar(self,cliente):
        nuevo = Nodo(cliente)
        if self.estaVacio():
            self.__primero = nuevo
        else:
            self.__ultimo.setSiguiente(nuevo)
        self.__ultimo = nuevo
        self.__cantidad += 1

    def eliminar(self):
        if self.estaVacio():
            print("La cola esta vacia")
        else:
            el = self.__primero.getDato()
            self.__primero = self.__primero.getSiguiente()
            self.__cantidad-=1
            return el

class cajero:
    __caja = bool
    __cliente = int
    
    def __init__(self):
        self.__caja = False
        self.__cliente = None
    def setAtencion(self,cliente):
        self.__caja = True
        self.__cliente = cliente
        
    def clienteAtendido(self):
        self.__caja = False
        self.__cliente = None
    
    def CajaAbierta(self):
        return self.__caja
    

if __name__ == '__main__':
    cola = ColaEncadenada()
    caja = cajero()
    TIEMPOSIMULADO = int(input('INGRESE EL TIEMPO DE SIMULACION \n'))
    ta_cajero = int(input('INGRESE EL TIEMPO DE ATENCION DEL CAJERO \n'))
    Frec_cliente = int(input('INGRESE LA FRECUENCIA DE LOS CLIENTES \n'))
    reloj = 0
    CLIENTEAT = 0
    tiempoespera= 0
    
    while(reloj <= TIEMPOSIMULADO):
        tiempoespera=+ cola.getCant()
        if (reloj % Frec_cliente)== 0:
            print('ENTRA PRIMER IF')
            CLIENTEAT =+1
            cola.Insertar(CLIENTEAT)
        if (reloj % ta_cajero) == 0 and not cola.estaVacio():
            print('ENTRA SEGUNDO IF')
            idcliente =cola.eliminar()
            caja.setAtencion(id)
            print('Se atendio cliente numero: {}'.format(idcliente))
            reloj =+1
        print('reloj:',reloj)
        reloj =+1
    prom = tiempoespera / CLIENTEAT
    print('El tiempo promedio de espera fue: {.2f}'.format(prom))