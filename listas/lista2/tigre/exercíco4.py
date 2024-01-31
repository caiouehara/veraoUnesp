import funcoes as mf
import math

print(""" 
###############################################################################
#Exercício 4
###############################################################################
      """)

#Função análise
def analiseFuncao(funcaoAproximada, funcaoExata):
      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, 1, 10**(-3), 0, 15)

      #Cálculando a solução exata
      N = len(tempo_vetor)
      sol_exata_vetor = []
      for i in range(N):
            valor = funcaoExata(tempo_vetor[i], tempo_vetor[i]) # ?
            sol_exata_vetor.append(valor)

      #Cálculando o erro absoluto
      erro_abs = mf.erro_absoluto(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("Solução caso (a)\n")

      print("Solução mais próxima: ", solucao_vetor[-1])
      print("Erro absoluto do método: ", erro_abs)

      #Aplicação do método de Euler
      tempo_vetor, solucao_vetor = mf.euler(funcaoAproximada, 1, 10**(-8), 0, 15)

      #Cálculando o erro absoluto
      erro_abs = mf.erro_absoluto(sol_exata_vetor, solucao_vetor)

      #Printando o resultado
      print("Solução caso (b)\n")

      print("Solução mais próxima: ", solucao_vetor[-1])
      print("Erro absoluto do método: ", erro_abs)


#Definição da Função
def funcaoA(t, y):
      return 3 + t - y

def funcaoA_exata(t, y):
      return 3 + t - y

print("Função A\n")
analiseFuncao(funcaoA, funcaoA_exata)

print("""
      ###############################################################################
""")

#Definição da Função
def funcaoA(t, y):
      return 3 + t - y

def funcaoA_exata(t, y):
      return 3 + t - y

print("Função A\n")
analiseFuncao(funcaoA, funcaoA_exata)

print("""
      ###############################################################################
""")

#Definição da Função
def funcaoA(t, y):
      return 3 + t - y

def funcaoA_exata(t, y):
      return 3 + t - y

print("Função A\n")
analiseFuncao(funcaoA, funcaoA_exata)

print("""
      ###############################################################################
""")

