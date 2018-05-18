import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm


def HPGe(counts, counting_time, plotname='pulseheight.png'):
    '''
    It's a detector
    '''

    geometric_efficiency = 0.5
    peak_stddev = 0.5

    t_bg = 7200  # s - the background counting time

    energy_lo = 0.2522  # keV
    energy_hi = 2264.5107  # keV
    num_channels = 8190

    erg_bins = np.linspace(energy_lo, energy_hi, num_channels)
    erg_mids = erg_bins - ((erg_bins[1] - erg_bins[0]) / 2)
    spectrum = erg_bins * 0

    def hpge_efficiency(e):
        e = np.log(e)
        eff = (-623.969) + (427.823) * e + (-109.149) * e**2 + (12.258) * e**3 + (-0.513) * e**4
        return np.exp(eff)

    # superimpose peaks via never use monte carlo no way
    for reac, count in counts:
        for branching_ratio, erg in reac:
            detected = count * geometric_efficiency * hpge_efficiency(erg) * branching_ratio
            fun = norm(loc=erg, scale=peak_stddev)
            spectrum += fun.pdf(erg_mids) * detected

    # load background info
    bg_data = np.loadtxt('bkg.txt', skiprows=1)
    bg = bg_data[:, 2]
    bg = bg / t_bg  # cps
    bg *= counting_time
    spectrum += bg

    # clean up spectrum
    for i, val in enumerate(spectrum):
        if val < 0.1:
            spectrum[i] = 0

    # plotting
    fig = plt.figure(9)
    ax = fig.add_subplot(111)
    ax.set_yscale('log')
    ax.set_xlabel('Energy keV')
    ax.set_ylabel('Counts')

    ax.plot(erg_bins, spectrum, 'k', linewidth=0.2)

    plt.savefig(plotname, dpi=300)
    plt.close(fig)
    return


if __name__ == '__main__':
    # HPGe([(500, 10000), (600, 10000)], 600)
    pass
