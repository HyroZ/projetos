filmes = ["filme 1", "filme 2", "filme 3", "filme 4", "filme 5"]
print("Bem vindo á classificação do filme")
print("Você tem 8 filmes para classificar de 0 á 5 estrelas")
print("Digite 0 para parar")

for filme in filmes:
  classificacao = input(f"Como classifica '{filme}' de 1 a 5: ")

  if classificacao == '0':
    print("Que pena")
    break

  classificacao = int(classificacao)
  if classificacao <1 or classificacao >5:
    print("Nota inválida")
  else:
    print(f"Você classificou '{filme}' com a '{classificacao}' estrelas")