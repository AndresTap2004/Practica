import sys
import random
sys.path.append('../')
from controller.tda.linked.linkedList import LinkedList
import time

lista = LinkedList()
lista2 = LinkedList()
lista3 = LinkedList()

for i in range(10000): # 10000 , 20000 , 25000
    numero = random.randint(0, 10000)
    lista.add(numero)
    lista2.add(numero)
    lista3.add(numero)
    
# Merge Sort 
inicio = time.time()
lista.metodos_merge_sort(lista, orden=1) 
fin = time.time()

# Quick Sort 
inicio2 = time.time()
lista2.metodos_quick_sort(lista2, orden=1)   
fin2 = time.time()

# Shell Sort 
inicio3 = time.time()
lista3.metodos_shell_sort(lista3, orden=1)  
fin3 = time.time()

print("Tiempo Merge Sort: ", fin - inicio)
print("Tiempo Quick Sort: ", fin2 - inicio2)
print("Tiempo Shell Sort: ", fin3 - inicio3)