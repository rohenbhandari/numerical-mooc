import numpy
import matplotlib.pyplot as plt

def linearconv(nx):
  """Solve the linear convection equation.
    
    Solves the equation d_t u + c d_x u = 0 where 
    * the wavespeed c is set to 1
    * the domain is x \in [0, 2]
    * 20 timesteps are taken, with \Delta t = 0.025
    * the initial data is the hat function
    
    Produces a plot of the results
    
    Parameters
    ----------
    
    nx : integer
        number of internal grid points
        
    Returns
    -------
    
    None : none
    """
  dx = 2. / (nx - 1)
  nt = 20
  #dt = 0.025
  c = 1
  sigma = 0.5
  dt = sigma * dx

  x = numpy.linspace(0, 2, nx)

  u = numpy.ones(nx)
  lbound = numpy.where(x >= 0.5)
  ubound = numpy.where(x <= 1)
  u[numpy.intersect1d(lbound, ubound)] = 2

  un = numpy.ones(nx)

  for n in range(nt):
    un = u.copy()
    u[1:] = un[1:] - c * (dt/dx) * (un[1:] - un[0 : -1])
    u[0] = 1.

  plt.plot(x, u, color = 'r', ls = '--', lw = 3)
  plt.ylim(0, 2.5)
  plt.show()

linearconv(84)
