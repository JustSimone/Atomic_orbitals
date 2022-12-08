import numpy as np

class Legendre_Polynomials:
    def __init__(self, n, theta, phi):
        self.n = n
        if n == 1:
            #Y(0,0)
            self.Y = 0.5 * np.sqrt(1 / np.pi) * np.ones(theta.shape)
        elif n == 2:
            #Y(0,0)
            self.Y = -0.5 * np.sqrt(1.5 / np.pi) * np.cos(phi) * np.sin(theta)
        elif n == 3:
            #Y(0,0)
            self.Y = 0.25 * np.sqrt(7.5 / np.pi) * np.cos(2 * phi) * np.sin(theta)**2

    def abs(self):
        return np.abs(self.Y)
    def max(self):
        return self.Y.max()
    def min(self):
        return self.Y.min()
    def shape(self):
        return self.Y.shape

    def flat(self):
        bool = self.Y.max() == self.Y.min()
        return bool
    def norm(self):
        if self.Y.max() != self.Y.min():
            return 2 * (self.Y - self.Y.min())/(self.Y.max()-self.Y.min()) - 1
