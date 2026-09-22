class Pessoa:
  def __init__(self, nome, idade, genero):
    self.nome = nome
    self.idade = idade
    self.genero = genero
  def apresentar(self):
    print(f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou do gênero {genero}.")
  def cumprimentar(self):
   return f"Olá, meu nome é {self.nome}."

  def aniversario(self):
   self.idade += 1

pessoa1 = Pessoa("João", 25, "Masculino")
print(pessoa1.cumprimentar())
print(f"Idade: {pessoa1.idade}")

#Chama o método aniversário para aumentar a idade
pessoa1.aniversario()
print(f"Nova idade: {pessoa1.idade}")

#Herança - Classe-Pai Animal e duas Classe-Filhas
class Animal:
  def __init__(self, nome):
    self.nome = nome

  def fazer_barulho(self):
    pass   #método "vazio" que será sobrescrito pelas filhas

  class Cachorro(Animal):
    def fazer_barulho(self):
      return "Latir"

  class Gato(Animal):
    def fazer_barulho(self):
      return "Miar"

#Criando e usando objetos das Classes-Filhas


rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

print(f"{rex.nome} faz barulho: {rex.fazer_barulho()}")
print(f"{whiskers.nome} faz barulho: {whiskers.fazer_barulho()}")


#Classe Veículo (classe-pai)
class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.velocidade = 0

  def acelerar(self, valor):
    self.velocidade += valor

  def frear(self, valor):
    self.velocidade -= valor

  def status(self):
    return (f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade}")

#Classes-Filhas - Carro e Bicicleta
class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, potencia):
    super().__init__(marca, modelo, ano)             #super() = chama o construtor da Classe-Pai
    self.potencia = potencia

  def acelerar(self, incremento):
    self.velocidade += incremento + self.potencia

class Bicicleta(Veiculo):
  def  __init__(self, marca, modelo, ano, tipo):
    super().__init__(marca, modelo, ano)
    self.tipo = tipo


def status(self):
  return (f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, Velocidade: {self.velocidade} km/h, Tipo: {self.tipo}")

#Testando os objetos
carro1 = Carro("Toyota", "Corolla", 2022, 150)
bicicleta1 = Bicicleta("Trek", "Mountain Bike", 2021, "MTB")

carro1.acelerar(50)
bicicleta1.acelerar(20)

print("Status do Carro:")
print(carro1.status())
print("Status da Bicicleta:")
print(bicicleta1.status())