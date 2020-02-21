def simpson_method(func, a, b, seg_num, eps):
    """
    Правило Симпсона
    seg_num - число отрезков, на которые разбивается [a;b]
    """
    if seg_num % 2 == 1:
        seg_num += 1

    dx = 1.0 * (b - a) / seg_num
    sum = (func(a) + 4 * func(a + dx) + func(b))
    n = 0

    for i in range(1, int(seg_num / 2)):
        sum += 2 * func(a + (2 * i) * dx) + 4 * func(a + (2 * i + 1) * dx)
        n += 1

    return sum * dx / 3, n


def midpoint_rectangle_rule(func, a, b, nseg):
    dx = 1.0 * (b - a) / nseg
    sum = 0.0
    xstart = a + 0.5 * dx  # 0 <= frac <= 1 задаёт долю смещения точки, в которой вычисляется
                           #  функция, от левого края отрезка dx

    for i in range(nseg):
        sum += func(xstart + i * dx)

    return sum * dx


def trapezoid_method(func, a, b, rtol=1e-8, nseg0=1):
    """
    Правило трапеций
       rtol - желаемая относительная точность вычислений
       nseg0 - начальное число отрезков разбиения
    """
    nseg = nseg0
    old_ans = 0.0
    dx = 1.0 * (b - a) / nseg
    ans = 0.5 * (func(a) + func(b))

    for i in range(1, nseg):
        ans += func(a + i * dx)

    ans *= dx
    err_est = max(1, abs(ans))

    n = 0
    while err_est > abs(rtol * ans):
        old_ans = ans
        ans = 0.5 * (ans + midpoint_rectangle_rule(func, a, b, nseg))  # новые точки для уточнения интеграла
                                                                    # добавляются ровно в середины предыдущих отрезков
        nseg *= 2
        err_est = abs(ans - old_ans)
        n += nseg

    return ans, n
