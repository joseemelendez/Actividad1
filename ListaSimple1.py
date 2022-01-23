
class Alumno:
    def __init__(self, carnet, nombre) -> None:
        self.carnet = carnet
        self.nombre = nombre
        self.siguiente = None
        pass

class Lista:
        def __init__(self) -> None:
            self.cabeza = None
            self.tamanio = 0
            pass

        def insertarInicio(self, carnet, nombre):
            nuevo = Alumno(carnet, nombre)

            if self.tamanio == 0:
                self.cabeza = nuevo
            else:
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo

            self.tamanio += 1

        def insertarFinal(self, carnet, nombre):
            nuevo = Alumno(carnet, nombre)

            if self.cabeza is None:
                self.cabeza = nuevo
            else:
                actual = self.cabeza
                while actual.siguiente is not None:
                    actual = actual.siguiente

                actual.siguiente = nuevo
            self.tamanio += 1

        def buscar(self, carnet):
            
            if self.tamanio == 0:
                print("No se puede buscar, lista vacia.")
            else:
                nodo = self.cabeza
                seguir = True
                while seguir:
                    if nodo.carnet == carnet:
                        print("Se ha encontrado el carnet: ", nodo.carnet, "pertenece a: " , nodo.nombre, "\n")
                        seguir = False
                    else:

                        if nodo.siguiente is None:
                            seguir = False
                            print("No se ha encontrado el estudiante.", "\n")
                        else :
                            nodo = nodo.siguiente
            
        def visualizar(self):
            actual = self.cabeza
            print("El tamaño de la lista es: ", self.tamanio)
            while actual is not None:
                if actual.siguiente is None:
                    print("Carnet: ", actual.carnet , " Nombre: " , actual.nombre , "\tSiguiente: ", actual.siguiente)
                else:
                    print("Carnet: ", actual.carnet , " Nombre: " , actual.nombre , "\tSiguiente: ", actual.siguiente.carnet)
                actual = actual.siguiente
            print()
        
lista = Lista()

lista.insertarInicio(1, "Jose")
lista.insertarInicio(2, "Carlos")
lista.insertarInicio(3, "Lucia")
lista.insertarInicio(4, "Juana")

lista.insertarFinal(5, "Carmen")
lista.insertarFinal(6, "Juan")

lista.insertarInicio(7, "Pablo")
lista.insertarFinal(8, "Carolina")

lista.visualizar()


lista.buscar(8)
