import numpy as np

def func(x, A):
    return np.exp(-x.T @ A @ x) / (1 + np.linalg.norm(x))


with np.load('data_89.npz') as data:
    A = data['A4']

N = 1000000
x = np.random.uniform(-1, 1, (N, 8))
sum = 0
for i in range(N):
    sum += func(x[i], A) / N
print(sum)
