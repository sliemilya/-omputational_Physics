import numpy as np
import matplotlib.pyplot as plt

n = 1000
a = np.random.normal(0, 1, (n, n))
A = a + a.T
x = np.linalg.eigvals(A)
plt.hist(x, density=True, bins=100)
plt.show()
