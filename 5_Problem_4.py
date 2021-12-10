import numpy as np
import matplotlib.pyplot as plt


def newton_iteration(f, fder, x0, eps=1e-7, maxiter=100):
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
    x_n = complex(x0)
    for niter in range(1, maxiter):
        x_n1 = x_n - f(x_n) / fder(x_n)
        if np.abs(x_n1 - x_n) < eps:
            break
        x_n = x_n1
    return x_n#, niter

eps = 1e-2
group_1x = []
group_1y = []
group_2x = []
group_2y = []
group_3x = []
group_3y = []
x1 = 1 + 0j
x2 = -0.49999999900165354-0.8660254028724281j
x3 = -0.49999999900165354+0.8660254028724281j
for x in range(-200, 200):
    for y in range(-200, 200):
        if y == 0:
            continue
        t = 100
        x0 = x/t + y*(1j)/t
        root = newton_iteration(lambda x: x**3 - 1, lambda x: 3*x**2, x0, eps)
        if(np.allclose(root, x1, rtol=eps, atol=eps)):
            group_1x.append(x/t)
            group_1y.append(y/t)
        elif (np.allclose(root, x2, rtol=eps, atol=eps)):
            group_2x.append(x/t)
            group_2y.append(y/t)
        elif (np.allclose(root, x3, rtol=eps, atol=eps)):
            group_3x.append(x/t)
            group_3y.append(y/t)
plt.plot(group_1x, group_1y, 'o', color='y', markersize=0.7)
plt.plot(group_2x, group_2y, 'o', color='g', markersize=0.7)
plt.plot(group_3x, group_3y, 'o', color='#7E1E9C', markersize=0.7)
plt.plot([-0.5, -0.5, 1], [-0.866025, 0.866025, 0], 'o', color='r', markersize=10)
plt.show()
