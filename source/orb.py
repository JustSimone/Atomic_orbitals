import numpy as np
import spherical_harmonics as sh
import wave_function as wf
import sys

pi = np.pi

p = int(sys.argv[3])
s = int(sys.argv[4])

# From the definition of l we get that l = n-1
def orbit (n, ml):

    # Image REsolution
    N = 50
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
    #A bit slow
    if p == 0:
        Y.plot(s)
    if p == 1:
        psi.plot(s)
    if p == 2:
        psi.plot(s)
        Y.plot(s)


n = int(sys.argv[1])
ml = int(sys.argv[2])
   
orbit(n, ml)
