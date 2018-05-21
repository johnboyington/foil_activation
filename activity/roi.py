import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad

from cross_sections import foils
from flux_spectrum import Flux

###############################################################################
#                               flux
###############################################################################
# flux
flux = Flux(1/0.833)
phi = flux.evaluate

#
total_phi = 0
e = np.logspace(-5, 9, 100)
for i in range(len(e) - 1):
    total_phi += quad(phi, e[i], e[i+1])[0]


fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.set_xlabel('Energy (eV)')
ax.set_ylabel('$\Phi$ $cm^{-2}s{-1}$')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1E-5, 1E9)
ax.set_ylim(1E-12, 1E1)
x = np.logspace(-5, 9, 1000)
y = phi(x)
ax.plot(x, y, 'k')
plt.savefig('plot/flux.png', dpi=300)
plt.close(fig)

###############################################################################
#                               cadmium
###############################################################################


# cadmium factor
cd = lambda e: 1







def roi(sigma, phi):
    region = sigma['region']
    xs = sigma['func']
    
    # find where zero
    e = np.geomspace(region[0], region[1], 1000)
    xss = xs(e)
    fw_xs = (xs(e) * phi(e)) / total_phi
    
    plt.plot(e, fw_xs)
    plt.xscale('log')
    plt.yscale('log')


# do it
xs = foils['Au']['reactions']['n,gamma']
roi(xs, phi)
