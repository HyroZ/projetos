meu_conjunto = set()
meu_conjunto.add(10)
meu_conjunto.add(20)
meu_conjunto.add(30)
meu_conjunto.add(10)

print(meu_conjunto)

#Verificando se um elemento está no conjunto
elemento = 20
if elemento in meu_conjunto:
  print(f"O elemento {elemento} está no conjunto")
else:
  print(f"O elemento {elemento} não está no conjunto")

#Numero de elementos repetidos e únicos em uma lista
numeros_rep = [1,2,2,2,3,3,3,4,4,4]
unicos = set(numeros_rep)
print(f"Elementos únicos: {unicos}")
print(f"Numero de elementos únicos: {len(unicos)}")
print(f"Numero de elementos repetidos: {len(numeros_rep) - len(unicos)}")