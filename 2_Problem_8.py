import numpy as np
import matplotlib.pyplot as plt

file = open('signatureData2.csv', 'r', encoding='utf8')
fig1 = []
fig2 = []
for line in file:
    a = list(map(float, line.split(',')))
    fig1.append([a[0], a[1]])
    fig2.append([a[2], a[3]])

def dist(X1, X2, R, mu):
    n = X1.shape[0]
    l = np.array([1]*n).reshape(-1, 1)
    X = X2 - (X1 @ R - l * mu)
    mod = np.trace(X.T @ X)
    return mod


def plot(X1, X2):
    '''
    Строит
    '''
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for i in X1:
        x1.append(i[0])
        y1.append(i[1])
    for i in X2:
        x2.append(i[0])
        y2.append(i[1])
    plt.scatter(x1, y1)
    plt.scatter(x2, y2)
    plt.show()

#############################################
sx1 = 0
sy1 = 0    # суммирование всех x1 и y1
for i in fig1:
    sx1 += i[0]
    sy1 += i[1]
x1 = np.array([sx1/len(fig1), sy1/len(fig1)])
#############################################
sx2 = 0
sy2 = 0    # суммирование всех x2 и y2
for i in fig2:
    sx2 += i[0]
    sy2 += i[1]
x2 = np.array([sx2/len(fig1), sy2/len(fig1)])
############################################
#создаем матрицы X1 и X2
#X1 = np.empty((len(fig1), 2))
#for i in range(len(fig1)):
#    X1[i][0], X1[i][1] = fig1[i][0], fig1[i][1]
#X2 = np.empty((len(fig2), 2))
X1 = np.array(fig1)
X2 = np.array(fig2)
#for i in range(len(fig1)):
#    X2[i][0], X2[i][1] = fig2[i][0], fig2[i][1]
#центрируем X1, X2
n = X1.shape[0]
l = np.array([1]*n).reshape(-1, 1)
X11 = X1 - l * x1             #Матрицы X1 с чертой из условия
X22 = X2 - l * x2

U, D, V = np.linalg.svd(X11.T @ X22)
R = U @ V
mu = x2 - R.T @ x1

X1_new = X1 @ R             #Поворачиваем

for i in range(len(X1_new)):    #делаем сдвиг
    X1_new[i][0] = X1_new[i][0] + mu[0]
    X1_new[i][1] = X1_new[i][1] + mu[1]


plot(X1_new, X2)

