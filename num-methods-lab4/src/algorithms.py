import numpy as np
from helper_methods import divide_row, combine_rows
from typing import List
from copy import copy


# Метод Гаусса
def gaussian_method(A, f):
    column = 0
    k = 0

    while column < len(f):
        k += 1
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r

        if current_row is None:
            return None

        if current_row != column:
            # меняем местами строки
            A[current_row], A[column] = A[column], A[current_row]
            f[current_row], f[column] = f[column], f[current_row]

        # делим строку на число
        divide_row(A, f, column, A[column][column])

        # прибавляем строку, умноженную на коэффициент
        for r in range(column + 1, len(A)):
            combine_rows(A, f, r, column, -A[r][column])

        column += 1

    X = [0 for _ in f]
    for i in range(len(f) - 1, -1, -1):
        X[i] = f[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))

    return X, k


# Метод быстрого спуска
def method_of_steepest_descent(m, c, eps):
    g: np.array = np.dot(m.transpose(), c)
    B: np.array = np.dot(m.transpose(), m)

    n = 0
    x: List[np.array] = [np.zeros(B.shape[0])]
    r: List = [np.dot(B, x[0]) - g]

    while n == 0 or not (np.sqrt(np.dot(r[-1], r[-1])) < eps and np.sqrt(np.dot(x[-1] - x[-2], x[-1] - x[-2])) < eps):
        tau = np.dot(r[-1], r[-1]) / np.dot(np.dot(B, r[-1]), r[-1])
        x.append(x[-1] - tau * r[-1])
        r.append(np.dot(B, x[-1]) - g)
        n += 1
    return x[-1], n


# Метод сопряжённых градиентов
def conjugate_gradient_method(A, c, eps):
    A = np.array(copy(A))
    g = np.dot(A.transpose(), c)
    A = np.dot(A.transpose(), A)

    x: List[np.array] = [np.zeros(A.shape[0])]
    r: List[np.array] = [g - np.dot(A, x[0])]
    z: List[np.array] = [r[0]]

    n = 0

    while np.sqrt(np.dot(r[-1], r[-1])) / np.sqrt(np.dot(g, g)) > eps or n < 4:
        alpha = np.dot(r[-1], r[-1]) / np.dot(np.dot(A, z[-1]), z[-1])
        x.append(x[-1] + alpha * z[-1])
        r.append(r[-1] - alpha * np.dot(A, z[-1]))
        beta = np.dot(r[-1], r[-1]) / np.dot(r[-2], r[-2])
        z.append(r[-1] + beta * z[-1])
        n += 1

    return x[-1], n
