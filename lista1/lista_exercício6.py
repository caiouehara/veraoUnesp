import numpy as np

#Exercício 6
def erro_cometido(n, a1=float(10), q=float(0.5)):
    resutaldo_aproximado = float(a1) * ( float(q) **(float(n)-1) )
    resultado_real = float(a1) / (1-float(q))
    print(resultado_real - resutaldo_aproximado)

erro_cometido(5)
erro_cometido(50)
erro_cometido(250)
erro_cometido(1000)