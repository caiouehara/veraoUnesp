import funcoes as mf
import math
import numpy as np

#Caminho para a pasta de resultados
path = "./listas/lista2/tigre/results/exercicio4/"

print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0, name):
      #Aplicação do método
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, y0, 10**(-3), 0, 15)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i])
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      erro_quad = mf.erro_quadratico(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("Solução caso (a)\n")

      print("Solução no último ponto mais próxima: ", solucao_vetor[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro quadrático médio do método: ", erro_quad)

      print("\n")

      #Aplicação do método de Euler
      _, solucao_vetor1 = mf.euler(funcaoAproximada, y0, 10**(-4), 0, 15)

      #Cálculando o erro absoluto
      erro_quad_1 = mf.erro_quadratico(sol_exata_vetor, solucao_vetor1)
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(tempo_vetor), 2), dtype=float)
      for i in range(len(tempo_vetor)):
            matrix[i, 0] = tempo_vetor[i]
            matrix[i, 1] = solucao_vetor[i]
      np.savetxt(path + f'resultado_exemplo04_A_{name}.txt', matrix)

      #Printando o resultado
      print("Solução caso (b)\n")

      print("Solução no último ponto aproximado: ", solucao_vetor1[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro quadrático do método: ", erro_quad_1)
      
      #Salvando o resultado em arquivo
      matrix = np.zeros((len(tempo_vetor), 2), dtype=float)
      for i in range(len(tempo_vetor)):
            matrix[i, 0] = tempo_vetor[i]
            matrix[i, 1] = solucao_vetor[i]
      np.savetxt(path + f'resultado_exemplo04_B_{name}.txt', matrix)
      
#Definição da Função (a)
def funcaoA(t, y):
      return 3 + t - y

def funcaoA_exata(t):
      return t - math.e**-t+2

print("Função A\n")
analiseFuncao(funcaoA, funcaoA_exata, 1, "FunçãoA")

print("""
      ###############################################################################
""")

#Definição da Função (b)
def funcaoB(t, y):
      return 2*y - 1

def funcaoB_exata(t):
      return 1/2*(math.e**2*t+1)

print("Função B\n")
analiseFuncao(funcaoB, funcaoB_exata, 1, "FunçãoB")

print("""
      ###############################################################################
""")

#Definição da Função (b)
def funcaoC(t, y):
      return 3*math.cos(t)-2*y

def funcaoC_exata(t):
      return (3/5)*(-2*math.exp(-2*t)+math.sin(t)+2*math.cos(t))

print("Função C\n")
analiseFuncao(funcaoC, funcaoC_exata, 0, "FunçãoC")
