import numpy as np
from scipy.special import sph_harm

class Legendre_Polynomials:

    def __init__(self, n, theta, phi):
        self.n = n
        if n == 0:
            #Y(0,0)
            self.Y = 0.5 * np.sqrt(1 / np.pi) * np.ones(theta.shape)
        elif n == 1:
            #Y(1,1)
            self.Y = -0.5 * np.sqrt(1.5 / np.pi) * np.cos(phi) * np.sin(theta)
        elif n == 2:
            #Y(2,2)
            self.Y = 0.25 * np.sqrt(7.5 / np.pi) * np.cos(2 * phi) * np.sin(theta)**2
        elif n == 20:
            #Y(2,0)
            self.Y = np.sqrt(5/(16*np.pi))*(3 * (np.cos(theta))**2 - 1)
        elif n == 30:
            #Y(3,0)
            self.Y = 0.25*np.sqrt(7/np.pi)*(5*(np.cos(theta))**3 - 3* np.cos(theta))
    '''
    def __init__(self, l, ml, theta, phi):
        self.ml = int(ml)
        self.l = int(l)
        self.Y = sph_harm(ml,l,phi, theta)
    '''
    def abs(self):
        return self.Y.real * self.Y.imag
    def get_max(self):
        return self.Y.max()
    def get_min(self):
        return self.Y.min()
    def shape(self):
        return self.Y.shape

    def flat(self):
        bool = self.Y.real.max() == self.Y.real.min()
        return bool
    def norm(self):
        return 2 * (self.Y - self.Y.min())/(self.Y.max()-self.Y.min()) - 1
