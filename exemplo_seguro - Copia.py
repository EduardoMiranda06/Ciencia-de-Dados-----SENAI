# (1) Carregamento das bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# (2) Entrada de dados
#dados = {"RAMO": ["Automóvel", "Saúde", "Incêndio", "Vida",
 #                 "Riscos Diversos", "Habitação", "Transporte",
  #                "Acidentes Pessoais", "Obrigatório Veículos",
   #               "Riscos de Engenharia", "Responsabilidade Civil"],
    #     "%": [33.6, 14.0, 12.9, 12.2, 5.5, 5.3, 3.1, 2.9, 1.7, 1.0, 0.9]}

arquivo = "dados_seguros3.csv"
dados_originais = pd.read_csv(arquivo, header =0 , delimiter= ";")  # Faz a leitura
dados= dados_originais.to_dict("list")  # Converte para a forma DICT
# (3) Processamento dos dados
# Construção do boxplot
coluna_percentual = dados["%"]              # Extrai a coluna % do DICT
boxplot = plt.boxplot(coluna_percentual)    # Constroi o boxplot

# Extração dos ramos de seguro com mais de 10.0%
lista_dos_ramos = []    # Cria uma lista vazia para preencher depois
contador = range(len(coluna_percentual))    # Cria um contador de 0
                                            # ao tamanho total
for indice in contador:     # Faz um laço em cima de todos os valores
    valor = coluna_percentual[indice]   # Pega o valor de percentual
    if (valor >= 10.0):                 # Testa se o valor é >= 10.0%
        nome_ramo = dados["RAMO"][indice]   # Em caso positivo, pega o nome
        lista_dos_ramos.append(nome_ramo)   # Adiciona à lista final

# (4) Apresentação dos resultados
print(dados)
print("Ramos maiores do que 10%: ", lista_dos_ramos)
plt.show()
