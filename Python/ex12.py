import numpy as np#Cada participante é um Dicionário (mapping)
participantes = [
    {'nome': 'Alice', 'localizacao': "EUA", 'afiliacao': "Universidade A",
     "interesses": ["Física", "Astronomia"]},
    {'nome': 'Bob', 'localizacao': "Brasil", 'afiliacao': "Instituicao B",
     "interesses": ["Biologia", "Astronomia"]},
    {'nome': 'Charlie', 'localizacao': "Índia", 'afiliacao': "Instituto C",
     "interesses": ["Química", "Engenharia"]}
]

#Set - Regiões dos participantes (sem duplicar)
regioes = set(p["localizacao"] for p in participantes)

#Dict - agrupando nomes por afiliação
afiliacoes = {}
for p in participantes:
  aff = p["afiliacao"]
  if aff not in afiliacoes:
    afiliacoes[aff] = []
  afiliacoes[aff].append(p["nome"])

#NumPy - Área de interesse mais popular
areas = np.array([i for p in participantes for i in p["interesses"]])
unicos, contagem = np.unique(areas, return_counts=True)
mais_popular = unicos[np.argmax(contagem)]

#Resultados
print("Regiões dos participantes:", regioes)
print("Afiliações dos participantes:")
for aff, nomes in afiliacoes.items():
  print(f" {aff}: {', '.join(nomes)}")
print(f"Área de interesse mais popular: {mais_popular}")