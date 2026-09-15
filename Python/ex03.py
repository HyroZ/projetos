numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros: 
    print(f"Camiseta: {numero}")

numero = int(input("Digite um número, ou 0 para sair: "))
while numero != 0:
    if numero %2 == 0:
        print(f"O número {numero} é par")
    else:
        print(f"O número {numero} é ímpar")
