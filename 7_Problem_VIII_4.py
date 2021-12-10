import numpy as np
import matplotlib.pyplot as plt


def euler_method_solution(y, start, finish, step=0.01):
    solve = []
    for i in range(1, int((finish - start) / step)):
        y = y * 0.5 + np.sqrt(4 * step + y ** 2) * 0.5  # y(k+1) = y(k) + 1/y(k+1)
        solve.append((y, i * step))
    return solve

plt.figure() #Методом Эйлера
points = np.transpose(euler_method_solution(1, 0, 5))
x, y = points[1], points[0]
plt.plot(x, y)
##########################################################
#plt.figure() #Точное решение
x_exact = np.arange(0, 5, 0.01)
y_exact = (2*x_exact + 1)**0.5
plt.plot(x_exact, y_exact)
plt.show()
