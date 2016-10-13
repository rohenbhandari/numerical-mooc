import sympy
import numpy
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify

x = sympy.symbols('x')
f = ((sympy.cos(x)**2) * (sympy.sin(x)**3)) / (4 * (x**5) * sympy.exp(x))
fprime = f.diff(x)
lam_f = lambdify(x, fprime)
print lam_f(2.2)
