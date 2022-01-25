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

    def buscar(self, carnet):
        nodo = self.cabeza
        encontrado = False
        while (nodo is not None) and encontrado == False:
            if nodo.carnet == carnet:
                print("Se ha encontrado el alumno con carnet: " + str(nodo.carnet) +", pertenece a:", nodo.nombre + ".\n")
                encontrado = True
            else:
                nodo = nodo.siguiente
        if encontrado == False:
            print("No se encontró el carnet:", carnet,"\n")
        pass

    def eliminar(self, carnet):
        anterior = None
        nodo = self.cabeza

        if nodo is None:#lista vacia
            print("Lista vacía, no se puede eliminar.\n")
        else: #tiene elementos
            if nodo.carnet == carnet: #elemento encontrado
                if self.cabeza == nodo:#es el primer elemento
                    self.cabeza = nodo.siguiente
                    self.tamanio -= 1
            else:# es otro elemento                    
                anterior = nodo
                nodo = nodo.siguiente
                while nodo is not None:
                    if nodo.carnet == carnet: #elemento encontrado
                        print("Se eliminará el estudiante con carnet " + str(nodo.carnet) + ". Nombre:", nodo.nombre,"\n")
                        anterior.siguiente = nodo.siguiente
                        self.tamanio -= 1

                        if nodo == self.cola: #es el ultimo elemento
                            self.cola = anterior
                        
                        nodo = None #funciona como el break
                    else:
                        anterior = nodo
                        nodo = nodo.siguiente

        pass


    def visualizar(self):
        nodo = self.cabeza

        if nodo is None:#lista vacia
            print("No se puede visualizar, lista vacía.\n")
        else: #lista tiene elementos
            while nodo is not None:
                if nodo.siguiente is None:#validando para que se pueda imprimir el valor del carnet del siguiente.
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre, "\tSiguiente:",nodo.siguiente)
                else:
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre, "\tSiguiente:",nodo.siguiente.carnet)
                nodo = nodo.siguiente
            print("\tTamaño:", self.tamanio,"\n")

        pass


print(__name__)
lista = ListaSimple2()
lista.visualizar()
lista.insertarFinal(1, "Juan")
lista.insertarFinal(2, "Pamela")
lista.insertarFinal(3, "Tamara")
lista.insertarInicio(100, "Pancho")
lista.visualizar()

lista.eliminar(1)

lista.visualizar()

lista.buscar(2)