#O evento científico
import numpy as np

#Cada participante é um Dicionário (mapping)
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