"""
Материалы взяты с сайта https://coderoad.ru/33203645/%D0%9A%D0%B0%D0%BA-%D0%BF%D0%BE%D1%81%D1%82%D1%80%D0%BE%D0%B8%D1%82%D1%8C-%D0%B3%D0%B8%D1%81%D1%82%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D1%83-%D1%81-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5%D0%BC-Matplotlib-%D0%B2-Python-%D1%81%D0%BE-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%BC

"""

import math
import random
import numpy
import matplotlib
import matplotlib.pyplot as plt
import os


def Force(M1, M2, R):                           #Считаем силу
    G = 6.67408 * 10 ** (-11)
    return G * M1 * M2 * R**(-2)


def Porginess(M1, poM1, M2, poM2, R, poR):                        #Считаем погрешность
    poF = Force(M1, M2, R) * math.sqrt((poM1/M1)**2 + (poM2/M2)**2 + 2*(poR/R)**2)
    return poF


def Data(M1, M2, R, poM1, poM2, poR):     #Тупой метод генерить данные
    fout = open('output.txt', 'w', encoding='utf8')                  #p.s. не используется в решении оставлю здесь это не зря писал же
    for i in range(10**5):
        M11 = M1 + random.uniform(-poM1, poM1)
        M22 = M2 + random.uniform(-poM2, poM2)
        R1 = R + random.uniform(-poR, poR)
        F = Force(M11, M22, R1)
        poF = Porginess(M11, poM1, M22, poM2, R1, poR)
        print(M11, M22, R1, F, poF, file=fout)
    fout.close()


def Data1(M1, M2, R, poM1, poM2, poR):   #Нормальный способ генерить данные по норамально распределению
    fout = open('output.txt', 'w', encoding='utf8')
    M11 = numpy.random.normal(M1, poM1, 10**5)
    M22 = numpy.random.normal(M2, poM2, 10**5)
    R1 = numpy.random.normal(R, poR, 10**5)
    for i in range(10**5):                                          #Запаковываем значения в файл
        F = Force(M11[i], M22[i], R1[i])
        poF = Porginess(M11[i], poM1, M22[i], poM2, R1[i], poR)
        print(M11[i], M22[i], R1[i], F, poF, file=fout)
    fout.close()


def optimbins(x, ind):
    if ind == 'd':
        return 1000
    q25, q75 = numpy.percentile(x, [.25, .75])
    bin_width = 2 * (q75 - q25) * len(x) ** (-1 / 3)
    bins = round((max(x) - min(x)) / bin_width)
    return bins


def main(M1, M2, R, poM1, poM2, poR, ind = ''):    #Функция в корой и просходит вся магия)))
    if ind == 'a':
        Data1(M1, M2, R, poM1, poM2, poR)   #В этой функции генерится равномерное распределение
    else:
        Data(M1, M2, R, poM1, poM2, poR)    #Тут просто генерятся значение с учетом погрешности(по тупому)
    #####################################################################################################
    fout = open('output.txt', 'r', encoding='utf8')
    #####################################################################################################
    x = []
    for line in fout:                       #запаковываем в список данные по силе из 4го столбца
        a = list(map(float, line.split()))
        x.append(a[3])
    #####################################       #Расчитываем оптимальное значение bins
    matplotlib.pyplot.hist(x, density=True, bins=optimbins(x, ind))  # Строим гистограмму
    plt.ylabel('Probability')
    plt.xlabel('Force')
    ########################################### Построение огибающей(теоретически)
    sigma = Porginess(M1, poM1, M2, poM2, R, poR)*1.25     #отклонение
    aver = Force(M1, M2, R)                                #среднеее значение силы
    a = numpy.arange(min(x), max(x), 0.00001)              #делаем список по которым строить
    y = (1 / (sigma * numpy.sqrt(2 * numpy.pi))) * numpy.exp(- (((a - aver) ** 2 )/ (2 * sigma ** 2)))
    plt.plot(a, y, color='r')
    ############################################
    plt.show()
    fout.close()
    ##################################################################################################################################33
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.txt') #Удаление файла
    os.remove(path)
    ##################################################################################################################################


var = 'd' ## a ли b
if var == 'a':                              #Условие пункта а
    M1 = 40 * 10**4
    poM1 = 0.05 * 10**4
    M2 = 30 * 10**4
    poM2 = 0.1 * 10**4
    R = 3.2
    poR = 0.01
if var == 'd':                              #Условия пункта d
    M1 = 40 * 10**4
    poM1 = 2 * 10**4
    M2 = 30 * 10**4
    poM2 = 10 * 10**4
    R = 3.2
    poR = 1

main(M1, M2, R, poM1, poM2, poR, 'd')

