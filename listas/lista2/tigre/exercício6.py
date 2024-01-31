import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, y0, h, a, b):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, y0, h, a, b)

      #Printando o resultado
      print("Solução caso (a)\n")

      print("Solução mais próxima: ", solucao_vetor[-1])


#Definição da Função
def funcaoA(t, y):
      return t*math.e**3*t-2*y

def funcaoB(t, y):
      return 3 + t - y

def funcaoA(t, y):
      return 3 + t - y

def funcaoA(t, y):
      return 3 + t - y

def funcaoA(t, y):
      return 3 + t - y

print("Função A\n")
analiseFuncao(funcaoA)

print("Função A\n")
analiseFuncao(funcaoA)

print("Função A\n")
analiseFuncao(funcaoA)

print("Função A\n")
analiseFuncao(funcaoA)