import numpy
import sympy
import matplotlib.pyplot as plt
from sympy.utilities.lambdify import lambdify
from matplotlib import animation

vmax = 80 #km/hr
L = 11 #km
rhomax = 250 #cars/km
nx = 51
dt = 0.001 #hours
sigma = 0.5


x = numpy.linspace(0, L, nx)
rho0 = numpy.ones(nx) * 10
rho0[10:20] = 50
print rho0
