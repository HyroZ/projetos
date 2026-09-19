# Exercício 08 - Python - Testando tuplas e listas com funções built-in

texto = "explorando a diversidade de linguagens de programação com Python"
print(f"Tamanho do texto: {len(texto)}")
print(f"Quantidade de 'e' no texto: {texto.count('e')}")
print(f"As 5 primeiras letras do texto: {texto[0:5]}")

cores = ['v', 'a', 'l', 'o', 'h']

for cor in cores:
    print(f"Posição = {cores.index(cor)} | Cor = {cor}")

linguagens = ["Python", "JavaScript", "C++", "Java", "C#"]
print("Antes da listcomp =", linguagens)


vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipos de vogais = {type(vogais)}")
for p, z in enumerate(vogais):
  print(f"Posição = {p}, valor = {z}")

#Testando tuplas e listas

cores = ("azul", "verde")

outra = cores
cores = ("vermelho", "amarelo")

print(outra)
print(cores)

#Lista de convidados

convidados = ("alice", "rodrigo", "carol", "felipe")
confirmados = ["alice", "rodrigo"]

print("Convidados que ainda não confirmaram:")
for convidado in convidados:
  if convidado not in confirmados:
    print(f"- {convidado}")