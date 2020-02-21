from algorithms import *


if __name__ == '__main__':
    f = lambda x: x - 4 * math.cos(x) * math.cos(x) + 3
    eps = 10 ** (-5)  # требуемая точность вычислений по y

    print('Метод бисекции (деления отрезка пополам):')
    x_bis_1, k_bis_1 = bisection_method(f, -2.2, -1.8, eps)
    print('x1 =', x_bis_1, '\nЧисло итераций:', k_bis_1, '\n')
    x_bis_2, k_bis_2 = bisection_method(f, -0.85, -0.6, eps)
    print('x2 =', x_bis_2, '\nЧисло итераций:', k_bis_2, '\n')
    x_bis_3, k_bis_3 = bisection_method(f, 0, 0.8, eps)
    print('x3 =', x_bis_3, '\nЧисло итераций:', k_bis_3, '\n')

    print('Метод релаксации:')
    x_rel_1, k_rel_1 = relaxation_method(f, -2.2, -1.8, eps)
    print('x1 = ', x_rel_1, '\nЧисло итераций:', k_rel_1, '\n')
    x_rel_2, k_rel_2 = relaxation_method(f, -0.85, -0.6, eps)
    print('x2 = ', x_rel_2, '\nЧисло итераций:', k_rel_2, '\n')
    x_rel_3, k_rel_3 = relaxation_method(f, 0, 0.8, eps)
    print('x3 = ', x_rel_3, '\nЧисло итераций:', k_rel_3)
