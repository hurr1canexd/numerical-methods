import math

# ==================== Функции системы ==================== #

def f(x, y):
    return math.sin(x - y) - x * y + 1


def g(x, y):
    return x * x - y * y - 0.75


# ==================== Аналитически вычисленные производные ==================== #

# Частная производная от f по x
def f_dx(x, y):
    return math.cos(x - y) - y


# Частная производная от f по y
def f_dy(x, y):
    return -math.cos(x - y) - x


# Частная производная от g по x
def g_dx(x, y):
    return 2*x


# Частная производная от g по y
def g_dy(x, y):
    return -2*y


# ==================== Численно вычисленные производные ==================== #

def f_dx_num(x, y, h=10**-5):
    return (f(x+h, y) - f(x, y)) / h


def f_dy_num(x, y, h=10**-5):
    return (f(x, y+h) - f(x, y)) / h


def g_dx_num(x, y, h=10**-5):
    return (g(x+h, y) - g(x, y)) / h


def g_dy_num(x, y, h=10**-5):
    return (g(x, y+h) - g(x, y)) / h
