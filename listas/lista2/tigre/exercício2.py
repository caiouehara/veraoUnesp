import funcoes as mf
import math

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

print("Erro caso(a)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-1), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])

print("\nErro caso(b)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-2), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])

print("\nErro caso(c)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-4), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])

print(""" 
------------------------------------------------------------------------------
#Exercício 2 (b)
------------------------------------------------------------------------------
      """)

def funcao(t, y):
    return 4+2*y-t

print("Erro caso(a)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-1), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])

print("\nErro caso(b)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-2), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])

print("\nErro caso(c)\n")
tempo_vetor, solucao_vetor = mf.euler(funcao, 2, 10**(-4), 0, 15)
print(tempo_vetor[-1], solucao_vetor[-1])