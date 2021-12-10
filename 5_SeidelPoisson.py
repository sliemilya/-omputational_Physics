import numpy as np
from scipy.linalg import block_diag
import matplotlib.pyplot as plt
from scipy.linalg import solve_triangular


def seidel_solve(m, b, x0, eps=1e-5, maxiter=500):
    """ Solve `m @ x = b` with Seidel iteration.

    Parameters
    ----------
    m : ndarray, shape (n, n)
       Input matrix
    b : ndarray, shape (n,)
       Right-hand side
    x0 : ndarray, shape (n, )
       Initial point for the iteration
    eps : float, optional
       Target accuracy.
       Stop iterations when the 2-norm of
       `|x_k - x_{k-1}| < eps`
    maxiter : int
       Maximum allowed number of iterations.

    Returns
    -------
    x : ndarray, shape (n,)
       The approximation to the solution of `m @ x = b`
    nit : the number of iterations performed.
    """
    n = np.shape(m)[0]
    x = np.zeros(n)
    for iter in range(1, maxiter):
        x = np.zeros(n)
        for i in range(n):
            sum1 = np.dot(m[i, :i], x[:i])
            sum2 = np.dot(m[i, i + 1:], x0[i + 1:])
            x[i] = (b[i] - sum1 - sum2) / m[i, i]
        if np.allclose(x0, x, atol=eps / n, rtol=eps):
            break
        x0 = x
    return x, iter
    raise NotImplementedError()

def lhs_matrix(n):
    # Диагональный блок
    a = np.zeros((n-1, n-1))

    idx = np.arange(n-1)

    a[idx, idx] = -4
    a[idx[:-1], idx[:-1]+1] = 1
    a[idx[1:], idx[1:]-1] = 1

    # собираем блочно-диагональную матрицу `m`
    m = block_diag(*(a,)*n)

    # заполняем "крылья"
    idx = np.arange(m.shape[0])

    m[idx[:-n+1], idx[:-n+1] + n-1] = 1
    m[idx[n-1:], idx[n-1:] - n+1] = 1
    return m

m = lhs_matrix(5)

#with np.printoptions(linewidth=99):
#    print(m)

#plt.matshow(m)
#plt.show()
b = np.zeros(m.shape[0])
b[m.shape[0]//2] = -1
eps = 1e-5
xx = []
yy = []
for i in range(40):
    x0 = np.ones(m.shape[0])
    x, nit = seidel_solve(m, b, x0, eps)
    eps = eps/2
    xx.append(nit)
    yy.append(eps)
print(list(zip(xx, yy)))
plt.plot(yy, xx, 'o-')
plt.show()
