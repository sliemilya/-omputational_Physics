import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lin

def kroneker(i,j):
    if i == j:
        return 1
    else:
        return 0
I = np.eye(32)
A = np.zeros((32, 32))
for i in range(32):
    for j in range(32):
        A[i, j] = -kroneker(i, j) + kroneker(i, j - 1) + kroneker(i, j - 2)
spect = np.linalg.eigvals(A)
y = []
for t in range(51):
    y.append(np.linalg.norm(lin.expm(A * t)))
a = np.linalg.norm(lin.expm(A))
plt.plot(range(51), y)
plt.show()
v, s, u = np.linalg.svd(5*I - A)
minsingular = min(s)
epsilon = 10**(-1)
points_x1, points_x2, points_x3, points_x4, points_x5 = [], [], [], [], []
points_y1, points_y2, points_y3, points_y4, points_y5 = [], [], [], [], []
t = 100
for x in range(-230, 100, 1):
    for y in range(-180, 180, 1):
        z = x / t + (y / t)* 1j
        v, s, u = np.linalg.svd(z * I - A)
        if s[-1] <= epsilon:
            points_x1.append(x/t)
            points_y1.append(y/t)
        if s[-1] <= epsilon/10:
            points_x2.append(x/t)
            points_y2.append(y/t)
        if s[-1] <= epsilon/100:
            points_x3.append(x/t)
            points_y3.append(y/t)
        if s[-1] <= epsilon/1000:
            points_x4.append(x/t)
            points_y4.append(y/t)
        if s[-1] <= epsilon/10000:
            points_x5.append(x/t)
            points_y5.append(y/t)
plt.plot(points_x1, points_y1, 'o', color='r')
plt.plot(points_x2, points_y2, 'o', color='b')
plt.plot(points_x3, points_y3, 'o', color='g')
plt.plot(points_x4, points_y4, 'o', color='y')
plt.plot(points_x5, points_y5, 'o', color='orange')
plt.show()
