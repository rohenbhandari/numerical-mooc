import numpy
import sympy
import matplotlib.pyplot as plt
from sympy import init_printing

x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x - 4.*t)**2. / (4. * nu * (t + 1.))) + sympy.exp(-(x - 4.*t - 2. * numpy.pi)**2. / (4. * nu * (t + 1.)))

phiprime = phi.diff(x)

from sympy.utilities.lambdify import lambdify
u = -2.*nu*(phiprime / phi) + 4.
u_lamb = lambdify((t, x, nu), u)

nx = 101.
nt = 100.
dx = 2. * numpy.pi / (nx - 1.)
nu - 0.7
sigma = 0.1
dt = sigma* dx**2. / nu

x = numpy.linspace(0., 2. * numpy.pi, nx)
un = numpy.empty(nx)
t = 0.

u = numpy.asarray([u_lamb(t, x0, nu) for x0 in x])
print u
