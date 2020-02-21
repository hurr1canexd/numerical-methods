from algorihms import *
import math


class Integral:
    # Класс будет хранить определения для квадратурных формул
    __sum = 0.0
    __nseg = 1  # число отрезков разбиения
    __ncalls = 0  # считает число вызовов интегрируемой функции


    # Производит обнуление счётчика
    def __clear(func, x0, x1, nseg0, reset_calls=True):
        if reset_calls:
            Integral.__ncalls = 0
        Integral.__nseg = nseg0

        # вычисление суммы для метода трапеций с начальным числом отрезков разбиения nseg0
        Integral.__sum = 0.5 * (func(x0) + func(x1))
        dx = 1.0 * (x1 - x0) / nseg0
        for i in range(1, nseg0):
            Integral.__sum += func(x0 + i * dx)

        Integral.__ncalls += 1 + nseg0
        return Integral.__sum * dx


    def __double_nseg(func, x0, x1):
        """Вдвое измельчает разбиение.
           Возвращает интеграл методом трапеций на новом разбиении"""
        nseg = Integral.__nseg
        dx = (x1 - x0) / nseg
        x = x0 + 0.5 * dx
        i = 0
        AddedSum = 0.0
        for i in range(nseg):
            AddedSum += func(x + i * dx)

        Integral.__sum += AddedSum
        Integral.__nseg *= 2
        Integral.__ncalls += nseg
        return Integral.__sum * 0.5 * dx


    def trapezoid(func, x0, x1, rtol=1e-10, nseg0=1):
        """Интегрирование методом трапеций с заданной точностью.
           rtol - относительная точность,
           nseg0 - число отрезков начального разбиения"""
        ans = Integral.__clear(func, x0, x1, nseg0)
        old_ans = 0.0
        err_est = max(1, abs(ans))
        while err_est > abs(rtol * ans):
            old_ans = ans
            ans = Integral.__double_nseg(func, x0, x1)
            err_est = abs(old_ans - ans)

        print("Число разбиений: " + str(Integral.__nseg))
        return ans


    def simpson(func, x0, x1, rtol=1.0e-10, nseg0=1):
        """Интегрирование методом парабол с заданной точностью.
           rtol - относительная точность,
           nseg0 - число отрезков начального разбиения"""
        old_trapez_sum = Integral.__clear(func, x0, x1, nseg0)
        new_trapez_sum = Integral.__double_nseg(func, x0, x1)
        ans = (4 * new_trapez_sum - old_trapez_sum) / 3
        old_ans = 0.0
        err_est = max(1, abs(ans))

        while (err_est > abs(rtol * ans)):
            old_ans = ans
            old_trapez_sum = new_trapez_sum
            new_trapez_sum = Integral.__double_nseg(func, x0, x1)
            ans = (4 * new_trapez_sum - old_trapez_sum) / 3
            err_est = abs(old_ans - ans)

        print("Разбиений функции: " + str(Integral.__nseg))
        return ans


if __name__ == '__main__':
    func = lambda x: math.sqrt(x)*math.sin(x)
    eps = 0.5 * 10**(-4)

    print("Метод Симпсона:")
    print(round(Integral.simpson(func, 0, 1, eps), 7))
    print("\nМетод трапеций:")
    print(round(Integral.trapezoid(func, 0, 1, eps), 7))

