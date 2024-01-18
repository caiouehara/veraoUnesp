import numpy as np

def estudo_pg(a1, q, n):
    an = a1*(q**(n-1))
    approx_sum = 0

    for n in range(1, n+1):
        approx_sum += an
        an = a1*(q**(n-1))

    real_sum = a1/(1 - q)
    abs_error = abs(real_sum - approx_sum)
    return approx_sum, real_sum, abs_error


a1, q, N = 10, 1/2, [50, 250, 1000]


def print_estudo_pg():
    for n in N:
        pg = estudo_pg(a1, q, n)
        print(f'O erro absoluto da pg com valor inicial {a1}, razao {q} \
                \n n = {n} é {pg[2]} \n')


print_estudo_pg()













