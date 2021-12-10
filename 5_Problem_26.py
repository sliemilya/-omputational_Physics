import numpy as np


def Jac(B, x, g, maxiter=1000, eps=1e-7):
    x0 = x
    q = np.linalg.norm(B)
    eps = eps * (1 - q) / q
    for i in range(maxiter):
        x = B @ x0 + g
        if np.linalg.norm(x - x0) < eps:
            break
        x0 = x
    return x


def matrix_B_D(A):
    d = np.diag(A)
    size = np.shape(A)[0]
    D = np.zeros((size, size))
    D_inv = np.zeros((size, size))
    for j in range(size):
        D_inv[j][j] = 1 / d[j]
        D[j][j] = d[j]
    B = D_inv @ (D - A)
    return B, D, D_inv


rnd = np.random.RandomState(1234)
n = 10
A = rnd.uniform(size=(n, n)) + np.diag([5] * n)
b = rnd.uniform(size=n)
B, D, D_inv = matrix_B_D(A)
g = D_inv @ b
x = Jac(B, np.zeros(n), g)
print('Норма матрицы B:',np.linalg.norm(B), 'Она меньше, а значит сходится')
print('Искомый вектор:',x)
print(np.allclose(A @ x, b, rtol=1e-3, atol=1e-2), 'Так как true значит найденное решение дейсвтельно корень')