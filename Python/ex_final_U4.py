#Classificação de Flores Iris com Machine Learning

import tensorflow as tf
import pandas as pd
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Definir sementes pra facilitar os resultados

np.random.seed(42)
tf.random.set_seed(42)

iris = load_iris()

# X = características das flores
# y = números que representam as espécies
X = iris.data
y = iris.target

# Cria um DataFrame para visualizar os dados
df_iris = pd.DataFrame(X, columns=iris.feature_names)
df_iris["especie"] = [
    iris.target_names[i] for i in y
]

print("===== PRIMEIROS REGISTROS =====")
print(df_iris.head())

print("\n===== ESPÉCIES DISPONÍVEIS =====")
print(iris.target_names)

# 80% dos dados serão usados para treinar o modelo
# 20% serão usados para avaliar desempenho
X_treino, X_teste, y_treino, y_teste = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Normaliza as características usando StandardScaler
# O scaler aprende apenas com os dados de treinamento
escalador = StandardScaler()

X_treino = escalador.fit_transform(X_treino)
X_teste = escalador.transform(X_teste)

print("\n===== DIMENSÕES DOS DADOS =====")
print("Dados de treinamento:", X_treino.shape)
print("Dados de teste:", X_teste.shape)

modelo = tf.keras.Sequential([
    # Camada de entrada com quatro características
    tf.keras.layers.Input(shape=(4,)),

    # Primeira camada oculta
    tf.keras.layers.Dense(16, activation="relu"),

    # Segunda camada oculta
    tf.keras.layers.Dense(12, activation="relu"),

    # Camada de saída com três espécies possíveis
    tf.keras.layers.Dense(3, activation="softmax")
])

# Configura o processo de aprendizagem
modelo.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("\n===== ESTRUTURA DO MODELO =====")
modelo.summary()

historico = modelo.fit(
    X_treino,
    y_treino,
    epochs=100,
    batch_size=8,
    verbose=0,
    validation_split=0.2
)

print("\nTreinamento concluído!")


# Avaliar o modelo com dados que não foram utilizados durante o treinamento
perda, precisao = modelo.evaluate(
    X_teste,
    y_teste,
    verbose=0
)

print("\n===== AVALIAÇÃO DO MODELO =====")
print(f"Perda no teste: {perda:.4f}")
print(f"Acurácia no teste: {precisao * 100:.2f}%")

#Fazer previsões com o modelo treinado
probabilidades = modelo.predict(X_teste, verbose=0)

previsoes = np.argmax(probabilidades, axis=1)

# Compara as previsões com as espécies reais
resultado = pd.DataFrame({
    "Espécie real": [
        iris.target_names[i] for i in y_teste
    ],
    "Espécie prevista": [
        iris.target_names[i] for i in previsoes
    ],
    "Acertou": previsoes == y_teste
})

print("\n===== COMPARAÇÃO DAS PREVISÕES =====")
print(resultado.head(10).to_string(index=False))

# Testa uma nova flor com medidas em centímetros:
# sépala: comprimento e largura
# pétala: comprimento e largura
nova_flor = np.array([[5.1, 3.5, 1.4, 0.2]])

# Aplica a mesma normalização usada no treinamento
nova_flor_normalizada = escalador.transform(nova_flor)

# Prevê a espécie da nova flor
probabilidade_nova = modelo.predict(
    nova_flor_normalizada,
    verbose=0
)

indice_especie = np.argmax(probabilidade_nova[0])
especie_prevista = iris.target_names[indice_especie]
confianca = probabilidade_nova[0][indice_especie] * 100

print("\n===== PREVISÃO PARA UMA NOVA FLOR =====")
print("Espécie prevista:", especie_prevista)
print(f"Probabilidade atribuída à classe: {confianca:.2f}%")