from math import ceil, sqrt, log
import sympy as sp
x = sp.Symbol('x')

""" faremos este exercício de dois jeitos, da forma simples e da forma que vai 
rodar no meu pc, utilizando o teorema de Euclides-Euler e o crivo de Eratóstones
"""

""" primeiro, segue o algoritmo a bruta força """

def dumb_factorize(N):   
    factors = [1]  # 1 é fator d todo mundo
    # Note que precisamos checar só até o maior inteiro vizinho de N/2 para o nosso exercício
    n = ceil(N/2) + 1
    for q in range(2, n):
        if N % q == 0:
            factors.append(q)
    return factors 

def dumb_perfect_int_finder(N):
    perfect_int = []
    for n in range(N+1):
        factors = dumb_factorize(n)
        if len(factors) != 1 and sum(factors) == n:
            perfect_int.append(n)
    return perfect_int


""" Agora, utilizando o teorema de Euclides-Euler, que diz que um número é 
perfeito se, e somente se, ele tem a forma 2**(n-1) * (2**n - 1)"""

#Implementando o crivo de Eratóstones para obter os primos 
def prime_finder(N):
    #fazendo o crivo 
    crivo = [True for i in range(N+1)] 
    for p in range(2, int(sqrt(N))):
        if crivo[p]:
            for i in range(p * p, N+1, p):
                crivo[i] = False
    #tirando os números que o crivo deu como falso
    primes = []
    for p in range(2, N+1):
        if crivo[p]:
            primes.append(p)
    return primes


def smart_perfect_int_finder(N):  # Ache os números perfeitos até N
    """Note que precisamos encontrar os primos apenas até o (2**nn - 1), onde
    nn é a solução de 2**(nn-1)*(2**nn - 1) = N. Usaremos sympy para encontrar nn"""
    nn = ceil(sp.N(sp.solve(2**(x-1) * (2**x - 1) - N, x)[1]) + 1)
    perfect_int = []
    NN = (2**nn - 1)
    primes = prime_finder(NN)
    for n in range(NN):
        if (2**n - 1) in primes:
            perfect_int.append(2**(n-1) * (2**n - 1))
    return perfect_int


print('''
-------------------------------------------------------------------------------
Exercício 11
-------------------------------------------------------------------------------
''')
print(''' faremos este exercício de duas formas, da forma óbvia, e da forma 
que vai rodar no meu pc, utilizando o teorema de Euclides-Euler 
(junto ao crivo de Eratóstones), cortesia do livro Introdução a Teoria dos 
Números pelos professores Sampaio e Caetano da UFSCar''')
print('-'*80)
print('Primeiro, com algoritmo usando o teorema de Euclides-Euler, encontraremos os inteiros perfeitos até 10**8')
print(smart_perfect_int_finder(10**8))
print('-'*80)
print('Agora, pelo algoritmo mais óbvio, faremos o mesmo até 10**5')
print(dumb_perfect_int_finder(10**5))

