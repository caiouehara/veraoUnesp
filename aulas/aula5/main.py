import numpy as np
import math
import funcoes as mf
from matplotlib import pyplot as plt

#Declaração do PVI
def pvi(t, y):
    return math.cos(2*t) + math.sin(3*t)

t_vetor, sol_euler_vetor = mf.euler(pvi, 1, 10**(-3), 0, 5)
t_vetor, sol_rk_vetor = mf.runge_kutta4(pvi, 1, 10**(-3), 0, 5)

sol_exata = 1/2 * math.sin(2*5) - 1/3 * math.cos(3*5) + 4/3
sol_rk = sol_rk_vetor[-1]
sol_euler = sol_euler_vetor[-1]

print(sol_rk, sol_euler)

erro = abs(sol_exata - sol_euler)
print(erro)

erro = abs(sol_exata - sol_rk)
print(erro)

N = len(t_vetor)
sol_exata_vetor = []
for i in range(N):
    valor = 1/2 * math.sin(2*t_vetor[i]) - 1/3 * math.cos(3*t_vetor[i]) + 4/3
    sol_exata_vetor.append(valor)
    
erro_abs_med = mf.erro_absoluto_medio(sol_exata_vetor, sol_rk_vetor)
print(erro_abs_med)

path = "./aulas/aula5/results/"
#Salvando o arquivo
matrix_euler = np.zeros((len(t_vetor), 2), dtype=float)
for i in range(len(t_vetor)):
    matrix_euler[i, 0] = t_vetor[i]
    matrix_euler[i, 1] = sol_rk_vetor[i]

np.savetxt(path + "resultado_exemplo02_euler.txt", matrix_euler)

#Lendo o arquivo
resultado_euler = np.loadtxt(path + "resultado_exemplo02_euler.txt")
vetor_tempo = resultado_euler[:, 0]
vetor_euler = resultado_euler[:, 1]

#Gráfico
plt.figure()
plt.plot(vetor_tempo, vetor_euler, color = "red")
plt.xlabel("Tempo (t)")
plt.ylabel("Resultado via Euler (Exemplo 02)")
plt.show()