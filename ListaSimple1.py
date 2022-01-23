
from xml.etree.ElementTree import tostring


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
                print("No se puede buscar, lista vacia.\n")
            else:
                nodo = self.cabeza
                seguir = True
                while seguir:
                    if nodo.carnet == carnet:
                        print("Se ha encontrado el carnet:", nodo.carnet, ", pertenece a:" , nodo.nombre, "\n")
                        seguir = False
                    else:

                        if nodo.siguiente is None:
                            seguir = False
                            print("No se ha encontrado el estudiante con carnet",carnet,".\n")
                        else :
                            nodo = nodo.siguiente

        def eliminar (self, carnet):
            nodo = self.cabeza

            if nodo is None: #la lista está vacia
                print("[!!] No se puede eliminar, lista vacía.\n")
            elif nodo.siguiente is None: #tiene solo un elemento
                if nodo.carnet == carnet:
                    print("[OK] Se eliminará el alumno Carnet:", nodo.carnet," Nombre:", nodo.nombre,"\n")
                    self.tamanio -= 1
                    self.cabeza = None
                else:
                    print("[!] No se ha encontrado el alumno con carnet", carnet, ".\n")
            else: #tiene mas de un elemento
                if nodo.carnet == carnet:#es el primer elemento
                    print("[OK] Se eliminará el alumno Carnet:", nodo.carnet," Nombre:", nodo.nombre,"\n")
                    self.tamanio -= 1
                    self.cabeza = nodo.siguiente
                else:#no es el primero
                    anterior = nodo
                    nodo = anterior.siguiente
                    while nodo is not None:
                        if nodo.carnet == carnet:
                            print("[OK] Se eliminará el alumno Carnet:", nodo.carnet," Nombre:", nodo.nombre,"\n")
                            anterior.siguiente = nodo.siguiente
                            self.tamanio -=1
                            break
                        else:
                            anterior = nodo
                            nodo = anterior.siguiente

                    if nodo is None:
                        print("[!] No se encontró el carnet a eliminar.\n")
            pass
            
        def visualizar(self):
            actual = self.cabeza
            print("Elementos en lista:")
            if actual is None:
                print("\tLista vacia.")

            while actual is not None:
                if actual.siguiente is None:
                    print("Carnet: ", actual.carnet , " Nombre: " , actual.nombre , "\tSiguiente: ", actual.siguiente)
                else:
                    print("Carnet: ", actual.carnet , " Nombre: " , actual.nombre , "\tSiguiente: ", actual.siguiente.carnet)
                actual = actual.siguiente
            print("\tTamaño: ", self.tamanio,"\n")
            
        
lista = Lista()
#PRUEBAS

lista.insertarFinal(1,"Jose")
lista.insertarFinal(2,"Carlos")
#lista.insertarFinal(3,"Maria")
# lista.insertarFinal(4,"Susana")
# lista.insertarFinal(5,"Pablo")
# lista.insertarFinal(6,"Lucia")
lista.insertarInicio(0, "Terminator")
lista.insertarInicio(100, "Twain")

lista.visualizar()
lista.eliminar(100)
lista.visualizar()