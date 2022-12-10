import spherical_harmonics as sh
import numpy as np


class Wave_function:
    def __init__(self, n, l, ml, r, theta, phi):
        self.Y = sh.Angular(l, ml, theta, phi)
        self.X = sh.Radial(n, l, r)
        self.psi = np.dot(self.X.values, self.Y.values)
    def plot(self, print):
        # Finding radii and colors for the plot
        radius, colors = features(self.Y)
        radii = np.dot(radius, self.X.values)
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
