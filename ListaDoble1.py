class Alumno:
    def __init__(self, carnet, nombre) -> None:
        self.carnet = carnet
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None
        pass

class ListaDoble1:
    def __init__(self) -> None:
        self.cabeza = None
        self.tamanio = 0
        pass

    def insertarInicio(self, carnet, nombre):
        nuevo = Alumno(carnet, nombre)

        if self.tamanio == 0:#lista vacía
            self.cabeza = nuevo
        else:
            self.cabeza.anterior = nuevo
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        self.tamanio += 1
        pass

    def insertarFinal(self, carnet, nombre):
        nuevo = Alumno(carnet, nombre)

        if self.tamanio == 0:#lista vacia
            self.cabeza = nuevo
        else:
            nodo = self.cabeza

            while nodo.siguiente is not None:
                nodo = nodo.siguiente

            nuevo.anterior = nodo
            nodo.siguiente = nuevo
        self.tamanio += 1
        pass

    def buscar(self, carnet):
        nodo = self.cabeza

        if nodo is None:#lista vacia, no se puede buscar.
            print("[!] Lista vacía, no se puede buscar.\n")
        else:
            while nodo is not None:
                if nodo.carnet == carnet:#se ha encontrado el carnet
                    print("Se ha encontrado el alumno con carnet:", str(nodo.carnet) + ", pertenece a:",nodo.nombre,"\n")
                    break
                else:
                    nodo = nodo.siguiente

            if nodo is None:
                print("[!] No se ha encontrado el carnet", carnet,"\n")
        pass

    def eliminar(self, carnet):
        print("[!] Se desea eliminar el carnet ",carnet)
        nodo = self.cabeza

        if self.tamanio == 0:
            print("[!] No se puede eliminar, lista vacía!\n")
        elif self.tamanio == 1:#solo un elemento
            if nodo.carnet == carnet:#el elemento encontrado es la cabeza
                self.cabeza = None
                self.tamanio -=1
                print("Se ha eliminado el alumno: ", nodo.nombre, "con carnet:",nodo.carnet,"\n")
                nodo = None
            else:
                print("No se ha encontrado el carnet",carnet,"\n")
        else:#tiene mas de un elemento
            print("La lista tiene mas de un elemento para borrar.\n")
            if nodo.carnet == carnet:#el elemento a eliminar es la cabeza
                self.cabeza = nodo.siguiente
                self.cabeza.anterior = nodo.anterior
                self.tamanio -= 1
                nodo = None
                print("Se ha eliminado la cabeza de la lista.\n")
            else:#se debe seguir buscando e iterar
                print("El elemento a eliminar no es la cabeza.\n")
                anterior = nodo
                nodo = nodo.siguiente
                siguiente = nodo.siguiente
                encontrado = False

                while encontrado == False:
                    if nodo.carnet == carnet:#se enocntró en la siguiente iteracion
                        encontrado = True

                        if siguiente is None: #el elemento es el ultimo 
                            anterior.siguiente = siguiente #siguiente es None
                            self.tamanio -= 1
                        else: #el elemento no es el ultimo
                            anterior.siguiente = siguiente
                            siguiente.anterior = anterior
                            self.tamanio -= 1

                        print("Se ha eliminado el carnet:", nodo.carnet, "que pertence al alumno:", nodo.nombre,"\n")
                    else:#iterar
                        anterior = nodo
                        nodo = nodo.siguiente
                        if nodo is None:
                            break
                        else:
                            siguiente = nodo.siguiente
                
                if encontrado == False:
                    print("[!] No se ha encontrado el carnet", carnet, "para eliminar.\n")

        pass


    def visualizar(self):
        nodo = self.cabeza

        if nodo is None: #lista vacia, no se puede mostrar
            print("[!] Lista vacía, no se puede visualizar.\n")
        else:
            print("Elementos en lista:")
            while nodo is not None:
                if nodo.siguiente is None:
                    if nodo.anterior is None:
                        print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre,"\t| Anterior:",nodo.anterior,"  \tSiguiente:",nodo.siguiente)
                    else:
                        print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre,"\t| Anterior:",nodo.anterior.carnet,"  \tSiguiente:",nodo.siguiente)
                elif nodo.anterior is None:
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre,"\t| Anterior:",nodo.anterior,"  \tSiguiente:",nodo.siguiente.carnet)
                else:
                    print("Carnet:", nodo.carnet, "\tNombre:", nodo.nombre,"\t| Anterior:",nodo.anterior.carnet,"  \tSiguiente:",nodo.siguiente.carnet)
                nodo = nodo.siguiente
            print("[-] Fin de la lista. Tamaño:",self.tamanio,"\n")
        pass

    

lista = ListaDoble1()

lista.visualizar()

lista.insertarInicio(0, "Carmen")
lista.insertarInicio(1, "Lucia")
lista.insertarFinal(10, "Carlos")
lista.insertarInicio(2, "Pablo")
lista.insertarInicio(3, "Juan")
lista.insertarFinal(13, "Carlos")
lista.insertarFinal(11, "Maria")

lista.visualizar()

lista.eliminar(101)

lista.visualizar()

# lista.buscar(100)


