import numpy as np

n = 3
a = np.random.normal(0, 1, (n, n))
A = a @ a.T

x = np.sort(np.linalg.eigvals(A))

Q, R = np.linalg.qr(A)
B = R @ Q
y = np.sort(np.diag(B))

z = np.divide(x, y)
iter = 1
while np.max(z) > 1.01 or np.min(z) < 0.99:
    Q, R = np.linalg.qr(B)
    B = R @ Q
    print('B', B)
    print('R', R)
    print('Q', Q)
    y = np.diag(B)
    y = np.sort(y)
    z = np.divide(x, y)
    iter += 1

print('Точность в процентах для каждого собвственного числа')
print(list(map(lambda x: ((x[0]-x[1])*100)/x[0], list(zip(x,y)))))
print('Итераций необходимо что бы получить спектр матрицы с точностью 1%:', iter)

