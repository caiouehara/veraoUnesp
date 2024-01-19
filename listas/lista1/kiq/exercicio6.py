
def estudo_pg(a1, q, n):
    approx_sum = 0

    for n in range(1, n+1):
        an = a1*(q**(n-1))
        approx_sum += an

    real_sum = a1/(1 - q)
    abs_error = abs(real_sum - approx_sum)
    return approx_sum, real_sum, abs_error


def print_estudo_pg(a1, q, N):
    for n in N:
        pg = estudo_pg(a1, q, n)
        print(f'O erro absoluto da pg com valor inicial {a1}, razao {q} \
                \n n = {n} é {pg[2]} \n')


a1, q, N = 10, 1/2, [50, 250, 1000]

print_estudo_pg(a1, q, N)
