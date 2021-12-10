import numpy as np
import matplotlib.pyplot as plt
#1)Уравение вида: 1+cos(x) = 0
maxiter = 1000
eps = 1e-5
x0 = 1
axis_x = []
axis_y = []
for iter in range(maxiter):
    x1 = x0 + (np.cos(x0) + 1)/np.sin(x0)
    if abs(x1 - x0) < eps:
        break
    axis_x.append(abs(x0 - np.pi))
    axis_y.append(abs(x1 - np.pi))
    x0 = x1
#axis_x = list(map(lambda x: x**2, axis_x))
plt.plot(axis_x[1:], axis_y[1:], 'o-')
plt.show()
print(x1, iter)
########################################################################################################################
#2)Уравениние вида: x**2 - 2 = 0
maxiter = 1000
eps = 1e-9
x0 = 1
axis_x = []
axis_y = []
for iter in range(maxiter):
    x1 = 0.5*(x0+2/x0)
    if abs(x1 - x0) < eps:
        break
    axis_x.append(abs(x0 - np.sqrt(2)))
    axis_y.append(abs(x1 - np.sqrt(2)))
    x0 = x1
axis_x = list(map(lambda x: x**2, axis_x)) #Покажем что зависимость будет квадратичная для это возведем все числа по оси x в квадрат
plt.plot(axis_x[0:], axis_y[0:], 'o-')
plt.show()
print(x1, iter)
