# Integrantes:
# • Bruno Geisler Vigentas
# • Francisco Lucas Sens
# • Gustavo Westarb
# • William Lopes da Silva

from collections import namedtuple
import matplotlib.pyplot as plt
import numpy as np
import numpy.polynomial.polynomial as poly
import pandas as pd
import random

class Questao03:

    def __init__(self):
        self.vetor_x = []
        self.vetor_y = []
        self.vetor_x_treinamento = []
        self.vetor_y_treinamento = []
        self.vetor_x_teste = []
        self.vetor_y_teste = []

        self.definir_variaveis(self.ler_dados())
        self.gerar_vetor_aleatoriamente()
        self.gerar_grafico()

    def gerar_vetor_aleatoriamente(self):
        quantidade_10_porcento = int((len(self.vetor_x) * 10) / 100)
        posicoes_vetor = [i for i in range(len(self.vetor_x))]
        posicoes_teste = random.choices(posicoes_vetor, k=quantidade_10_porcento) 
        posicoes_treinamento = [x for x in posicoes_vetor if x not in posicoes_teste]
        self.vetor_x_treinamento = [self.vetor_x[i] for i in posicoes_treinamento]
        self.vetor_y_treinamento = [self.vetor_y[i] for i in posicoes_treinamento]
        self.vetor_x_teste = [self.vetor_x[i] for i in posicoes_teste]
        self.vetor_y_teste = [self.vetor_y[i] for i in posicoes_teste]

    def gerar_polyfit(self, valor_N):
        return np.polyfit(self.vetor_x, self.vetor_y, valor_N)[::-1]


    def gerar_linha(self, valor_n_regressao):
        novo_vetor_x = np.linspace(self.vetor_x[0], self.vetor_x[-1], num=len(self.vetor_x)*10)
        novo_vetor_y = poly.polyval(novo_vetor_x, valor_n_regressao)

        Retorno_linha = namedtuple("Retorno", ["vetor_x", "vetor_y"])
        return Retorno_linha(novo_vetor_x, novo_vetor_y)


    def definir_variaveis(self, dados):
        for i, array in enumerate(dados.values):
            self.vetor_x.append(array[0])
            self.vetor_y.append(array[1])


    def ler_dados(self):
        return pd.read_csv('.\/assets\/Dados\/data_preg.csv')


    def gerar_grafico(self):
        plt.scatter(self.vetor_x, self.vetor_y, marker='s',  color='red', linewidth=1)

        #Questao - C
        linha_C = self.gerar_linha(self.gerar_polyfit(1))
        plt.plot(linha_C.vetor_x, linha_C.vetor_y, color='red')

        #Questao - D
        linha_D = self.gerar_linha(self.gerar_polyfit(2))
        plt.plot(linha_D.vetor_x, linha_D.vetor_y, color='green')
        
        #Questao - E
        linha_E = self.gerar_linha(self.gerar_polyfit(3))
        plt.plot(linha_E.vetor_x, linha_E.vetor_y, color='black')

        #Questao - F
        linha_F = self.gerar_linha(self.gerar_polyfit(8))
        plt.plot(linha_F.vetor_x, linha_F.vetor_y, color='yellow')

        plt.show()


if __name__ == "__main__":
    q = Questao03()