import funcoes as mf
import numpy as np
from matplotlib import pyplot as plt

def x_dot(t, x, y, z):
    return 3*x*(1-y)-2.2*z
def y_dot(t, x, y, z):
    return -y*(1*(x**2))
def z_dot(t, x, y, z):
    return 0.001*x

condicao_inicial = (-3, 7, 4)
h = 10**(-3)

t_vetor, x_vetor, y_vetor, z_vetor = mf.rk4_sistemas_3por3(
    x_dot,
    y_dot,
    z_dot,
    condicao_inicial,
    0,
    1000,
    10**(-3),
)

atrator = np.zeros((len(t_vetor), 3), dtype=float)
atrator[:, 0] = x_vetor
atrator[:, 1] = y_vetor
atrator[:, 2] = z_vetor

plt.figure().add_subplot(projection = "3d")
plt.plot(*atrator.T)
plt.show()

#Descarte de Transiente
x_descartado = mf.descarte_de_transiente(0.28, x_vetor)
y_descartado = mf.descarte_de_transiente(0.28, y_vetor)
z_descartado = mf.descarte_de_transiente(0.28, z_vetor)

atrator2 = np.zeros((len(t_vetor), 3), dtype=float)
atrator2[:, 0] = x_descartado
atrator2[:, 1] = y_descartado
atrator2[:, 2] = z_descartado

plt.figure().add_subplot(projection = "3d")
plt.plot(*atrator2.T)
plt.show()