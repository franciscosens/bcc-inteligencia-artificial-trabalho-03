# Integrantes:
# • Bruno Geisler Vigentas
# • Francisco Lucas Sens
# • Gustavo Westarb
# • William Lopes da Silva

import math

def correlacao(vetor_x, vetor_y):

    quantidade_elementos_x = len(vetor_x)
    quantidade_elementos_y = len(vetor_y)

    soma_x = somar_valores(vetor_x, quantidade_elementos_x)
    media_x = soma_x / quantidade_elementos_x

    soma_y = somar_valores(vetor_y, quantidade_elementos_y)
    media_y = soma_y / quantidade_elementos_y

    soma_parte_baixo_1 = 0.0
    soma_parte_baixo_2 = 0.0
    soma_parte_cima = 0.0
    
    for i in range(quantidade_elementos_x):
        x = float(vetor_x[i])
        y = float(vetor_y[i])

        parte_cima_1 = x - media_x
        parte_cima_2 = y - media_y
        soma_parte_cima = soma_parte_cima + (parte_cima_1 * parte_cima_2)

        parte_baixo_1 = math.pow((x - media_x), 2)
        soma_parte_baixo_1 = soma_parte_baixo_1 + parte_baixo_1

        parte_baixo_2 = math.pow((y - media_y), 2)
        soma_parte_baixo_2 = soma_parte_baixo_2 + parte_baixo_2

    parte_baixo = soma_parte_baixo_1 * soma_parte_baixo_2
    parte_baixo = math.sqrt(parte_baixo)

    coefiente_correlacao = soma_parte_cima / parte_baixo

    return coefiente_correlacao

def somar_valores(vetor, quantidade_elementos):
    soma = 0.0
    for i in range(quantidade_elementos):
        soma = soma + vetor[i]
    return soma