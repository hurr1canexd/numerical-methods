#  Приближенное вычисление корней системы нелинейных уравнений методом Ньютона

from newton_method import *


if __name__ == '__main__':
    eps = 10 ** (-5)  # точность вычислений

    print('Численно')
    x1, y1 = newton_method(f, g, -1, 0, eps)
    print(f'x1 = {x1}, y1 = {y1}\n')

    print('Аналитически')
    x1_num, y1_num = newton_method(f, g, -1, 0, eps, 'numerically')
    print(f'x1 = {x1_num}, y1 = {y1_num}\n')

    print('Численно')
    x2, y2 = newton_method(f, g, 1, 2, eps)
    print(f'x2 = {x2}, y2 = {y2}\n')

    print('Аналитически')
    x2_num, y2_num = newton_method(f, g, 1, 2, eps, 'numerically')
    print(f'x2 = {x2_num}, y2 = {y2_num}')
