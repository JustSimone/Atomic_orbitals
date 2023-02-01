import numpy as np
import spherical_harmonics as sh
import wave_function as wf

pi = np.pi

# From the definition of l we get that l = n-1
def orbit (n, ml):

    # Image REsolution
    N = 100
    l = n-1

    # Creation of the main variables
    theta = np.linspace(0, pi, N)
    phi = np.linspace(0, 2 * pi, N)
    r = np.linspace(0.1, 1, N)
    theta, phi = np.meshgrid(theta, phi)

    psi = wf.Wave_function(n, l, ml, r, theta, phi)
    Y = sh.Angular(l, ml, theta, phi)

    '''
    # Definition of the firsts Legendre Polynomials
    #
    #Using the scipy library for spherical harmonics
    Y = sh.Angular(l, ml, theta, phi)
    X = sh.Radial(n, l, r)
    #Using spherical harmonics caluculated manually
    Y = sh.Spherical_harmonics(30, theta, phi)
    '''

    #Plot(0) does not print any Image
    #Plot(1) does print images
    Y.plot(0)
    psi.plot(0)
orbit(3, 0)
