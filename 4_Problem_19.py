import numpy as np
from sympy import var, plot_implicit

A = np.array([[0, 1], [0, 0]])
z = np.linalg.eigvals(A)
print(z)
var('x y')
epsilon = 0.1
plot_implicit((2/(x**2+y**2) + 1/(x**2+y**2)**2)**0.5 >=epsilon**(-1))
epsilon = 0.01
plot_implicit((2/(x**2+y**2) + 1/(x**2+y**2)**2)**0.5 >=epsilon**(-1))
