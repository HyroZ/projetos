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