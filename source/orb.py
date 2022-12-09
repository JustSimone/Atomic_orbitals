import numpy as np
import Legendre_Polynomials as lp
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D

pi = np.pi

def features(Y):
    if Y.flat():
        radii = np.ones(Y.shape())
        colors = np.ones(Y.shape())
        return [radii, colors]
    else:
        radii = np.abs(Y.norm())
        colors = 0.5 *(Y.norm() + 1)
        return [radii, colors]


def orbit (l, ml):

    # Image REsolution
    N = 100

    # Creation of the main variables
    theta = np.linspace(0, pi, N)
    phi = np.linspace(0, 2 * pi, N)
    theta, phi = np.meshgrid(theta, phi)

    # Definition of the firsts Legendre Polynomials
    #Y = lp.Legendre_Polynomials(l, ml, theta, phi)
    Y = lp.Legendre_Polynomials(30, theta, phi)

    # Finding radii and colors for the plot
    radii, colors = features(Y)

    # Computing the cartesian coordinates
    x = radii * np.sin(theta) * np.cos(phi)
    y = radii * np.sin(theta) * np.sin(phi)
    z = radii * np.cos(theta)

    # Plotting
    fig = plt.figure(figsize=plt.figaspect(1.))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.coolwarm(colors))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.set_zlim(-1,1)
    plt.show()

orbit(3,1)
