import numpy
import math
import funcoes as mf

#Declaração do PVI
def pvi(t, y):
    return math.cos(2*t) + math.sin(3*t)

t, sol_euler_vetor = mf.euler(pvi, 1, 10**(-3), 0, 5)
t, sol_rk_vetor = mf.runge_kutta4(pvi, 1, 10**(-3), 0, 5)

sol_exata = 1/2 * math.sin(2*5) - 1/3 * math.cos(3*5) + 4/3
sol_rk = sol_rk_vetor[-1]
sol_euler = sol_euler_vetor[-1]

print(sol_rk, sol_euler)

erro = abs(sol_exata - sol_euler)
print(erro)

erro = abs(sol_exata - sol_rk)
print(erro)

N = len(t)
sol_exata_vetor = []
for i in range(N):
    valor = 1/2 * math.sin(2*t[i]) - 1/3 * math.cos(3*t[i]) + 4/3
    sol_exata_vetor.append(valor)
    
erro_abs_med = mf.erro_absoluto_medio(sol_exata_vetor, sol_rk_vetor)
print(erro_abs_med)
