import sympy as sp


s, t, a, b = sp.symbols('s, t, a, b')


def pretty_print(*f):
    N = len(f)
    for i in range(N):
        F = sp.exp(-s*t)*f[i]
        print('O laplaciano da função ', f[i])
        print('é dado por: ', 
              sp.simplify(sp.integrate(F, I, conds='none')))
        print('-'*80)

I = (t, 0, sp.oo)
f1 = 1
f2 = sp.sin(a*t)
f3 = sp.cos(a*t)
f4 = sp.exp(a*t)*sp.sin(b*t)

print('''
-------------------------------------------------------------------------------
Exercício 12
-------------------------------------------------------------------------------
''')

pretty_print(f1, f2, f3, f4)

