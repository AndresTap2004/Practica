
from controller.exception.LinkedEmpty import LinkedEmpty
from controller.tda.linked.node import Node
from controller.exception.arrayPositionException import ArrayPositionException
from controller.exception.vacioException import VacioException
from controller.tda.linked.merge_sort import MergeSort
from controller.tda.linked.quick_sort import QuickSort
from controller.tda.linked.shell_sort import ShellSort
from controller.tda.linked.busqueda_binaria import Busqueda_Binaria
from controller.tda.linked.busqueda_lineal_binaria import Busqueda_Lineal_Binaria
from numbers import Number

class LinkedList(object):

    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value


    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length = self.__length +1
        else:
            headOdl = self.__head
            node = Node(data, headOdl)
            self.__head = node
            self.__length = self.__length +1

    
    def __addLast__(self, data):
        if self.isEmpty:
            self.__addFirst__(data)
        else:
            node = Node(data)
            self.__last._next = node 
            self.__last = node
            self.__length += 1

    def getNode(self, pos):
        if self.isEmpty:
            raise VacioException("Error, la lista esta vacia")
        elif pos < 0  or pos >= self.__length:
            raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
        elif pos == 0:
            return self.__head
        elif pos == (self.__length -1):
            return self.__last
        else:
            node = self.__head
            cont = 0
            while cont < pos:
                cont += 1
                node = node._next
            return node
        
    def add(self, data, pos = 0):
        if pos == 0:
            self.__addFirst__(data)
        elif pos == self.__length:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos-1)
            node_last =  node_preview.__next 
            node = Node(data, node_last)
            node_preview._next = node
            self.__length += 1

    def edit(self, data, pos = 0):
        if pos == 0:
            self.__head._data = data
        elif pos == self.__length:
            self.__last._data = data
        else:
            node = self.getNode(pos)
            node._data = data

    @property 
    def toArray(self):
        #Todo
        array = []
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self.__length:
                array.append(node._data)
                cont += 1
                node = node._next
        return array

    def toList(self, array):
        self.clear
        for i in range(0, len(array)):
            self.__addLast__(array[i])
            
    def deleteFirst(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            element = self.__head._data
            aux = self.__head._next
            self.__head = aux
            if self._length == 1:
                self.__last = None
            self._length -= 1
            return element
        
    def deleteLast(self):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        else:
            node = self.__head
            while node._next != self.__last:
                node = node._next
            element = self.__last._data
            node._next = None
            self.__last = node
            self._length -= 1
            return element


    def delete(self, pos):
        if self.isEmpty:
            raise VacioException("Lista Vacia")
        elif pos < 0 or pos >= self.__length:
            raise ArrayPositionException("Posición fuera de los límites de la lista")
        elif pos == 0:
            return self.deleteFirst()
        elif pos == self.__length - 1:
            return self.deleteLast()
        else:
            prev_node = self.getNode(pos - 1)
            node_to_delete = prev_node._next
            prev_node._next = node_to_delete._next
            element = node_to_delete._data
            del node_to_delete
            self._length -= 1
            return element
        
    def list_all(self):
        if self.isEmpty:
            print("La lista está vacía.")
        else:
            current_node = self.__head
            while current_node is not None:
                print(current_node._data)
                current_node = current_node._next

    def arreglo_de_diccionarios(self):
        if self.isEmpty:
            return []
        else:
            array = []
            node = self.__head
            while node is not None:
                array.append(node._data.persona_to_dict())
                node = node._next
            return array
        
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0

    def get(self, pos):
        try:
            if self.isEmpty:
                raise VacioException("Error, la lista esta vacia")
            elif pos < 0  or pos >= self.__length:
                raise ArrayPositionException("Error, Esta fuera de los limites de la lista ")
            elif pos == 0:
                return self.__head._data
            elif pos == (self.__length -1):
                return self.__last._data
            else:
                node = self.__head
                cont = 0
                while cont < pos:
                    cont += 1
                    node = node._next
                return node._data
        except Exception as e:
            print(e)


    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = 'List is Empty'
        else:
            node = self.__head
            while node != None:
                out += str(node._data) + " "
                node = node._next
        return out
    
    @property
    def print(self):
        node = self.__head
        data = ""
        while node is not None:
            data += str(node._data) + "    "
            node = node._next
        print(f'Lista de datos\n{data}')
    
    # Metodos de ordenamiento
    
    def metodos_merge_sort(self, arr, attribute=None, orden=1):
        arreglo = arr.toArray  
        ordenamiento = MergeSort()
        if attribute:
            arreglo = ordenamiento.sort_merge_atribute(arreglo, attribute, orden)
        else:
            arreglo = ordenamiento.sort_merge_number(arreglo, orden)
        self.toList(arreglo)
        return self
    
    def metodos_quick_sort(self, arr, attribute=None, orden=1):
        arreglo = arr.toArray  
        ordenamiento = QuickSort()
        if attribute:
            arreglo = ordenamiento.sort_quick_atribute(arreglo, attribute, orden)
        else:
            arreglo = ordenamiento.sort_quick_number(arreglo, orden)
        self.toList(arreglo)
        return self
    
    def metodos_shell_sort(self, arr, attribute=None, orden=1):
        arreglo = arr.toArray  
        ordenamiento = ShellSort()
        if attribute:
            arreglo = ordenamiento.sort_shell_atribute(arreglo, attribute, orden)
        else:
            arreglo = ordenamiento.sort_shell_number(arreglo, orden)
        self.toList(arreglo)
        return self
    
    # Metodos de busqueda

    def search_secuential(self, lista, data):
        result_list = LinkedList()  
        array = lista.toArray
        for item in array:
            if item == data:
                result_list.add(item)  
        return result_list

    def busqueda_binaria_linked(self, lista, attribute=None, value=None):
        busqueda = Busqueda_Binaria()
        array = lista.toArray
        if attribute:
            valor_encontrado = busqueda.busqueda_binaria_atribute(array, attribute, value)
        else:
            valor_encontrado = busqueda.busqueda_binaria_number(array, value)
        
        if valor_encontrado is not None:
            self.toList(valor_encontrado)
        
        return self

    def busqueda_lineal_binaria_linked(self, lista, attribute=None, value=None):
        arreglo = Busqueda_Lineal_Binaria()
        array = lista.toArray  
        if attribute:
            array = arreglo.busqueda_binaria_lineal_atribute(array, attribute, value)  
        else:
            array = arreglo.busqueda_binaria_lineal_number(array, value)  
        self.toList(array) 
        return self


    
