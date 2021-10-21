import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams

def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './pictures/{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    #plt.close()


fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.grid(True)

# Настройка оси главных делений для оси абсцисс
ax1.tick_params(axis='x', which='major', direction='inout',
                bottom=True, top=False, left=True, right=False,
                color='b', labelcolor='g',
                labelbottom=True, labeltop=False, labelleft=True, labelright=False)
# Настройка оси главных делений для оси ординат
ax1.tick_params(axis='y', which='major', direction='inout',
                bottom=True, top=False, left=True, right=False,
                color='r', labelcolor='pink',
                labelbottom=True, labeltop=False, labelleft=True, labelright=False)
'''
axis : ['x' | 'y' | 'both'] - экземпляр Axis на котором находятся деления; по умолчанию 'both';
reset : [True | False] - если True, то значения всех параметров сбрасываются на значения по умолчанию. По умолчанию равен False;
which : ['major' | 'minor' | 'both'] - определяет принадлежность к типу делений. По умолчанию 'major';
direction : ['in' | 'out' | 'inout'] - определяет направление делений (внутрь, вовне или и снаружи и внутри);
length - длиная деления в точках (points);
width - ширина деления в точках (points);
color - цвет деления. Возможен любой цвет, приемлимый в matplotlib;
pad - расстояние в точках между делением и подписью к нему;
labelsize - размер шрифта подписи деления в виде строки (например, 'large') или числа;
labelcolor - цвет подписи деления. Возможен любой цвет, приемлимый в matplotlib;
colors - изменяет цвет деления и цвет подписи деления на одно значение. Возможен любой цвет, приемлимый в matplotlib;
zorder - zorder деления и подписи деления;
bottom, top, left, right : [bool | 'on' | 'off'] - каждый из параметров контролирует отображение делений на соответствующей оси;
labelbottom, labeltop, labelleft, labelright : [bool | 'on' | 'off'] - каждый из параметров контролирует отображение подписи делений на соответствующей оси.
'''
########################################################################################################################
separ = ' '    #между '' нужно вставить то чем у вас в файле будет разделитель между столбцами
title = 'Graph'
ind = True #Если нужна сетка то ставь True, Если не нужна ставь False
fout = open('data.txt', 'r', encoding='utf8')
#all_x('blue', 0, 11) # Цвет, угол, размер
#all_y('blue', 0, 11)
########################################################################################################################



data = []
for line in fout:
    a = list(map(float, line.split(separ)))
    data.append(a)
data = np.array(data)
plt.title(title)
x = data[0:, 0]        #по x будут значения из первого столбца
y = data[0:, 1]        #по y будут значение из втрого столбца
plt.scatter(x, y)      #строим по точкам
plt.grid(ind)
plt.show()


