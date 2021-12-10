import numpy as np
import matplotlib.pyplot as plt

N = 1000
k = 1
#####################################
#Создание матрицы A, собственными значениями которой будут являться квадраты частот нормальных мод колебаний
B = np.eye(2*N, dtype=float)
A = np.zeros((2*N, 2*N), dtype=float)
A[0, 0] = 2.
A[0, 1] = -1.
A[2*N - 1, 0] = -1
A[0, 2*N - 1] = -1
A[2*N - 1, 2*N - 1] = 2.
A[2*N - 1, 2*N - 2] = -1.
for i in range(1, 2*N - 1):
    A[i, i] = 2.
    A[i, i + 1] = -1.
    A[i, i - 1] = -1.
K = np.copy(A)
M = np.eye(2*N)
#####################################
for i in range(N):
    j = 2 * i + 1
    A[j, :] = A[j, :] / 2
    M[j, :] = M[j, :] * 2 * k
A = A * (k)
spect, v = np.linalg.eig(A)
spect = np.array(list(map(lambda x: np.real(x), list(spect))))
spect = np.array(list(map(lambda x: (x)**0.5, list(spect))))
plt.hist(spect, density=False, bins=200)
plt.show()
indmin = np.argmin(spect)
indmax = np.argmax(spect)
indmed = np.argsort(spect)[1000]
massiv_y1 = []
massiv_y2 = []
massiv_y3 = []
for i in range(2*N):
    massiv_y1.append(np.real(v[indmin, i]))
    massiv_y2.append(np.real(v[indmax, i]))
    massiv_y3.append(np.real(v[indmed, i]))
plt.plot(np.arange(2*N), massiv_y1, 'o-')
plt.show()
plt.plot(np.arange(2*N), massiv_y2, 'o-')
plt.show()
plt.plot(np.arange(2*N), massiv_y3, 'o-')
plt.show()
