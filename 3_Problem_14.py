'''
Так как x_i = U_0i * t + (at**2) / 2, а в нашем случае t = 1, так же f = ma, m = 1, значит f = a, тогда x_i = U_0i + f/2
f = delta(U) / delta(t), у нас все дискретно поэтому delta(t) = 1, значит delta(U) = f


A = [[x_k                          ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
x_k = 1/2 + SUM(from i = 1, to i = k-1) f_i / f_k
'''

import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((2, 10))
for i in range(10):
    A[0, i - 1] += 0.5
    A[1, i - 1] = 1
    for j in range(i):
        A[0, j - 1] += 1

u, s, v = np.linalg.svd(A)
y = np.zeros((10, 1))
a = np.array([[1], [0]])
for i in range(2):
    y[i] = (u[:, i].T @ a)/s[i]
f = v.T @ y
#print(A @ f)
print(f)
#print(A)
r, p = [], []
for i in range(10):
    r.append(f[i])
    p.append(i)
plt.scatter(p, r)
plt.plot(r)
plt.xlabel('Time')
plt.ylabel('Force')
plt.show()
