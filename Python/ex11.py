#Criando e manipulando um array sem dependências externas
my_array = [1, 2, 3, 4, 5]
print("Array original")
print(my_array)

#Operações em massa
squared_array = [element ** 2 for element in my_array]   #elemento ao quadrado
sum_of_elements = sum(my_array) #soma dos elementos

print("\nArray ao quadrado")
print(squared_array)
print("\nSoma dos elementos")
print(sum_of_elements)

#Acessando um elemento por índice
print("\nElemento no índice 2", my_array[2])