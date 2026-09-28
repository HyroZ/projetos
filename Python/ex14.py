import matplotlib.pyplot as plt

class Produto:
  def __init__(self, nome, preco, categoria, estoque):
    self.nome = nome
    self.preco = preco
    self.categoria = categoria
    self.estoque = estoque

#Definimos como o produto aparece quando é impresso

  def __str__(self):
    return (f"{self.nome} - R$ {self.preco:.2f} - "
            f"Categoria: {self.categoria} - Estoque: {self.estoque}")

def remover_produto(nome_produto):
    produto_removido = False
    # Cria uma cópia do catálogo para não cometer erros
    for produto_obj in list(catalogo):
        if produto_obj.nome == nome_produto:
            catalogo.remove(produto_obj)
            # Remove a categoria se ela exisitr na lista de categorias gerais
            if produto_obj.categoria in categorias:
                categorias.remove(produto_obj.categoria)
            print(f"Produto '{nome_produto}' removido com sucesso!")
            produto_removido = True
            break
    if not produto_removido:
        print(f"Produto '{nome_produto}' não encontrado no catálogo.")

catalogo = []
categorias = []

def adicionar_produto(nome, preco, categoria, estoque):
  novo_produto = Produto(nome, preco, categoria, estoque)
  catalogo.append(novo_produto)
  categorias.append(categoria)
  print(f"Produto '{nome}' adicionado com sucesso!")

def listar_catalogo():
  print("--- Catálogo de Produtos: ---")
  for produto in catalogo:
    print(produto)

#Cadastrar Produtos
adicionar_produto("Camiseta", 29.99, "Roupas", 50)
adicionar_produto("Calça Jeans", 59.99, "Roupas", 30)
adicionar_produto("Tênis Esportivo", 89.99, "Calçados", 20)
adicionar_produto("Livro de Python", 39.99, "Livros", 100)
adicionar_produto("Cadeira de Escritório", 149.99, "Móveis", 15)

listar_catalogo()