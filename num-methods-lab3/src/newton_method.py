from functions import *


def newton_method(f, g, x, y, eps=10**-5, derivative='analytically'):
    k = 0  # количество итераций

    # Значение производных в точках
    if derivative == 'analytically':  # аналитически
        a = f_dx(x, y)
        b = f_dy(x, y)
        c = g_dx(x, y)
        d = g_dy(x, y)

    elif derivative == 'numerically':  # численно
        a = f_dx_num(x, y)
        b = f_dy_num(x, y)
        c = g_dx_num(x, y)
        d = g_dy_num(x, y)

    else:
        return -1, -1

    # - [F']^{-1} * F
    dx = -(d * f(x, y) - b * g(x, y)) / (a * d - b * c)
    dy = -(a * g(x, y) - c * f(x, y)) / (a * d - b * c)
    # print('dx, dy =', dx, dy)

    # x_{n+1} = x_{n} + dx
    x_next = x + dx
    y_next = y + dy  # вычисление следующего значения y_{n+1}
    k += 1
    # print(k)

    while math.sqrt(f(x_next, y_next)**2 + f(x_next, y_next)**2) > eps and \
            math.sqrt((x_next - x)**2 + (y_next - y)**2) > eps:
        # print(math.sqrt(f(x_next, y_next)**2 + f(x_next, y_next)**2))

        if derivative == 'analytically':  # аналитически
            a = f_dx(x, y)
            b = f_dy(x, y)
            c = g_dx(x, y)
            d = g_dy(x, y)

        if derivative == 'numerically':  # численно
            a = f_dx_num(x, y)
            b = f_dy_num(x, y)
            c = g_dx_num(x, y)
            d = g_dy_num(x, y)

        dx = -(d * f(x_next, y_next) - b * g(x_next, y_next)) / (a * d - b * c)
        dy = -(a * g(x_next, y_next) - c * f(x_next, y_next)) / (a * d - b * c)
        # print('dx, dy =', dx, dy)

        # Сохраняю значения x_n и y_n
        x = x_next
        y = y_next

        # x_{n+1} = x_{n} + dx
        x_next = x + dx
        y_next = y + dy  # вычисление следующего значения y_{n+1}
        k += 1

    print('Число итераций:', k)
    return x_next, y_next
