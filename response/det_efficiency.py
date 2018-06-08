from numpy import log, exp
import numpy as np
import matplotlib.pyplot as plt


def hpge_efficiency(erg):
    a = -623.969
    b = 427.823
    c = -109.149
    d = 12.258
    e = -0.513
    return exp(a + b * log(erg) + c * log(erg)**2 + d * log(erg)**3 + e * log(erg)**4)

if __name__ == '__main__':
    e = np.linspace(1, 2000, 4000)
    eff = hpge_efficiency(e)
    plt.plot(e, eff)
