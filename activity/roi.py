import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import quad
from scipy.optimize import fsolve

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







def roi(sigma, phi, cd):
    region = sigma['region']
    xs = sigma['func']
    
    # find where zero
    #e = np.geomspace(region[0], region[1], 1000)
    #xss = xs(e)
    #fw_xs = (xs(e) * phi(e) * cd(e)) / total_phi
    
    '''
    plt.xlabel('Energy $MeV$')
    plt.ylabel('Reaction Rate (Arbitrary Units)')
    plt.plot(e, xss)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(*region)
    '''

    # calc 5 95
    # find total rr
    def reaction_rate(e, phi, sigma, cd_fun):
        return (sigma(e) * 1E-24) * phi(e) * cd_fun(e)

    def fold(l, r):
        total_phi = 0
        R = 0
        e = np.geomspace(l, r, 1000)
        for i in range(len(e) - 1):
            total_phi += quad(phi, e[i], e[i+1])[0]
            R += quad(reaction_rate, e[i], e[i+1], args=(phi, xs, cd))[0]
        R = R / total_phi
        return R
    
    R_tot = fold(region[0], region[1])
    R95 = R_tot * 0.95
    
    def fold_l(l, r, r95):
        R = fold(l, r)
        return R - r95
    
    def fold_r(r, l, r95):
        R = fold(r, l)
        return R - r95

    left = fsolve(fold_l, region[0] * 10, args=(region[1], R95))[0]
    right = fsolve(fold_r, region[1] * 1e-2, args=(region[0], R95))[0]
    
    print(fold(left, region[1]) / R_tot)
    print(fold(region[0], right) / R_tot)
    print(region[0], region[1])
    return left, right


# do it
xs = foils['Au']['reactions']['n,gamma']
left, right = roi(xs, phi, cd)
print(left, right)
