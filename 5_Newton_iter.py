import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_allclose

def newton_iteration(f, fder, x0, eps=1e-5, maxiter=100):
    """Нахождение корней $f(x) = 0$ через итерации Ньютона.

    Parameters
    ----------
    f : callable
        Функция, корни которой мы хотим найти.
    fder : callable
        Производная `f`.
    x0 : float
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
    x : float
        Найденное приближение к корню.
    niter : int
        Количество итераций.
    """
    x_n = x0
    for niter in range(maxiter):
        x_n1 = x_n - f(x_n)/fder(x_n)
        if np.abs(x_n1 - x_n) < eps:
            break
        x_n = x_n1
    return x_n, niter


def mod_newton(f, fder, x0, m, eps=1e-5, maxiter=100):
    """Нахождение корней $f(x) = 0$ через итерации Ньютона.

    Parameters
    ----------
    f : callable
        Функция, корни которой мы хотим найти.
    fder : callable
        Производная `f`.
    x0 : float
        Начальное приближение итераций Ньютона.
    eps : float
        Заданная точность.
        Алгоритм прекращает работу когда расстояние между последовательными приближениями меньше `eps`.
        По умолчанию 1e-5.
    maxiter : int
        Максимальное число итераций (по умолчанию 100).
        Алгоритм прекращается, когда число итераций достигает `maxiter`.
        Этот параметр нужен лишь для преcдотвращения бесконечного зацикливания.

    Returns
    -------
    x : float
        Найденное приближение к корню.
    niter : int
        Количество итераций.
    """
    x_n = x0
    for niter in range(maxiter):
        x_n1 = x_n - (m * f(x_n)) / fder(x_n)
        if np.abs(x_n1 - x_n) < eps:
            break
        x_n = x_n1
    return x_n, niter


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
    X_n = X0
    for niter in range(maxiter):
        X_n1 = X_n - np.linalg.inv(jcb(X_n)) @ F(X_n)
        if np.linalg.norm(X_n1 - X_n) < eps:
            break
        X_n = X_n1
    return X_n, niter


def func2(X):
    x, y, z = X
    return np.array([x ** 2 + y ** 2 + z ** 2 - 25,
                     x * y + y * z + z * x - 5,
                     x + y - 3])


def jac2(X):
    """Return the Jacobian of `func2(X)`.


    The Jacobian matrix is defined as

    $$
    J_{ij} = \partial f_i / \partial x_j
    $$

    so that the first row contains the derivatives of $f_0$
    with respect to the first, second etc coordinates; the second
    row contains the derivatives of $f_1$ with respect to
    the first, second etc coordinates; and so on.
    """
    x, y, z = X
    F = func2(X)
    Jac = np.zeros(3)
    for i in range(3):
        for j in range(3):

    raise NotImplementedError()

'''
#xx, nit = newton_iteration(lambda x: x**2 - 1, lambda x: 2.*x, x0=4)
x = []
y = []
for i in range(1, 100):
    xx, nit = newton_iteration(lambda x: x**2 - 1, lambda x: 2.*x, x0=4, eps=1e-15, maxiter=i)
    y.append(np.log(xx-1))
    x.append(nit)
plt.plot(x, y, 'o-')
plt.show()

for m in [1, 2, 3, 4, 5, 6]:
    xx, nit = mod_newton(lambda x: (x**2 - 1)**4,
                         lambda x: 4*(x**2 - 1)**3 * 2 * x,
                         x0=2, m=m, maxiter=10000, eps=1e-9)
    assert_allclose(xx, 1.0, atol=1e-8)
'''

'''
it = []
mel = [1, 2, 3, 4, 5, 6]
for m in [1, 2, 3, 4, 5, 6]:
    xx, iter = mod_newton(lambda x: (x**2 - 1)**2,
               lambda x: 2*(x**2 - 1) * 2 * x,
               x0=2, m=m, maxiter=10000, eps=1e-9)
    it.append(iter)
print(list(zip(it, mel)))
m = 2
x0 = 7
axis_x = []
axis_y = []
x_n1, iter = mod_newton(lambda x: (x**2 - 1)**2, lambda x: 2*(x**2 - 1) * 2 * x, x0=x0, m=m, maxiter=1, eps=1e-9)
for maxiter in range(2, 10):
    x_n, iter = mod_newton(lambda x: (x**2 - 1)**2, lambda x: 2*(x**2 - 1) * 2 * x, x0=x0, m=m, maxiter=maxiter, eps=1e-9)
    axis_y.append(np.abs(x_n-1))
    axis_x.append(np.abs(x_n1 - 1))
    x_n1 = x_n
plt.plot(axis_x, axis_y, 'o-')
p = np.arange(0, 2.5, 0.001)
q = 0.07*p**2+0.18*p-0.007
plt.plot(p, q)
plt.show()
'''