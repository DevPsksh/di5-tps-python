import numpy as np
import matplotlib.pyplot as mpplt

#
#
print("Showing curve")

DATA = np.random.rand(10, 2)

mpplt.plot(DATA)
mpplt.show()

#
#
print("Showing multiple curves")

DATA = np.random.rand(10, 2)

mpplt.plot(DATA)
mpplt.show()

#
#
print("Showing histogram")

mu, sigma = 100, 15
x = mu + sigma*np.random.randn(10000)

# the histogram of the data
n, bins, patches = mpplt.hist(x, 50, density=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
#y = mlab.normpdf( bins, mu, sigma)
#l = mpplt.plot(bins, y, 'r--', linewidth=1)

mpplt.xlabel('Smarts')
mpplt.ylabel('Probability')
mpplt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
mpplt.axis([40, 160, 0, 0.03])
mpplt.grid(True)

mpplt.show()

#
#
print("Showing camembert")

labels = 'Allemagne', 'France', 'Belgique', 'Espagne'
sizes = [15, 80, 45, 40]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

mpplt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)

mpplt.axis('equal')

mpplt.savefig('PieChart01.png')
mpplt.show()

#
#
print("Showing mesh")

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

fig = mpplt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

mpplt.show()
