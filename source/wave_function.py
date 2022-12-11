import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from matplotlib.widgets import Slider, Button
import spherical_harmonics as sh
from mpl_toolkits.mplot3d import Axes3D
from lib import features, harm


class Wave_function:
    def __init__(self, n, l, ml, r, theta, phi):
        self.Y = sh.Angular(l, ml, theta, phi)
        self.X = sh.Radial(n, l, r)
        self.ml = int(ml)
        self.l = int(l)
        self.n = int(n)
        self.theta = theta
        self.phi = phi


    def plot(self, img):
        # Finding radii and colors for the plot
        radii, colors = features(self.Y)
        i = 0

        X = self.X.values()

        fig = plt.figure(figsize=plt.figaspect(1.))
        fig.subplots_adjust(left=0.25, bottom=0.25)
        ax = fig.add_subplot(111, projection='3d')

        x =  X[i] * radii * np.sin(self.theta) * np.cos(self.phi)
        y =  X[i] * radii * np.sin(self.theta) * np.sin(self.phi)
        z =  X[i] * radii * np.cos(self.theta)

        # Plotting
        ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.coolwarm(colors))
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        '''
        ax.set_xlim(-0.001,0.001)
        ax.set_ylim(-0.001,0.001)
        ax.set_zlim(-0.001,0.001)
        '''
        
        axi = fig.add_axes([0.25, 0.1, 0.65, 0.03])
        i_slider = Slider(
            ax=axi,
            label="Amplitude",
            valmin=0,
            valmax=100,
            valinit=i,
            valstep = 1
        )

        def update(val):
            i_ = int(i_slider.val)
            x =  X[i_] * radii * np.sin(self.theta) * np.cos(self.phi)
            y =  X[i_] * radii * np.sin(self.theta) * np.sin(self.phi)
            z =  X[i_] * radii * np.cos(self.theta)
            ax.plot_surface(x, y, z,  rstride=1, cstride=1, facecolors=cm.coolwarm(colors))

        i_slider.on_changed(update)

        plt.show()
        if img == 1:
            pic_name = "../img/Y"+str(self.l)+"_"+str(self.ml)+".pdf"
            fig.savefig(pic_name)
