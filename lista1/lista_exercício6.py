import numpy as np

#Exercício 6
def erro_cometido(n, a1=float(10), q=float(0.5)):
    #Cálculo dos resultados
    resutaldo_aproximado = float(a1) * ( float(q) **(float(n)-1) )
    resultado_real = float(a1) / (1-float(q))
    
    #Impressão
    print("Erro cometido de : ", resultado_real - resutaldo_aproximado)

#Execucção do código
erro_cometido(50)
erro_cometido(250)
erro_cometido(1000)