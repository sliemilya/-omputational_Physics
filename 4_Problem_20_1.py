import numpy as np

def matrixA(i, j):
    '''
    :param i: строка матрицы А
    :param j: столбец матрицы А
    :return: элемент матрица А стоящий на i, j позиции
    '''
    global u, D, normk
    if i != j:
        return (u[i] * u[j])/normk
    return D[i] + (u[i]**2)/normk
#####################################
#глобальные переменные!!!!! не трогать
n = 100
u = np.random.normal(0, 1, n)
D = np.random.normal(0, 1, n)
normk = np.dot(u, u)
######################################

P = np.zeros((n, 1), dtype=float)
P[:, 0] = u
U = (P @ P.T)/(P.T @ u)
A = D + U
w, v = np.linalg.eig(A)
indmin = np.argmin(list(map(abs, w)))# находим индекс минимального элемента метод1 смотреть число по модулю
print('Минимальное собственное значение: L_min =', w[indmin])
print('Соответсвующий ему собственный вектор:V =', v[:, indmin])
