import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 6
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, y0, h, a, b):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, y0, h, a, b)

      #Printando o resultado      
      print("Solução no último ponto aproximado: ", solucao_vetor[-1])


#Definição da Função
def funcaoA(t, y):
      return t*math.exp(3*t)-2*y

analiseFuncao(funcaoA, 0, 10**(-4), 0, 1)

def funcaoB(t, y):
      return 1 + (t-y)**2

analiseFuncao(funcaoB, 1, 10**(-4), 2, 3)

def funcaoC(t, y):
      return 1 + y/t

analiseFuncao(funcaoC, 2, 10**(-4), 1, 2)

def funcaoD(t, y):
      return math.cos(2*t) + math.sin(3*t)

analiseFuncao(funcaoD, 1, 10**(-4), 0, 1)
