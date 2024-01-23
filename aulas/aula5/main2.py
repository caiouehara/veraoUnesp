import numpy as np
import math
import funcoes as mf
from matplotlib import pyplot as plt

#Caminho para a pasta de resultados
path = "./aulas/aula5/results/"

#Declaração do PVI
def pvi(t, y):
    return (1+t)/(1+y)

t_vetor, sol_euler_vetor = mf.euler(pvi, 2, 10**(-4), 1, 5)
t_vetor, sol_rk_vetor = mf.runge_kutta4(pvi, 2, 10**(-4), 1, 5)

N = len(t_vetor)
sol_exata_vetor = []
for i in range(N):
    valor = math.sqrt(t_vetor[i]**2+2*t_vetor[i]+6)-1
    sol_exata_vetor.append(valor)
    
erro_quadratico_medio_euler = mf.erro_quadratico_medio(sol_exata_vetor, sol_euler_vetor)
erro_quadratico_medio_rk = mf.erro_quadratico_medio(sol_exata_vetor, sol_rk_vetor)
print(erro_quadratico_medio_euler, erro_quadratico_medio_rk)

#Salvando o arquivo
matrix_euler = np.zeros((len(t_vetor), 2), dtype=float)
for i in range(len(t_vetor)):
    matrix_euler[i, 0] = t_vetor[i]
    matrix_euler[i, 1] = sol_euler_vetor[i]

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