
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

        def eliminar (self, carnet):
            
            nodo = self.cabeza

            if nodo is None: #la lista está vacia
                print("No se puede eliminar, lista vacía.")
            elif nodo.siguiente is None: #tiene solo un elemento
                if nodo.carnet == carnet:
                    print("Se ha encontrado el carnet: ", nodo.carnet)
                    self.tamanio -= 1
                    self.cabeza = None
                else:
                    print("No se ha encontrado el elemento.")
            else: #tiene mas de un elemento
                if nodo.carnet == carnet:#es el primer elemento
                    print("Se ha encontrado el carnet: ", nodo.carnet)
                    self.tamanio -= 1
                    self.cabeza = nodo.siguiente
                else:#no es el primero
                    print("El elemento a borrar no es el primero")
                    anterior = nodo
                    nodo = anterior.siguiente
                    while nodo is not None:
                        if nodo.carnet == carnet:
                            anterior.siguiente = nodo.siguiente
                            self.tamanio -=1
                            break
                        else:
                            anterior = nodo
                            nodo = anterior.siguiente
                    
                    if nodo is None:
                        print("No se encontró el carnet a eliminar.")
                            


                   
                        





                #if nodo is None: #tiene solo un elemento
                
                #else:




            # if self.cabeza is None: #si está vacia
            #     print("No se puede eliminar, lista vacia.")
            # else:
            #     nodo = self.cabeza
            #     seguir = True
            #     if nodo.carnet == carnet: #si tiene solo un elemento
            #         self.cabeza = None
            #         self.tamanio -= 1
            #         print("Se eliminado el alumno: ", nodo.carnet)
            #     else: #si tiene mas elementos
            #         while seguir:
                        
            #             if nodo.carnet == carnet:
            #                 anterior = nodo
            #                 anterior.siguiente = nodo.siguiente
            #                 self.tamanio -=1
            #                 seguir = False
            #                 print("Se eliminado el alumno: ", carnet)
                            
            #             else:
            #                 nodo = nodo.siguiente

            pass
            
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

#lista.insertarInicio(1, "Jose")
#lista.insertarInicio(2, "Carlos")
#lista.insertarInicio(3, "Lucia")
lista.insertarInicio(4, "Juana")

lista.insertarFinal(5, "Carmen")
lista.insertarFinal(6, "Juan")

lista.insertarInicio(7, "Pablo")
lista.insertarFinal(8, "Carolina")

lista.visualizar()
lista.eliminar(10)
lista.visualizar()


#lista.buscar(8)

#lista.visualizar()
#lista.visualizar()
