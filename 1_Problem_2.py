""""
Поделим подинтегральное выражение в столбик получим:
I_n = 1/n - a*I_(n-1)
Посчитаем теперь I_0(a) = ln(1 + a) - ln(a)
Тогда I_(n) = (-I_(n+1) + 1/(n + 1))/a
"""
import math
import numpy
def dirintegral(a, n):    #Прямая рекурсия
    if n == 0:
        return numpy.log(1 + a)
    return -dirintegral(a, n - 1) * a + 1 / n


def revintegral(a, n):    #Обратная рекурсия
    if n == 50:
        return 0
    return (-revintegral(a, n + 1) + 1/(n + 1))/a


print('Прямой Рекурсией I_25(0.1) =', dirintegral(0.1, 25))
print('Обратной Рекурсией I_25(0.1) =',revintegral(0.1, 25))
print('Прямой Рекурсией I_25(10) =', dirintegral(10, 25))
print('Обратной Рекурсией I_25(10) =',revintegral(10, 25))
