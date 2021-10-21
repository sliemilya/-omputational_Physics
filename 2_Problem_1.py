import numpy as np


def diy_lu(a):
    """
    Создает LU - разложение матрицы `a`.

    Наивное LU - разложение: работает столбец за столбцом, накапливает элементарные треугольные матрицы.
    Без выбора главного элемента.
    """
    N = a.shape[0]

    u = a.copy()
    L = np.eye(N)
    for j in range(N - 1):
        lam = np.eye(N)
        gamma = u[j + 1:, j] / u[j, j]
        print(gamma)
        lam[j + 1:, j] = -gamma
        u = lam @ u

        lam[j + 1:, j] = gamma
        L = L @ lam
    return L, u


def isDetNotZero(a):
    '''
     Функция проверяет что ведущие миноры не нулевые. Возвращает True если это так, в противном случае False
    '''
    l = a.shape[0]
    for i in range(1, l + 1):
        if np.linalg.det(a[0:i, 0:i]) == 0:
            return False
    return True


def diy_plu(a):
    '''
    делает PLU разложение
    L - верхнетреугольная матрица
    U-нижнетреугольная матрица
    P - обратная матрица перестановок определяется так: P**(-1)A = LU Тогда А = PLU
    '''
    N = a.shape[0]
    u = a.copy()
    L = np.zeros((N, N))
    p = np.eye(N)
    for j in range(N - 1):
        maxind = np.argmax(abs(u[j:, j]))  # Находим индекс максимального элемента в j столбце начиная с j элемента
        if maxind != 0:
            p1 = np.eye(N)
            p1[[j, maxind + j]] = p1[[maxind + j, j]]  # меняем строки в матрице перестановок
            #u[[j, maxind + j]] = u[[maxind + j, j]]  # меняем строки в матрице u
            u = p1 @ u
            p = p1 @ p
            L = p1 @ L
        lam = np.eye(N)
        gamma = u[j + 1:, j] / u[j, j]
        lam[j + 1:, j] = -gamma
        u = lam @ u

        L[j + 1:, j] = gamma
        L = L @ lam
    np.fill_diagonal(L, 1)
    return np.linalg.inv(p), L, u


def recMatrix(L, U, P):
    '''
    Восстанливает изначальную матрицу из разложения:
    L - верхнетреугольная матрица
    U-нижнетреугольная матрица
    P - обратная матрица перестановок определяется так: P**(-1)A = LU Тогда А = PLU
    '''
    return P @ L @ U


# Теперь сгенерируем матрицу полного ранга и протестируем наивное разложение.
N = 6
a = np.zeros((N, N), dtype=float)
for i in range(N):
    for j in range(N):
        a[i, j] = 3. / (0.6 * i * j + 1)
print(np.linalg.matrix_rank(a))

# Настройка вывода чисел с плавающей точкой для большей ясности
np.set_printoptions(precision=3)

p, L, u = diy_plu(a)
print("Наивное разложение первой матрицы")
print(a, "\n")
print('Матрица L:')
print(L, "\n")
print('Матрица U:')
print(u, "\n")
print('Если их перемножить получим изнчальную матрицу:')
# Быстрый тест на адекватность: L @ U должна быть равна изначальной матрице с точностью до ошибок округления.
print(L @ u - a, "\n")
print("Восстановим изначальную матрицу из разложения:")
print(recMatrix(L, u, p), "\n")

a1 = a.copy()
a1[1, 1] = 3
########################################################################################################################
# Тест II.1
print('а')
if isDetNotZero(a):
    print('Ведущих нулевых миноров нет')
else:
    print('Есть ведущие нулевыем миноры')
print('а1')
if isDetNotZero(a1):
    print('Ведущих нулевых миноров нет')
else:
    print('Есть ведущие нулевыем миноры')
########################################################################################################################
p, l, u = diy_plu(a1)
print('Разложение PLU второй матрицы ', "\n")
print('Матрица L:')
print(l, "\n")
print('Матрица U:')
print(u, "\n")
print('Матрица P:')
print(p, "\n")
print('Если их перемножить то получим изначальную матрицу')
# Быстрый тест на адекватность: L @ U должна быть равна изначальной матрице с точностью до ошибок округления.
print(p @ l @ u - a1, "\n")
########################################################################################################################
print("Восстановим изначальную матрицу из разложения:")
print(recMatrix(l, u, p))
