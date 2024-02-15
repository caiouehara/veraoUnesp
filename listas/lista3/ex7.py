import funcoes as mf
import matplotlib.pyplot as plt


def f1(t, x, y): return y
def f2(t, x, y): return 0.01 * x - 0.2 * x


condicao_inicial = [1, 1]
a = 0
b = 200
h = 10**(-4)
t_vector, x_vector, y_vector = mf.rk4_sistemas_2por2(
    f1, f2, condicao_inicial, a, b, h)


print('''
-------------------------------------------------------------------------------
Exercício 11
-------------------------------------------------------------------------------
''')
print(f'Solução da EDO x\'\' = 0.01x\' - 0.2x, x(0) = 1, x\'(0) = 1, com passo h=10**(-4) de 0 a 200 está no gráfico:')

plt.plot(t_vector, x_vector)
plt.title(f'Solução da EDO x\'\' = 0.01x\' - 0.2x, x(0) = 1, x\'(0) = 1, com passo h=10**(-4) de 0 a 200')
plt.xlabel('t')
plt.ylabel('x')
plt.grid(True)
plt.show()
