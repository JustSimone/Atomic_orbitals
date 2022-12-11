import numpy as np
from scipy.special import sph_harm, genlaguerre
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
from lib import features, harm

class Angular:
    '''
    def __init__(self, n, theta, phi):
        self.n = n
        self.Y = harm(n, theta, phi)
    '''
    def __init__(self, l, ml, theta, phi):
        if ml*ml <= l*l:
            self.ml = int(ml)
            self.l = int(l)
            self.theta = theta
            self.phi = phi

            self.Y = sph_harm(self.ml, self.l, phi, theta)
        else:
            raise Exeption("|ml|<l")

    def max(self):
        return self.Y.max()
    def min(self):
        return self.Y.min()
    def shape(self):
        return self.Y.shape
    def values(self):
        return self.Y.real

    def norm(self):
        return (self.Y.real * self.Y.real + self.Y.imag * self.Y.imag)*5
    def plot(self, print):
        # Finding radii and colors for the plot
        radii, colors = features(self.Y)

        # Computing the cartesian coordinates
        x = radii * np.sin(self.theta) * np.cos(self.phi)
        y = radii * np.sin(self.theta) * np.sin(self.phi)
        z = radii * np.cos(self.theta)

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
        if print == 1:
            pic_name = "../img/Y"+str(self.l)+"_"+str(self.ml)+".pdf"
            fig.savefig(pic_name)

'''
It is important to notice that the form of the radial function depends on the shape of the potential energy function
therefore this solution may be different from the one of a different system.
The system I decided to study is the hydrogenlike atom, with a coulombian attractive potential.

U(r) = - Zq**2 / r

'''
class Radial:
    def __init__(self, n, l, r):
        # General constant definition (values to be fixed)
        Z = 1
        q = 1
        rB = 1
        Uef = (2*Z)/(rB*n)
        a = np.sqrt(Uef * (np.math.factorial(n-l-1)/(2*n*np.math.factorial(n+l))))
        b = np.power(Uef*r,l)

        # Class elements definition
        self.n = n
        self.l = l
        self.r = r
        self.U = -Z*(q*q)/r
        self.L = genlaguerre((2 * self.l + 1), (self.n - self.l - 1))(Uef*r)
        self.X = a * b * self.L * np.exp(-(Uef*r)/2)

    def values(self):
        return self.X
