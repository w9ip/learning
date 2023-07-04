import numpy as np
from scipy.optimize import curve_fit

def linear_model(v, a, b):
    return a*v*b + b*v

# Экспериментальные данные
xs = [100, 1000, 10000]
ys = [0.063, 0.565, 5.946]

# Первое возвращаемое значение - массив из двух коэффициентов
(a, b), _ = curve_fit(linear_model, xs, ys)
print(f'linear = {a}*N + {b}')

def log2N(N):
    