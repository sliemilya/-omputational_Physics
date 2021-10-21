import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools

def dist(p, c, n):
    return (np.dot(p - c, n))**2


with np.load('data_distance_svd.npz') as data:
    xp, yp, zp = data['xp'], data['yp'], data['zp']

points = []                    #запаковываем точки в список
for i in range(len(xp)):
    point = [xp[i], yp[i], zp[i]]
    points.append(point)

#print(max())

########################################################################################################################
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x0 = np.sort(xp)[int(len(np.sort(xp))*0.5)]
y0 = np.sort(xp)[int(len(np.sort(yp))*0.5)]
z0 = np.sort(xp)[int(len(np.sort(zp))*0.5)]
c = np.array([x0, y0, z0])
ax.scatter(xp, yp, zp)
ax.scatter(x0, y0, z0, 'red')
########################################################################################################################
a = itertools.combinations(points, 3)
N = []
for i in a:
    M1 = np.array([[i[0][0], i[0][1], i[0][2]], [i[1][0], i[1][1], i[1][2]], [i[2][0], i[2][1], i[2][2]]])  # Матрица (левая часть системы)
    v1 = np.array([-1, -1, -1]) # Вектор (правая часть системы)
    n = np.linalg.solve(M1, v1)
    k = n[0]**2 + n[1]**2 + n[2]**2
    n = [n[0]/k, n[1]/k, n[2]/k]
    N.append(n)
distance = []
for i in N:
    for j in points:
        distance.append((dist(j, c, i), j, i))
distance.sort()
pisa = distance[0]


x = np.linspace(0,10,100)
y = np.linspace(0,10,100)

X,Y = np.meshgrid(x,y)
n0 = np.sqrt(pisa[2][0]**2 + pisa[2][1]**2 + pisa[2][2]**2)
n1 = pisa[2][0]/n0
n2 = pisa[2][1]/n0
n3 = pisa[2][2]/n0
Z=-(n1/n3)*X - (n2/n3)*Y + (n1/n3)*x0 + (n2/n3) * y0 + z0
fig1 = plt.figure()
ax1 = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z)\

plt.show()
