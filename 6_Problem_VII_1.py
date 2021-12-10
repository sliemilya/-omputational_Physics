import numpy as np
from scipy.optimize import least_squares

def f(x, a):
    x1 = np.zeros(np.shape(x)[0]+1, dtype=float)
    x1[0], x1[1:] = 1.0, x
    return 1/(np.exp(np.dot(x1, a)) + 1)

def minimfun(a, *args):
    A = args[0]
    y = args[1]
    s = 0
    for i in range(len(y)):
        s += (f(A[i], a) - y[i])**2
    return s

with np.load('data_89.npz') as data:
    A, y = data['A2'], data['y2']

res = least_squares(minimfun, np.ones(11), args=[A, y])
print('Искомый вектор a:', res['x'])
print('Минимальное значение:', minimfun(res['x'], A, y))