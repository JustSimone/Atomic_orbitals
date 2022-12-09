from scipy.special import sph_harm
import numpy as np
import spherical_harmonics as ph

def flat(Y):
    bool = Y.max().real == Y.min().real
    return bool

def norm(Y):
    return (Y.real * Y.real + Y.imag * Y.imag)*5

def features(Y):
    if flat(Y):
        radii = np.ones(Y.shape())
        colors = np.ones(Y.shape())
        return [radii, colors]
    else:
        radii = np.abs(norm(Y))
        colors = 0.5 *(norm(Y) + 1)
        return [radii, colors]
