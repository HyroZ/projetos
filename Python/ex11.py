#NumPy - Importando e criando uma Array
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
print("Array original")
print(my_array)

#NumPy - Operações em massa
squared_array = my_array ** 2   #elemento ao quadrado
sum_of_elements = np.sum(my_array) #soma dos elementos

print("\nArray ao quadrado")
print(squared_array)
print("\nSoma dos elementos")
print(sum_of_elements)

#Acessando um elemento por índice
print("\nElemento no índice 2", my_array[2])