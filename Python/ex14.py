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