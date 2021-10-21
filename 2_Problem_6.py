import numpy as np
import timeit


def woodbury(A, U, V):
    '''
    Вычисление по формуле с вики
    C: Единичная матрица k на k
    :param A: Матрица n на n
    :param U: Матрица n на k
    :param V: Матрица k на n
    :return: (A + UV)^(-1)
    '''
    C = np.eye(U.shape[1])
    A = np.linalg.inv(A)
    P = A - A @ U @ np.linalg.inv(C + V @ A @ U) @ V @ A
    return P


def woodbury_dir(A, U, V):
    '''
    вычисляет напрямую
    '''
    return np.linalg.inv(A + U @ V)


p = 5000
k = 100
A = np.diag(np.random.random(p))
U = np.random.random((p, k))
V = np.random.random((k, p))

print('Время выполнения вычислений по формуле Вудбери:')
t1 = timeit.default_timer()
woodbury(A, U, V)
print(timeit.default_timer() - t1)

print('Время выполнения вычислений по прямой формуле:')
t2 = timeit.default_timer()
woodbury_dir(A, U, V)
print(timeit.default_timer() - t2)
