import matplotlib.pyplot as plt
import numpy as np

def func_G(X):
    N = len(X)
    G = np.zeros((N, 1), dtype=float)
    dx = 10/N
    for i in range(1, N - 1):
        G[i, 0] = (X[i + 1] - 2*X[i] + X[i - 1])/(dx**2) - np.exp(X[i]) + 1 + np.exp(-3*(dx*i - 5)**2)
    return G[1:-1]

def Jac_G(X):
    N = len(X)
    Jac = np.zeros((N, N))
    dx = 10./N
    for i in range(1, N - 1):
        Jac[i, i - 1] = 1/(dx**2)
        Jac[i, i] = -2/(dx**2) - np.exp(X[i])
        Jac[i, i + 1] = 1/(dx**2)
    return Jac[1:-1, 1:-1]


def newton_system(F, jcb, X0, eps=1e-5, maxiter=100):
    """Нахождение корней $f(x) = 0$ через итерации Ньютона.

    Parameters
    ----------
    F : callable
        Вектор-функция системы, которую мы хотим решить.
    jcb : callable
        Якобиан `f`.
    X0 : array-like of floats, shape (n,)
        Начальное приближение итераций Ньютона.
    eps : float
        Заданная точность.
        Алгоритм прекращает работу когда расстояние между последовательными приближениями меньше `eps`.
        По умолчанию 1e-5.
    maxiter : int
        Максимальное число итераций (по умолчанию 100).
        Алгоритм прекращается, когда число итераций достигает `maxiter`.
        Этот параметр нужен лишь для предотвращения бесконечного зацикливания.

    Returns
    -------
    X : array-like of floats, shape (n,)
        Найденное приближение к корню.
    niter : int
        Количество итераций.
    """
    X_n = np.zeros((len(X0), 1))
    X_n[:, 0] = X0
    for niter in range(maxiter):
        A = np.zeros((len(X0), 1))
        A[1: -1] = np.linalg.inv(jcb(X_n)) @ F(X_n)
        X_n1 = X_n - A
        if np.linalg.norm(X_n1 - X_n) < eps:
            break
        X_n = X_n1
    return X_n, niter

N = 1000
x, i = newton_system(func_G, Jac_G, np.zeros(N))
plt.plot(np.linspace(0, 10, N), x)
plt.show()

