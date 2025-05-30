import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as plt
arquivo = "AMOSTRAS.csv"
dados_originais = pd.read_csv(arquivo, header =0 , delimiter= ";")  # Faz a leitura
dados= dados_originais.to_dict("list")  # Converte para a forma DICT
print(dados_originais)

lista_diametro = 14.98,14.53,16.52,14.88,12.57,15.69,14.01,17.18
lista_altura = 21.24,20.69,23.16,25.84,25.58,26.92,27.64,29.22
lista_massa =4.26,4.06,

#calculo da média
media = np.mean(dados_originais)
print(media)