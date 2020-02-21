from algorithms import *
import pandas as pd


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


if __name__ == '__main__':
    # input A, f
    # A*x = f
    # output: x

    eps = 10**(-7)

    A = np.array([
        [1., -0.22, 0.11, -0.31],
        [-0.38, 1., 0.12, -0.22],
        [-0.11, -0.23, 1., 0.51],
        [-0.17, 0.21, -0.31, 1.]
    ])

    f = np.array([2.7, -1.5, 1.2, -0.17])

    x_gauss = gaussian_method(A, f)
    print(f"Метод Гаусса: {x_gauss[0]}")
    print(f"Итераций: {x_gauss[1]}\n")

    epss = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    x1 = []
    x2 = []
    x3 = []
    iters = []

    for eps in epss:
        result = method_of_steepest_descent(A, f, eps)
        x1.append(to_fixed(result[0][0], 7))
        x2.append(to_fixed(result[0][1], 7))
        x3.append(to_fixed(result[0][2], 7))
        iters.append(result[1])

    print('Метод наискорейшего спуска')
    res = pd.DataFrame({
        "Точность": epss,
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "Итераций": iters
    })

    print(res, '\n')

    epss = [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    rounder = [2, 3, 4, 5, 6, 7, 8]
    x1 = []
    x2 = []
    x3 = []
    iters = []

    for eps in epss:
        result = conjugate_gradient_method(A, f, eps)
        x1.append(to_fixed(result[0][0], 7))
        x2.append(to_fixed(result[0][1], 7))
        x3.append(to_fixed(result[0][2], 7))
        iters.append(result[1])

    print('Метод сопряжённых градиентов')
    res = pd.DataFrame({
        "Точность": epss,
        "x1": x1,
        "x2": x2,
        "x3": x3,
        "Итераций": iters
    })

    print(res)
