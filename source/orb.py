import numpy as np
import spherical_harmonics as sh

pi = np.pi

def orbit (l, ml):

    # Image REsolution
    N = 100

    # Creation of the main variables
    theta = np.linspace(0, pi, N)
    phi = np.linspace(0, 2 * pi, N)
    theta, phi = np.meshgrid(theta, phi)

    # Definition of the firsts Legendre Polynomials
    #
    #Using the scipy library for spherical harmonics
    Y = sh.Spherical_harmonics(l, ml, theta, phi)

    #Using spherical harmonics caluculated manually
    #Y = sh.Spherical_harmonics(30, theta, phi)

    #Plot(0) does not print any Image
    #Plot(1) does print images
    Y.plot(0)

orbit(2,1)
