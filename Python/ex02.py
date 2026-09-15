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

idade = int(input("Digite sua idade: "))

Ingressos1 = 10
Ingressos2 = 0
Ingressos3 = 15
Ingressos4 = 3

if idade < 12:
  print(f"Recomendamos o filme infantil 1. Que atualmente está com {Ingressos1} Disponíveis")
elif idade >= 12 and idade < 18:
  print(f"Recomendamos o filme infantil 2. Que atualmente está com {Ingressos2} Disponíveis")
elif idade >= 18 and idade < 25:
  print(f"Recomendamos o filme adulto. Que atualmente está com {Ingressos3} Disponíveis")
else:
  print(f"Recomendamos o filme adulto 2. Que atualmente está com {Ingressos4} Disponíveis")




