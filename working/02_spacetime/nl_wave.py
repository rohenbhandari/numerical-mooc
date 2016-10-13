''' Nonlinear Convection '''
import numpy
import matplotlib.pyplot as plt

nx = 41
dx = 2. / (nx - 1)
nt = 10
dt = 0.02
c = 5
x = numpy.linspace(0, 2, nx)

lbound = numpy.where(x >= 0.5)
ubound = numpy.where(x <= 1)

# Initial conditions
u = numpy.ones(nx)
u[numpy.intersect1d(lbound, ubound)] = 2

#plt.plot(x, u, color = 'g', ls = '--', lw = 3)
#plt.ylim(0, 2.5)
#plt.show()

for n in range(1, nt):
  un = u.copy()
  u[1:] = un[1:] - un[1:] * (dt/dx) * (un[1:] - un[0 : -1])
  u[0] = 1.0

plt.plot(x, u, color = 'b', ls = '--', lw = 3)
plt.ylim(0, 2.5)
plt.show()
