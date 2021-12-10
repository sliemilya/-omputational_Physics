import numpy as np
import matplotlib.pyplot as plt


with np.load ('data_noisy_image.npz') as data:
    A , C = data ['A'], data ['C']

def mat2vec(A):
    h, w = A.shape
    a = np.zeros(h*w, dtype=A.dtype)
    A = np.flipud(A)
    for i, row in enumerate(A):
        a[i*w:i*w+w] = row
    return a

def vec2mat(a, shape):
    h, w = shape
    A = np.zeros(shape, dtype=a.dtype)
    for i in range(h):
        A[i, :]=a[i*w:i*w+w]
    return np.flipud(A)

plt.imshow(A)
plt.show()
Epsilon = []
U, S, V = np.linalg.svd(C)
S_1 = np.zeros((816, 1500))
for i in range(350):
    S_1[i, i] = 1/S[i]
C_inv = V.T @ S_1 @ U.T
X0 = C_inv @ mat2vec(A)
eps = np.linalg.norm(mat2vec(A) - C @ X0)
plt.imshow(vec2mat(X0, (16, 51)))
plt.show()
