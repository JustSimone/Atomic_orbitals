import numpy as np
def harm(n, theta, phi):
    if n == 0:
        #Y(0,0)
        return 0.5 * np.sqrt(1 / np.pi) * np.ones(theta.shape)
    elif n == 1:
        #Y(1,1)
        return -0.5 * np.sqrt(1.5 / np.pi) * np.cos(phi) * np.sin(theta)
    elif n == 2:
        #Y(2,2)
        return 0.25 * np.sqrt(7.5 / np.pi) * np.cos(2 * phi) * np.sin(theta)**2
    elif n == 20:
        #Y(2,0)
        return np.sqrt(5/(16*np.pi))*(3 * (np.cos(theta))**2 - 1)
    elif n == 30:
        #Y(3,0)
        return 0.25*np.sqrt(7/np.pi)*(5*(np.cos(theta))**3 - 3* np.cos(theta))
    elif n == 21:
        #Y(2,1)
        return -0.5* np.sqrt(15/(2*np.pi)) * np.cos(phi) * np.sin(theta) * np.cos(theta)
