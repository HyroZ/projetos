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