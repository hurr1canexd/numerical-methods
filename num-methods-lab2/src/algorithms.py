import math


def bisection_method(f, a, b, eps):
    k = 0  # число итераций (делений на 2)

    while b - a > eps:
        k += 1
        c = (a + b) / 2

        if f(a)*f(c) < 0:
            b = c
        elif f(a)*f(c) > 0:
            a = c
        else:
            ans = c
            return ans, k

    ans = a

    return ans,k


def relaxation_method(f, a, b, eps):
    f_dif = lambda x: 8 * math.sin(x) * math.cos(x) + 1  # f'
    k = 0  # количество итераций
    x_n, t, tau = 0, 0, 0

    t = (a+b)/2

    # Поиск оптимального значения параметра \tau
    if f_dif(a) > 0 and f_dif(b) > 0:
        tau = -2 / abs(f_dif(a) + f_dif(b))
    else:
        tau = 2 / abs(f_dif(a) + f_dif(b))

    #  x_{n+1} = x_n + tau*f(x_n)
    x_n = t
    t = x_n + tau*f(x_n)  # вычисление следующего значения t
    k += 1

    while abs(x_n - t) > eps and abs(f(t)) > eps:
        x_n = t
        t = x_n + tau*f(x_n)
        k += 1

    return t, k
