import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as plt


dados = "Lista - Coleta dos dados (Formatação e Equação)"
dados_originais = pd.read_csv(dados, header =0, delimiter= ";")
pd.read_csv(dados, header =0 , delimiter= ";")

media = np.mean(dados)
mediana = np.median(dados)
sigma = np.std(dados)

# Cálculos para o boxplot
Q1 = np.percentile(dados, 25, method='averaged_inverted_cdf')
Q2 = np.percentile(dados, 50, method='averaged_inverted_cdf')
Q3 = np.percentile(dados, 75, method='averaged_inverted_cdf')

dq = Q3-Q1
menor_valor = min(dados)
maior_valor = max(dados)

LI = max(menor_valor, Q1 - 1.5*dq)
LS = min(maior_valor, Q3 + 1.5*dq)

# (4) Apresentação dos resultados
print("A média dos dados é: ", media)
print("A mediana dos dados é: ", mediana)
print("O desvio-padrão dos dados é: ", sigma)

print("Q1 = ", Q1)
print("Q2 = ", Q2)
print("Q3 = ", Q3)

print("LI = ", LI)
print("LS = ", LS)

grafico = plt.boxplot(dados)
plt.show()