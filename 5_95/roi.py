import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d
from scipy.integrate import quad
from scipy.optimize import fsolve

from flux_spectrum import Flux


def calc_roi(xs_string, lo_guess, hi_guess, plot=False):
    # load in cross section data
    xs_erg, xs_vals = np.loadtxt(xs_string, delimiter=',', skiprows=1, unpack=True)
    sigma = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)

    if plot:
        fig = plt.figure(0)
        ax = fig.add_subplot(111)
        ax.plot(xs_erg[1:-2], xs_vals[1:-2])
        ax.set_xscale('log')
        ax.set_yscale('log')

    # load in spectrum
    phi = Flux()

    def reaction_rate(e):
        return sigma(e) * phi.evaluate(e)

    e_lo = 0.025
    e_hi = 1E9

    total_rr = quad(reaction_rate, e_lo, e_hi)[0]

    def roi_lo(e_lo):
        return quad(reaction_rate, e_lo, e_hi)[0] - (0.95 * total_rr)

    lo = fsolve(roi_lo, lo_guess)
    fifth_percent = quad(reaction_rate, lo, e_hi)[0] / total_rr
    print(fifth_percent)

    def roi_hi(e_hi):
        return quad(reaction_rate, e_lo, e_hi)[0] - (0.95 * total_rr)

    hi = fsolve(roi_hi, hi_guess)
    ninety_fifth_percent = quad(reaction_rate, e_lo, hi)[0] / total_rr
    print(ninety_fifth_percent)

    return lo[0], hi[0]


if __name__ == '__main__':
    lo, hi = calc_roi('13-Al-27(n,p)', 1E4, 1E7)
    print('ROI: {:4.2e} eV  to  {:4.2e} eV'.format(lo, hi))
