import numpy
import math
import funcoes as mf

#Declaração do PVI
def pvi_exponencial(t, y):
    return y

#Exemplo do Slide :: PVI y' = y com y(0) = 1 para [0,10] com h = 10^(-4)
t, sol_euler = mf.euler(pvi_exponencial, 0, 10, 10**(-4), 1)
t, sol_numerica = mf.euler(pvi_exponencial, 0, 10, 10**(-4), 1)

# Calcular a Solução Exata y = exp(t)
sol_exata = []
N = len(t)
for i in range(N):
    valor_exato = math.exp(t[i])
    sol_exata.append(valor_exato)
    
#Erro Absoluto
erro_absoluto = mf.erro_absoluto(sol_exata, sol_numerica)
print(erro_absoluto)

#Erro Absoluto médio
erro_absoluto_medio = mf.erro_absoluto_medio(sol_exata, sol_numerica)
print(erro_absoluto)

#Erro Quadrático
erro_quadratico = mf.erro_quadratico(sol_exata, sol_numerica)
print(erro_quadratico)

#Erro Quadrático médio
erro_quadratico_medio = mf.erro_quadratico_medio(sol_exata, sol_numerica)
print(erro_quadratico_medio)

