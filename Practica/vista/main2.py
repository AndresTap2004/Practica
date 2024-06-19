import sys
import random
sys.path.append('../')
from controller.tda.linked.linkedList import LinkedList
import time

lista = LinkedList()
lista2 = LinkedList()

for i in range(25000): # 10000 , 20000
    numero = (random.randint(0, 25000))
    lista.add(numero)
    lista2.add(numero)

valor_a_buscar = random.randint(0, 25000)

# Busqueda merge sort
lista.metodos_merge_sort(lista, orden=1)
lista2.metodos_merge_sort(lista, orden=1)

# Búsqueda lineal binaria
inicio_lineal_binaria = time.time()
resultado_busqueda_lineal_binaria = lista.busqueda_lineal_binaria_linked(lista, value=valor_a_buscar)
fin_lineal_binaria = time.time()
tiempo_lineal_binaria = fin_lineal_binaria - inicio_lineal_binaria

# Búsqueda secuencial
inicio_secuencial = time.time()
resultado_busqueda_secuencial = lista2.search_secuential(lista2, valor_a_buscar)
fin_secuencial = time.time()
tiempo_secuencial = fin_secuencial - inicio_secuencial

print(f"Valor a buscar: {valor_a_buscar}")
print(f"Tiempo de búsqueda lineal binaria: {tiempo_lineal_binaria} segundos")
print(f"Tiempo de búsqueda secuencial: {tiempo_secuencial} segundos")
