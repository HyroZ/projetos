#Guardando informações

idade = 20
maior_idade = idade >= 18
print(maior_idade)

idade = int(input("Digite sua idade: "))
if idade < 18:
  print("Menor de idade!")
elif idade >= 18 and idade < 60:
  print("Adulto")
else:
  print("Idoso")