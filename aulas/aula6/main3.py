import numpy as np
import math
import funcoes as mf
from matplotlib import pyplot as plt

#Caminho para a pasta de resultados
path = "./aulas/aula6/results/"

# Presa Predador
def x_dot(t, x, y):
    return x*(1-y)

def y_dot(t, x, y):
    return y*(x-1)

condicao_inicial = (5, 2)
a = 0
b = 100
h = 10**(-3)
t, theta_vetor, omega_vetor = mf.rk4_sistemas_2por2(x_dot, y_dot, condicao_inicial, a, b, h)

plt.figure()
plt.plot(t, theta_vetor)
plt.show()