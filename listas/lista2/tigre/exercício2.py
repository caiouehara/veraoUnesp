import funcoes as mf
import math
from matplotlib import pyplot as plt

print(""" 
###############################################################################
#Exercício 2
###############################################################################
      """)

print(""" 
------------------------------------------------------------------------------
#Exercício 2 (a)
------------------------------------------------------------------------------
      """)

def funcao(t, y):
    return 2*t*math.e**(2*t)+y

print("Solução caso (a)\n")
tempo_vetor1, solucao_vetor1 = mf.euler(funcao, 1, 10**(-1), 0, 15)

print("\nSolução caso (b)\n")
tempo_vetor2, solucao_vetor2 = mf.euler(funcao, 1, 10**(-2), 0, 15)

print("\nSolução caso (c)\n")
tempo_vetor3, solucao_vetor3 = mf.euler(funcao, 1, 10**(-4), 0, 15)

#Gráfico
plt.figure()
plt.plot(tempo_vetor1, solucao_vetor1, color = "red")
plt.plot(tempo_vetor2, solucao_vetor2, color = "blue")
plt.plot(tempo_vetor3, solucao_vetor3, color = "green")
plt.xlabel("Tempo (t)")
plt.ylabel("Resultado via Euler")
plt.yscale("log")
plt.show()

print(""" 
------------------------------------------------------------------------------
#Exercício 2 (b)
------------------------------------------------------------------------------
      """)

def funcao2(t, y):
    return 4+2*y-t

print("Solução caso (a)\n")
tempo_vetor1, solucao_vetor1 = mf.euler(funcao2, 2, 10**(-1), 0, 15)

print("\nSolução caso (b)\n")
tempo_vetor2, solucao_vetor2 = mf.euler(funcao2, 2, 10**(-2), 0, 15)

print("\nSolução caso (c)\n")
tempo_vetor3, solucao_vetor3 = mf.euler(funcao2, 1, 10**(-4), 0, 15)

#Gráfico
plt.figure()
plt.plot(tempo_vetor1, solucao_vetor1, color = "red")
plt.plot(tempo_vetor2, solucao_vetor2, color = "blue")
plt.plot(tempo_vetor3, solucao_vetor3, color = "green")
plt.xlabel("Tempo (t)")
plt.ylabel("Resultado via Euler")
plt.yscale("log")
plt.show()