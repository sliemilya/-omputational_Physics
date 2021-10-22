import numpy as np
import matplotlib.pyplot as plt


a = np.zeros((15, 28))
a[2: -2, 1] = 1
a[2, 2:6] = 1
a[2:7, 6] = 1
a[7:-2, 7] = 1
a[7, 2:7] = 1
a[-3, 2:7] = 1
a[2:-2, 10] = 1
a[2:-2, 14] = 1
a[2:-2, 18] = 1
a[-3, 10:19] = 1
######################
#Дописываю :)
a[2, 21:26] = 1
a[7, 21:26] = 1
a[12, 21:26] = 1
a[2:-2, 26] = 1
######################
def approx_matrix(a, Rank):
    '''
    :param a: изначальная матрица для приближения
    :param Rank: нужный ранг матрицы на выходе
    :return:
    '''
    U, S, V = np.linalg.svd(a)
    P = np.zeros((len(S), np.shape(V)[0]))
    for i in range(Rank):
        P[i][i] = S[i]
    B = U @ P @ V
    return B


b = np.linalg.matrix_rank(a) #Ранг матрицы a
print('Ранг Матрицы a =', b)
plt.imshow(approx_matrix(a, 1))
plt.show()