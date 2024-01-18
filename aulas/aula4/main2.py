import numpy
import math
import funcoes as mf

#Declaração do PVI
def pvi_exponencial(t, y):
    return y

#Exemplo do Slide :: PVI y' = y com y(0) = 1 para [0,10] com h = 10^(-4)
t, sol_euler = mf.euler(pvi_exponencial, 0, 10, 10**(-4), 1)
t, sol_rk = mf.runge_kutta4(pvi_exponencial, 0, 10, 10**(-4), 1)

sol_exata = math.exp(0.6)
sol_rk = sol_rk[-1]
sol_euler = sol_euler[-1]

erro = abs(sol_exata - sol_euler)
print(erro)

erro = abs(sol_exata - sol_rk)
print(erro)