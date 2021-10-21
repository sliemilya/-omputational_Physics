import math
import cmath
from numpy import allclose

def solve_quad(b, c):
    """Решает квадратное уравнение, x**2 + bx + c = 0.
    """
    D = b**2 - 4*c
    if D >= 0:
        x1 = (-b + math.sqrt(D)) * 0.5
        x2 = (-b - math.sqrt(D)) * 0.5
    else:
        x1 = (-b + cmath.sqrt(b**2 - 4*c)) * 0.5
        x2 = (-b - cmath.sqrt(b**2 - 4*c)) * 0.5
    if x1 == 0 and x1**2 + b*x1 + c != 0:
        x1 = c / x2
    elif x2 == 0 and x2**2 + b*x2 + c != 0:
        x2 = c / x1
    return (x1, x2)

variants = [{'b': 4.0, 'c': 3.0},
            {'b': 2.0, 'c': 1.0},
            {'b': 0.5, 'c': 4.0},
            {'b': 1e10, 'c': 3.0},
            {'b': -1e10, 'c': 4.0},]

for var in variants:
    x1, x2 = solve_quad(**var)
    print(allclose(x1*x2, var['c']), x1, x2)
