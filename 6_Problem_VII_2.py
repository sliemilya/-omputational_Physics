import autograd.numpy as np
from scipy.optimize import least_squares
from autograd import grad


def gradient_descent(a0, gamma, A, y, maxiter=1000, eps=1e-4):
    a = a0
    for i in range(1,maxiter):
        a = a0 - gamma * grad_diff_approx(a0, A, y,eps)
        if np.allclose(a, a0, rtol=1e-5):
            break
        a0 = a
    return a


def grad_diff_approx(a,x,y,h):
    #Bычисляем градиент методом разностных приближений
    gradient = np.zeros(11)
    for i in range(len(a)):
        a1, a2 = np.copy(a), np.copy(a)
        a1[i], a2[i] = a[i]+h, a[i]-h
        gradient[i] = (func(a1, A, y)-func(a2, x, y))/(2*h)
    return gradient


def grad_throught_autograd(a, x, y):
    return


def func(a, A, y):
    s = 0
    for i in range(20):
        s += (f(A[i], a)-y[i])**2
    return s
########################################################################################################################


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
########################################################################################################################


with np.load('data_89.npz') as data:
    A, y = data['A2'], data['y2']

a0=np.random.normal(size=11)
h = gradient_descent(a0=a0, gamma=0.1, A=A, y=y)
print("Искомый вектор a:", h)
Min_1 = func(h, A, y)
print("Минимальное значение найденное методом град. спуска: Min_1 =", Min_1)
#############################################################
res = least_squares(minimfun, np.ones(11), args=[A, y])
Min_2 = minimfun(res['x'], A, y)
print("Минимальное значение найденное least_squares: Min_2 =", Min_2)
#############################################################
print("Их различние в процентах:", (abs(Min_2-Min_1)/Min_2) * 100)
print(func(a0, A, y))