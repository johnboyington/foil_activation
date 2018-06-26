from numpy import log, exp
import numpy as np
import matplotlib.pyplot as plt


def hpge_efficiency(erg):
    a = -143.191
    b = 91.147
    c = -21.757
    d = 2.279
    e = -0.089
    return exp(a + b * log(erg) + c * log(erg)**2 + d * log(erg)**3 + e * log(erg)**4)

if __name__ == '__main__':
    e = np.linspace(1, 2000, 4000)
    eff = hpge_efficiency(e)
    plt.plot(e, eff)
