import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

arquivo = "CIDA.csv"
dados_originais = pd.read_csv(arquivo, header =0 , delimiter= ";")  # Faz a leitura
dados= dados_originais.to_dict("list")  # Converte para a forma DICT

#  Processamento dos dados

coluna_percentual = dados["%"]
boxplot = plt.boxplot(coluna_percentual)


Mestrado = []
contador = range(len(coluna_percentual))

Doutorado = []
contador = range(len(coluna_percentual))

Bacharel = []
contador = range(len(coluna_percentual))

# (4) Apresentação dos resultados
print(dados)
plt.show()