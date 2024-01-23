import numpy as np
import math
import funcoes as mf
from matplotlib import pyplot as plt

#Caminho para a pasta de resultados
path = "./aulas/aula6/results/"

# Pendulo amortecido
def theta_dot(t, theta, omega):
    return omega

def omega_dot(t, theta, omega):
    return -0.1*omega - 9.8*math.sin(theta)

condicao_inicial = (0.5, 0)
a = 0
b = 100
h = 10**(-3)
t, theta_vetor, omega_vetor = mf.rk4_sistemas2por2(theta_dot, omega_dot, condicao_inicial, a, b, h)

plt.figure()
plt.plot(t, theta_vetor)
plt.show()