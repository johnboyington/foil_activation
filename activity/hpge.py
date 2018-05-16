import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from scipy.stats import norm


def HPGe(counts, counting_time, plotname='pulseheight.png'):
    '''
    It's a detector
    '''

    hpge_efficiency = 0.5
    peak_stddev = 0.5

    t_bg = 7200  # s - the background counting time

    energy_lo = 0.2522  # keV
    energy_hi = 2264.5107  # keV
    num_channels = 8190

    erg_bins = np.linspace(energy_lo, energy_hi, num_channels)
    spectrum = erg_bins * 0

    # superimpose peaks via monte carlo
    for erg, count in counts:
        detected = count * 0.5 * hpge_efficiency
        fun = norm(loc=erg, scale=peak_stddev)
        for j in range(int(detected)):
            sample = fun.ppf(rand())
            for i, e in enumerate(erg_bins[:-1]):
                if erg_bins[i] < sample and sample < erg_bins[i+1]:
                    spectrum[i+1] += 1
                    break

    # load background info
    bg_data = np.loadtxt('bkg.txt', skiprows=1)
    bg = bg_data[:, 2]
    bg = bg / t_bg  # cps
    bg *= counting_time
    spectrum += bg

    # plotting
    fig = plt.figure(9)
    ax = fig.add_subplot(111)
    ax.set_yscale('log')
    ax.set_xlabel('Energy keV')
    ax.set_xlabel('Counts')

    ax.plot(erg_bins, spectrum, 'k', linewidth=0.2)

    plt.savefig(plotname, dpi=300)
    plt.close(fig)
    return


if __name__ == '__main__':
    HPGe([(500, 10000), (600, 10000)], 600)
