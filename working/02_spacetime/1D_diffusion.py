import numpy
import matplotlib.pyplot as plt

nx = 41
dx = 2.0 / (nx - 1)
nt = 20
nu = 0.3 #value of viscosity
sigma = 0.2
dt = sigma * dx**2 / nu

x = numpy.linspace(0, 2, nx)
ubound = numpy.where(x >= 0.5)
lbound = numpy.where(x <= 1)

u = numpy.ones(nx)
u[numpy.intersect1d(lbound, ubound)] = 2
un = numpy.ones(nx)

for n in range(nt):
  un = u.copy()
  u[1:-1] = un[1:-1] + nu*(dt/dx)**2*(un[2:] - 2 * un[1:-1] + un[0:-2])

#plt.plot(x, u, color = 'r', ls = '--', lw = 3)
#plt.ylim(0, 2.5)
#plt.show()

#Animating the wave
from matplotlib import animation

nt = 50
u = numpy.ones(nx)
u[numpy.intersect1d(lbound, ubound)] = 2
un = numpy.ones(nx)

fig = plt.figure(figsize = (8,5))
ax = plt.axes(xlim = (0, 2), ylim = (1, 2.5))
line = ax.plot([], [], color = 'r', ls = '--', lw = 3)[0]

def diffusion(i):
  line.set_data(x, u)
  un = u.copy()
  u[1:-1] = un[1:-1] + nu * (dt/dx) ** 2 * (un[2:] - 2*un[1:-1] + un[0:-2])

anim = animation.FuncAnimation(fig, diffusion, frames = nt, interval = 1)
plt.show()
