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

'''
n = 10
D = np.random.normal(0, 1, (n, n))
u = np.random.normal(0, 1, (n, 1))
U = (u @ u.T)/(u.T @ u)
A = D + U
l = np.linalg.eigvals(A)
mineigvals = sorted(l, key=abs)[0]


def my_abs(a):
#    if type(a) == 'complex':
    return 0
'''
#n = 100
#D = np.random.normal(0, 1, (n, n))
P = np.zeros((n, 1), dtype=float)
P[:, 0] = u
#print(P)
#p = np.random.normal(0, 1, (n, 1))

U = (P @ P.T)/(P.T @ u)
A = D + U
w, v = np.linalg.eig(A)
indmin = np.argmin(list(map(abs, w)))# находим индекс минимального элемента метод1 смотреть число по модулю
print('Минимальное собственное значение: L_min =', w[indmin])
print('Соответсвующий ему собственный вектор:V =', v[:, indmin])
'''
n = 10**2
D = np.random.normal(0, 1, (n, n))
u = np.random.normal(0, 1, (n, 1))
A = D + (u @ u.T)/(u.T @ u)
x = np.linalg.eigvals(A)
y = np.linalg.eigvals(D)
q = np.zeros((n, n), dtype=complex)
print(len(y), len(x))
for i in range(n):
    for k in range(n):
        q[k, i] = np.divide(u[k, 0], y[k] - x[i])
'''