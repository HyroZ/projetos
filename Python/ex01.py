print("Hello, World!")
#2 Criando variáveis de tipos diferentes
x = 10
nome = 'Anderson'
nota = 8.75
fez_inscricao = True

print(x)
print(nome)
print(nota)
print(fez_inscricao)

nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")

Nota_1 = int(input("Digite a primeira nota: "))
Nota_2 = int(input("Digite a segunda nota: "))
Nota_3 = int(input("Digite a terceira nota: "))
Nota_4 = int(input("Digite a quarta nota: "))
media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4
print(f"A média das notas é: {media}")

if media >= 6:
    print("Parabéns! Você foi aprovado(a)!")
else:
    print("Infelizmente, você foi Reprovado(a).")