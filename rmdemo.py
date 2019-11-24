# Integrantes:
# • Bruno Geisler Vigentas
# • Francisco Lucas Sens
# • Gustavo Westarb
# • William Lopes da Silva

from collections import namedtuple
import math
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import utils

class CorrelacaoRegressaoLinearMultipla:

    def __init__(self):
        dados = self. ler_dados()

        variaveis = self.definir_variaveis(dados)

        # Matriz_x
        # 0 - Primeira coluna é sempre um
        # 1 - Segunda coluna é tamanho da casa
        # 2 - Terceira coluna é o número de quartos
        matriz_x = variaveis.matri_x
        vetor_y = variaveis.vetor_y

        correlacao_tamanho_casa = self.correlacao_por_variavel(1, matriz_x, vetor_y)
        correlacao_numero_quartos = self.correlacao_por_variavel(2, matriz_x, vetor_y)

        regressao = self.regressao(matriz_x, vetor_y)

        self.gerar_grafico(matriz_x, vetor_y, regressao, correlacao_tamanho_casa, correlacao_numero_quartos)


    def reg_multipla(self):
        pass

    def regressao(self, matriz_x, vetor_y):
        
        matriz_aux = np.array(matriz_x)

        #a = Xt*X
        multiplicacao_matriz = matriz_aux.T.dot(matriz_aux)
        
        #b = (a)-1
        matriz_potencia = inv(multiplicacao_matriz)

        #c = b * Xt
        potencia_matriz_transposta = np.dot(matriz_potencia, matriz_aux.T)
        
        #d = c * Y
        primeira_parte = np.dot(potencia_matriz_transposta, vetor_y)

        # Questão G
        matriz_aux_questao_G = np.array([1, 1650, 3])
        print('Questão G, resultado do preço da casa é: ')
        print(matriz_aux_questao_G.dot(primeira_parte))

        #X * d
        _regressao = matriz_aux.dot(primeira_parte)

        return np.array(_regressao)


    def gerar_grafico(self, matriz_x, vetor_y, regressao, correlacao_tamanho_casa, correlacao_numero_quartos):
        
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        matriz_np = np.array(matriz_x)

        ax.scatter(matriz_np[:, 1], matriz_np[:, 2], vetor_y, s = 20, color = 'green', marker='o')
        ax.set_xlabel('Correlaçao tamanho:' + '%.4f' % correlacao_tamanho_casa)
        ax.set_ylabel('Correlação quartos:' + '%.4f' % correlacao_numero_quartos)

        plt.plot(matriz_np[:, 1], matriz_np[:, 2], regressao, color = 'pink')
        plt.show()


    def correlacao_por_variavel(self, variavel, matriz_x , vetor_y):

        matriz_np = np.array(matriz_x)
        vetor_x = matriz_np[:, variavel]

        return utils.correlacao(vetor_x, vetor_y)


    def definir_variaveis(self, dados):
        
        matriz_aux = []
        vetor_y_aux = []

        for i, array in enumerate(dados.values):
            matriz_aux.append([1, array[0], array[1]])
            vetor_y_aux.append(array[2])
        
        _retorno = namedtuple("retorno", ["matri_x", "vetor_y"])

        return _retorno(matriz_aux, vetor_y_aux)


    def ler_dados(self):
        return pd.read_csv('.\/assets\/Dados\/data.csv')


if __name__ == "__main__":
    c = CorrelacaoRegressaoLinearMultipla()
