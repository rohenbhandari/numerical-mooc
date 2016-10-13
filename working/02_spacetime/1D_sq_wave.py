''' 1D wave equation with square wave initial conditions
u(x,0) = 2; 0 <= x <=1 and 1; everywhere else in (0,2) '''

import numpy
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

nx = 41 # number of spatial grid points
dx = 2. / (nx - 1) # distance between pair of adjacent grid points
nt = 25 # number of time grid points
dt = 0.02
c = 1 # that constant from the equation (wavespeed)
x = numpy.linspace(0, 2, nx) # nx divisions between 0 and 2

#Setting Initial Conditions
u = numpy.ones(nx) # fills array with 1s

lbound = numpy.where(x >= 0.5)
ubound = numpy.where(x <= 1) # u = 2 when 0.5 < x < 1

#print lbound
#print ubound

bounds = numpy.intersect1d(lbound, ubound)
u[bounds] = 2

#print u

# Making Graph
#plt.plot(x, u, color = 'r', ls = '--', lw = 3)
#plt.ylim(0, 2.5)
#plt.show()

# Implementing Finite Difference method

for n in range(1, nt):
  un = u.copy()
  for i in range(1, nx):
    u[i] = un[i] - c * (dt/dx) * (un[i] - un[i - 1])

plt.plot(x, u, color = '#003367', ls = '--', lw = 3)
plt.ylim(0, 2.5)
plt.show()
