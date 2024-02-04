import funcoes as mf
import math
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio6/"

print(""" 
###############################################################################
#Exercício 6
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, y0, h, a, b, name):
      #Aplicação do método
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, y0, h, a, b)

      #Printando o resultado      
      print("Solução no último ponto aproximado: ", solucao_vetor[-1])
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(tempo_vetor), 2), dtype=float)
      for i in range(len(tempo_vetor)):
            matrix[i, 0] = tempo_vetor[i]
            matrix[i, 1] = solucao_vetor[i]
      np.savetxt(path + f'resultado_exemplo06_{name}.txt', matrix)

#Definição da Função
def funcaoA(t, y):
      return t*math.exp(3*t)-2*y

analiseFuncao(funcaoA, 0, 10**(-4), 0, 1, "Função A")

def funcaoB(t, y):
      return 1 + (t-y)**2

analiseFuncao(funcaoB, 1, 10**(-4), 2, 3, "Função B")

def funcaoC(t, y):
      return 1 + y/t

analiseFuncao(funcaoC, 2, 10**(-4), 1, 2, "Função C")

def funcaoD(t, y):
      return math.cos(2*t) + math.sin(3*t)

analiseFuncao(funcaoD, 1, 10**(-4), 0, 1, "Função D")
