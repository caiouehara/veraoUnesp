import sympy as sp


x = sp.symbols('x')


def pretty_print(*f):
    N = len(f)
    for i in range(N):
        print(f'a função f{i} é dada por: {f[i]}\n'
              f'e a sua derivada é: {f[i].diff(x)}\n'
              f'{"-"*80}')


f1 = sp.cos(2*x)*sp.exp(x)*(x**2 + 5*x - sp.sin(x))
f2 = (3*(x**2)+5*+2)/(x**2 + x)
f3 = sp.sin(sp.sin(x)) + sp.exp(x)*sp.cos(x)+5


print('''
-------------------------------------------------------------------------------
Exercício 3
-------------------------------------------------------------------------------
''')

pretty_print(f1, f2, f3)

