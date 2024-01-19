import numpy as np

#Exercício 7
def erro_cometido(n, a1=float(10), q=float(0.5)):
    #Cálculo dos resultados
    resutaldo_aproximado = float(a1) * ( float(q) **(float(n)-1) )
    resultado_real = float(a1) / (1-float(q))
    return resultado_real-resutaldo_aproximado

for n in range(1, 10000):
    E = erro_cometido(n, 3, 0.1)
    
    if(E >= 10**-2):
        print("O 'n' para o item (c) é: ", n)
    
    if(E >= 10**-5):
        print("O 'n' para o item (b) é: ", n)
        
    if(E >= 10**-10):
        print("O 'n' para o item (a) é: ", n)
        break


        