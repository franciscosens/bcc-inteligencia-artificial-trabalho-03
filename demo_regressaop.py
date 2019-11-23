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
import utils
import math

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

    def gerar_polyfit(self, valor_N, vetor_x, vetor_y):
        return np.polyfit(vetor_x, vetor_y, valor_N)[::-1]


    def gerar_linha(self, valor_n_regressao, vetor_x, vetor_y):
        novo_vetor_x = np.linspace(vetor_x[0], vetor_x[-1], num=len(vetor_x))
        novo_vetor_y = poly.polyval(novo_vetor_x, valor_n_regressao)

        Retorno_linha = namedtuple("Retorno", ["vetor_x", "vetor_y"])
        return Retorno_linha(novo_vetor_x, novo_vetor_y)
    

    def erro_quadratico_medio(self, vetor_y):
        
        quantidade_elementos_vetor_y = len(vetor_y)
        soma_y = utils.somar_valores(vetor_y, quantidade_elementos_vetor_y)
        media_y = soma_y / quantidade_elementos_vetor_y
        soma_residuo = 0.0

        for i in range(len(vetor_y)):
            y = vetor_y[i]
            soma_residuo = soma_residuo + math.pow((y - media_y), 2)

        return soma_residuo / quantidade_elementos_vetor_y


    def definir_variaveis(self, dados):
        for i, array in enumerate(dados.values):
            self.vetor_x.append(array[0])
            self.vetor_y.append(array[1])


    def ler_dados(self):
        return pd.read_csv('./assets/Dados/data_preg.csv')


    def gerar_grafico(self):

        #######################            INICIO GRAFICO 1            #######################################

        print('\n################# Dados normais #################\n')

        plt.figure(0)
        plt.scatter(self.vetor_x, self.vetor_y, marker='s', color='red', linewidth=1)

        #Questao - C
        linha_C = self.gerar_linha(self.gerar_polyfit(1, self.vetor_x, self.vetor_y), self.vetor_x, self.vetor_y)
        plt.plot(linha_C.vetor_x, linha_C.vetor_y, color='red')

        print('Questao - C - Primeira')
        print(self.erro_quadratico_medio(linha_C.vetor_y))

        #Questao - D
        linha_D = self.gerar_linha(self.gerar_polyfit(2, self.vetor_x, self.vetor_y), self.vetor_x, self.vetor_y)
        plt.plot(linha_D.vetor_x, linha_D.vetor_y, color='green')
        
        print('Questao - D - Primeira')
        print(self.erro_quadratico_medio(linha_D.vetor_y))

        #Questao - E
        linha_E = self.gerar_linha(self.gerar_polyfit(3, self.vetor_x, self.vetor_y), self.vetor_x, self.vetor_y)
        plt.plot(linha_E.vetor_x, linha_E.vetor_y, color='black')

        print('Questao - E - Primeira')
        print(self.erro_quadratico_medio(linha_E.vetor_y))

        #Questao - F
        linha_F = self.gerar_linha(self.gerar_polyfit(8, self.vetor_x, self.vetor_y), self.vetor_x, self.vetor_y)
        plt.plot(linha_F.vetor_x, linha_F.vetor_y, color='yellow')

        print('Questao - F - Primeira')
        print(self.erro_quadratico_medio(linha_F.vetor_y))

        #######################            FIM GRAFICO 1            #######################################






        #######################            INICIO GRAFICO 2            #######################################

        print('\n################# Dados treinamento #################\n')

        plt.figure(1)
        plt.scatter(self.vetor_x_treinamento, self.vetor_y_treinamento, marker='s', color='red', linewidth=1)

        #Questao - C - 2
        linha_C2 = self.gerar_linha(self.gerar_polyfit(1, self.vetor_x_treinamento, self.vetor_y_treinamento), self.vetor_x_treinamento, self.vetor_y_treinamento)
        plt.plot(linha_C2.vetor_x, linha_C2.vetor_y, color='red')

        print('Questao - C - Segunda')
        print(self.erro_quadratico_medio(linha_C2.vetor_y))

        #Questao - D - 2
        linha_D2 = self.gerar_linha(self.gerar_polyfit(2, self.vetor_x_treinamento, self.vetor_y_treinamento), self.vetor_x_treinamento, self.vetor_y_treinamento)
        plt.plot(linha_D2.vetor_x, linha_D2.vetor_y, color='green')

        print('Questao - D - Segunda')
        print(self.erro_quadratico_medio(linha_D2.vetor_y))

        #Questao - E - 2
        linha_E2 = self.gerar_linha(self.gerar_polyfit(3, self.vetor_x_treinamento, self.vetor_y_treinamento), self.vetor_x_treinamento, self.vetor_y_treinamento)
        plt.plot(linha_E2.vetor_x, linha_E2.vetor_y, color='black')

        print('Questao - E - Segunda')
        print(self.erro_quadratico_medio(linha_E2.vetor_y))

        #Questao - F - 2
        linha_F2 = self.gerar_linha(self.gerar_polyfit(8, self.vetor_x_treinamento, self.vetor_y_treinamento), self.vetor_x_treinamento, self.vetor_y_treinamento)
        plt.plot(linha_F2.vetor_x, linha_F2.vetor_y, color='yellow')

        print('Questao - C - Segunda')
        print(self.erro_quadratico_medio(linha_F2.vetor_y))

        #######################            FIM GRAFICO 2            #######################################

        print('\n################# Dados de teste #################\n')
        questao_i_linha_c = self.gerar_linha(self.gerar_polyfit(1, self.vetor_x_teste, self.vetor_y_teste), self.vetor_x_teste, self.vetor_y_teste)
        print('Questao C')
        print(self.erro_quadratico_medio(questao_i_linha_c.vetor_y))

        questao_i_linha_d = self.gerar_linha(self.gerar_polyfit(2, self.vetor_x_teste, self.vetor_y_teste), self.vetor_x_teste, self.vetor_y_teste)
        print('Questao E')
        print(self.erro_quadratico_medio(questao_i_linha_d.vetor_y))

        questao_i_linha_e = self.gerar_linha(self.gerar_polyfit(3, self.vetor_x_teste, self.vetor_y_teste), self.vetor_x_teste, self.vetor_y_teste)
        print('Questao E')
        print(self.erro_quadratico_medio(questao_i_linha_e.vetor_y))

        questao_i_linha_f = self.gerar_linha(self.gerar_polyfit(8, self.vetor_x_teste, self.vetor_y_teste), self.vetor_x_teste, self.vetor_y_teste)
        print('Questao F')
        print(self.erro_quadratico_medio(questao_i_linha_f.vetor_y))

        plt.show()


if __name__ == "__main__":
    q = Questao03()