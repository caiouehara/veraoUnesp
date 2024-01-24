import numpy as np
import math
import funcoes as mf
from matplotlib import pyplot as plt

#Caminho para a pasta de resultados
path = "./aulas/aula6/results/"

# Um atrator "estranho" em 3 dimensões
def x_dot(t, x, y, z):
    return 3*x*(1-y)-2.2*z

def y_dot(t, x, y, z):
    return -y*(1-x**2)

def z_dot(t, x, y, z):
    return 0.001*x

# Condições Numéricas de Integração
condicao_inicial = (1, 1, 0)
a = 0
b = 1000
h = 10**(-3)

# Chamar o rk4 para sistemas 3 por 3
t, x_vec, y_vec, z_vec = mf.rk4_sistemas_3por3(
    x_dot, 
    y_dot, 
    z_dot, 
    condicao_inicial, 
    a, 
    b, 
    h
)

#Salvando em estrutura matricial
#atrator = np.zeros((len(t), 3), dtype=float)
#atrator[:, 0] = x_vec
#atrator[:, 1] = y_vec
#atrator[:, 2] = z_vec
atrator = np.column_stack((x_vec, y_vec, z_vec))

plt.figure().add_subplot(projection = '3d')
plt.plot(*atrator.T)
plt.show()