
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal
import seaborn as sns


centerX = 100, centerY = 100
radius = 200
sigma = 20
scaleZ = 100
vmin = -0.5, vmax = 1

# mu = np.array([centerX, centerY])  # define the center of the receptive field
# x, y = np.mgrid[0:radius:200j, 0:radius:200j] # define coordinates of receptive field
# xy = np.column_stack([x.flat, y.flat]) # Need an (N, 2) array of (x, y) pairs.
# sigma = np.array([sigma, sigma])
# covariance = np.diag(sigma**2)
# z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)
# z = scaleZ * z.reshape(x.shape) # Reshape back to a (radius x radius) grid.

# Excitatory Center of Receptive Field
x, y = np.mgrid[0:radius:200j, 0:radius:200j]
z = 1.0 - ((1/100)* (((x - 100)**2 + (y - 100)**2)**0.5))
z = z.clip(min=0)

fig = plt.figure(figsize=[12,5])
ax1 = fig.add_subplot(121)
t1 = ax1.contourf(x, y, z, 20, cmap='RdGy',vmin=-1,vmax=1)
fig.colorbar(t1)

#Inhibitory Surround of Receptive Field
centerX2 = 100, centerY2 = 100
radius2 = 200
x2, y2 = np.mgrid[0:radius2:200j, 0:radius2:200j]
z2 = 0.5 - ((1/300)* (((x - centerX2)**2 + (y - centerY2)**2)**0.5))  # use this for inhibitory connection

ax2 = fig.add_subplot(122)
t2 = ax2.contourf(x2, y2, z2, 20, cmap='RdGy',vmin=-1,vmax=1)
fig.colorbar(t2)

plt.show()


# 3D Plot
# fig = plt.figure(figsize=[12,5])
# ax1 = fig.add_subplot(121, projection='3d')
# ax1.plot_surface(x,y,z)
# ax1.set_zlim(0,1)
# ax2 = fig.add_subplot(122, projection='3d')
# ax2.plot_surface(x2,y2,z2)
# ax2.set_zlim(0,1)
# ax2.set_xlim(0,200)
# ax2.set_ylim(0,200)
# plt.show()