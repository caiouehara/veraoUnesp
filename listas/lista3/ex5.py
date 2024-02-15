import sympy as sp


x = sp.symbols('x')


def pretty_print(*f):
    N = len(f)
    for i in range(N):
        print(f'a função f{i+1} é dada por: {f[i][0]}\n'
              f'e a sua integral no intervalo {f[i][1]} é dada por: {sp.integrate(f[i][0], f[i][1])}\n'
              f'{"-"*80}')


f1 = [1/(x**2 + 9), I1:=(x, 3, sp.oo)]
f2 = [1/(2*x - 3)**2, I2:=(x, -sp.oo, 1)]
f3 = [x*sp.exp(-x**2), I3:=(x, 0, sp.oo)]
f4 = [1/sp.log(x), I4:=(x, 2, sp.oo)]
f5 = [x*sp.sin(x), I5:=(x, 0, sp.oo)]
f6 = [x/(x**4 + 9), I6:=(x, -sp.oo, sp.oo)]
f7 = [1/(x-1)**3, I7:=(x, -sp.oo, 0)]

print('''
-------------------------------------------------------------------------------
Exercício 5
-------------------------------------------------------------------------------
''')

pretty_print(f1, f2, f3, f4, f5, f6, f7)

