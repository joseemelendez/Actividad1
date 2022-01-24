class Alumno:
    def __init__(self, carnet, nombre) -> None:
        self.carnet = carnet
        self.nombre = nombre
        self.siguiente = None
        pass

class ListaSimple2:
    def __init__(self) -> None:
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
        pass

    def insertarInicio(self, carnet, nombre):
        nuevo = Alumno(carnet, nombre)

        if (self.cabeza is None) and (self.cola is None): #la lista está vacía
            self.cabeza = nuevo
            self.cola = nuevo
        else: #la lista tiene elementos
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        self.tamanio += 1
        pass

    def insertarFinal(self, carnet, nombre):
        nuevo = Alumno(carnet, nombre)

        if (self.cabeza is None) and (self.cola is None): #la lista está vacía
            self.cabeza = nuevo
            self.cola = nuevo
        else: #la lista tiene elementos
            self.cola.siguiente = nuevo
            self.cola = nuevo
        
        self.tamanio += 1
        pass

    def eliminar(self, carnet):
            
        pass


    def visualizar(self):
        nodo = self.cabeza

        if nodo is None:#lista vacia
            print("Lista vacía")
        else: #lista tiene elementos
            while nodo is not None:
                if nodo.siguiente is None:#validando para que se pueda imprimir el valor del carnet del siguiente.
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre, "\tSiguiente:",nodo.siguiente)
                else:
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre, "\tSiguiente:",nodo.siguiente.carnet)
                nodo = nodo.siguiente
            print("\tTamaño:", self.tamanio,"\n")

        pass



lista = ListaSimple2()
lista.visualizar()
lista.insertarFinal(1, "Juan")
lista.insertarFinal(2, "Pamela")
lista.insertarFinal(3, "Tamara")
lista.visualizar()

