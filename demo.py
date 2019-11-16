from collections import namedtuple
import math
import numpy as np
import utils
import matplotlib.pyplot as plt

x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]


class CorrelacaoRegressaoLinear:
    def __init__(self):
        vetor_x = x1
        vetor_y = y1

        correlacao = utils.correlacao(vetor_x, vetor_y)
        regressao = self.regressao(vetor_x, vetor_y)
        self.gerar_grafico(vetor_x, vetor_y, correlacao, regressao)


    def gerar_grafico(self, vetor_x, vetor_y, correlacao, regressao):

        plt.scatter(vetor_x, vetor_y, marker='s',  color='red', linewidth=1)
        plt.plot(vetor_x, regressao.valores_y)

        b0 = '%.4f' % regressao.b0
        b1 = '%.4f' % regressao.b1
        correlacao_arredondada = '%.4f' % correlacao

        plt.title(f'Correlação: {correlacao_arredondada} e Regressão => b0 : {b0} b1 : {b1}')
        plt.show()

    def regressao(self, vetor_x, vetor_y):

        quantidade_elementos_x = len(vetor_x)
        quantidade_elementos_y = len(vetor_y)

        soma_x = utils.somar_valores(vetor_x, quantidade_elementos_x)
        media_x = soma_x / quantidade_elementos_x

        soma_y = utils.somar_valores(vetor_y, quantidade_elementos_y)
        media_y = soma_y / quantidade_elementos_y

        soma_parte_cima = 0.0
        soma_parte_baixo = 0.0

        for i in range(quantidade_elementos_x):
            x = vetor_x[i]
            y = vetor_y[i]

            parte_cima_1 = x - media_x
            parte_cima_2 = y - media_y
            soma_parte_cima = soma_parte_cima + (parte_cima_1 * parte_cima_2)

            soma_parte_baixo = soma_parte_baixo + math.pow((x - media_x), 2)

            # TODO verificar se isto deve ficar dentro das iterações ou não
        b1 = soma_parte_cima / soma_parte_baixo
        b0 = media_y - b1 * media_x
        valores_y = []

        for i in range(quantidade_elementos_x):
            x = vetor_x[i]
            y = b0 + b1 * x
            valores_y.append(y)
        Retorno = namedtuple("Retorno", ["b0", "b1", "valores_y"])

        return Retorno(b0, b1, valores_y)


if __name__ == "__main__":
    c = CorrelacaoRegressaoLinear()
