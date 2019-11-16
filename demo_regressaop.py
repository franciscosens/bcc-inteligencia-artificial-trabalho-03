from collections import namedtuple
import matplotlib.pyplot as plt
import pandas as pd

class Questao03:

    def __init__(self):
        self.vetor_x = []
        self.vetor_y = []

        self.definir_variaveis(self.ler_dados())
        self.gerar_grafico()


    def definir_variaveis(self, dados):
        for i, array in enumerate(dados.values):
            self.vetor_x.append(array[0])
            self.vetor_y.append(array[1])

    def ler_dados(self):
        return pd.read_csv('.\/assets\/Dados\/data_preg.csv')

    def gerar_grafico(self):
        plt.scatter(self.vetor_x, self.vetor_y, marker='s',  color='red', linewidth=1)
        plt.show()


if __name__ == "__main__":
    q = Questao03()