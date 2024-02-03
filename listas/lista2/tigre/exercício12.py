import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 12
###############################################################################
      """)
      
#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata, y0, h, a, b, methodName):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.methods[methodName](funcaoAproximada, y0, h, a, b)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i])
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      erro_quad = mf.erro_quadratico(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("\nSolução\n")

      print("Solução no último ponto mais próxima: ", solucao_vetor[-1])
      print("Solução no último ponto exata", sol_exata_vetor[-1])
      print("Erro quadrádico: ", erro_quad)
      
      return erro_quad
      
#Definição das funções
def funcaoA(t, y):
      return t*math.exp(3*t)-2*y

def funcaoA_exata(t):
      return (1/5)*t*math.exp(3*t)-(1/25)*math.exp(3*t)+(1/25)*math.exp(-2*t)


def funcaoB(t, y):
      return 1 + (t-y)**2

def funcaoB_exata(t):
      return t + 1/(1-t)

def funcaoC(t, y):
      return 1 + y/t

def funcaoC_exata(t):
      return t*math.log(t)+2*t


def funcaoD(t, y):
      return math.cos(2*t) + math.sin(3*t)

def funcaoD_exata(t):
      return 1/2*math.sin(2*t)-(1/3)*math.cos(3*t)+(4/3)

print("Aplicação do Heun \n")
analiseFuncao(funcaoA, funcaoA_exata, 0, 10**(-4), 0, 1, "heun")
analiseFuncao(funcaoB, funcaoB_exata, 1, 10**(-4), 2, 3, "heun")
analiseFuncao(funcaoC, funcaoC_exata, 2, 10**(-4), 1, 2, "heun")
analiseFuncao(funcaoD, funcaoD_exata, 1, 10**(-4), 0, 1, "heun")