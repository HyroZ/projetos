# SQLite + Pandas + Matplotlib + Seaborn
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configura o estilo dos gráficos
sns.set_theme(style="whitegrid")

# Conecta ao banco de dados SQLite
conexao = sqlite3.connect("dados_vendas.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
""")

# Insere os dados de exemplo somente se a tabela estiver vazia.
# Isso evita duplicar os registros ao executar novamente o código.
cursor.execute("SELECT COUNT(*) FROM vendas1")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""
        INSERT INTO vendas1
        (data_venda, produto, categoria, valor_venda)
        VALUES (?, ?, ?, ?)
    """, [
        ('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
        ('2023-01-05', 'Produto B', 'Roupas', 350.00),
        ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
        ('2023-03-15', 'Produto D', 'Livros', 200.00),
        ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
        ('2023-04-02', 'Produto F', 'Roupas', 400.00),
        ('2023-05-05', 'Produto G', 'Livros', 150.00),
        ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
        ('2023-07-20', 'Produto I', 'Roupas', 600.00),
        ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
        ('2023-09-30', 'Produto K', 'Livros', 300.00),
        ('2023-10-05', 'Produto L', 'Roupas', 450.00),
        ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
        ('2023-12-20', 'Produto N', 'Livros', 250.00)
    ])

# Salva as alterações no banco de dados
conexao.commit()

# PASSO 2: Carregar e explorar os dados com Pandas
# Lê os dados da tabela e cria um DataFrame
df_vendas = pd.read_sql_query(
    "SELECT * FROM vendas1", conexao
)

# Converte a coluna de datas para o formato datetime
df_vendas["data_venda"] = pd.to_datetime(
    df_vendas["data_venda"]
)

# Exibe os primeiros registros
print("===== PRIMEIROS REGISTROS =====")
print(df_vendas.head())

# Verifica os tipos de dados e a quantidade de registros
print("\n===== INFORMAÇÕES DO DATAFRAME =====")
df_vendas.info()

print("\n===== VALORES AUSENTES =====")
print(df_vendas.isnull().sum())

#Análise dos dados de vendas

faturamento_total = df_vendas["valor_venda"].sum()
total_vendas = len(df_vendas)
ticket_medio = df_vendas["valor_venda"].mean()

print("\n===== INDICADORES GERAIS =====")
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Quantidade de vendas: {total_vendas}")
print(f"Valor médio por venda: R$ {ticket_medio:,.2f}")

# Agrupa as vendas por categoria e soma os valores
vendas_categoria = (
    df_vendas.groupby("categoria")["valor_venda"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== FATURAMENTO POR CATEGORIA =====")
print(vendas_categoria)

# Identifica o produto com maior valor de venda
produto_destaque = df_vendas.loc[
    df_vendas["valor_venda"].idxmax()
]

print("\n===== PRODUTO COM MAIOR VALOR DE VENDA =====")
print(f"Produto: {produto_destaque['produto']}")
print(f"Valor: R$ {produto_destaque['valor_venda']:.2f}")

# Cria uma coluna com o mês da venda
df_vendas["mes"] = df_vendas["data_venda"].dt.month

# Calcula o faturamento de cada mês
vendas_mensais = (
    df_vendas.groupby("mes")["valor_venda"]
    .sum()
    .reindex(range(1, 13), fill_value=0)
)

# Identifica o mês com maior faturamento
mes_destaque = vendas_mensais.idxmax()

print("\n===== FATURAMENTO MENSAL =====")
print(vendas_mensais)
print(f"Mês com maior faturamento: {mes_destaque}")

# PASSO 4: Visualização dos dados

# Gráfico 1: Faturamento mensal usando Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(
    vendas_mensais.index,
    vendas_mensais.values,
    marker="o"
)
plt.title("Faturamento Mensal")
plt.xlabel("Mês")
plt.ylabel("Faturamento (R$)")
plt.xticks(range(1, 13))
plt.tight_layout()
plt.show()

# Gráfico 2: Faturamento por categoria usando Seaborn
plt.figure(figsize=(9, 5))
sns.barplot(
    x=vendas_categoria.index,
    y=vendas_categoria.values
)
plt.title("Faturamento por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")
plt.tight_layout()
plt.show()

# Gráfico 3: Distribuição dos valores das vendas
plt.figure(figsize=(9, 5))
sns.histplot(
    data=df_vendas,
    x="valor_venda",
    bins=6,
    kde=True
)
plt.title("Distribuição dos Valores de Venda")
plt.xlabel("Valor da venda (R$)")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

# PASSO 5: Relatório final com insights

print("\n===== RELATÓRIO FINAL =====")
print(f"Faturamento total: R$ {faturamento_total:,.2f}")
print(f"Categoria com maior faturamento: {vendas_categoria.idxmax()}")
print(f"Faturamento dessa categoria: R$ {vendas_categoria.max():,.2f}")
print(f"Mês de maior faturamento: {mes_destaque}")
print(f"Valor médio por venda: R$ {ticket_medio:,.2f}")

# Encerra a conexão com o banco de dados
conexao.close()
