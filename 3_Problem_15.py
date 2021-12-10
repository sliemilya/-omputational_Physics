import copy
import numpy as np

C = np.array([[1, 0.9, 0.7], [0.9, 1, 0.4], [0.7, 0.4, 1]])
C_0 = copy.deepcopy(C)
C_0[1][2], C_0[2][1] = 0.3, 0.3

l, s = np.linalg.eig(C_0)
for i in range(len(l)):
    if l[i] < 0:
        l[i] = 0
print(s)
for i in range(len(l)):
    s[i] = s[i] * l[i]
s = s.T
print(s)
s1 = copy.deepcopy(s)
for i in range(len(l)):
    for j in range(len(l)):
        s1[i][j] = s1[i][j]/np.linalg.norm(s[i])
C_1 = s1 @ s1.T
#print(s1)
#print(s1.T)
#print(C_1)
#print(C_0)
