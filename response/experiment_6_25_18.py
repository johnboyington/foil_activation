from numpy import log, exp
import numpy as np
import scipy.signal as signal
from det_efficiency import hpge_efficiency

tka_path = 'data/6_25_18/'


def single_foil(mat, node, pk_data, t_w, mass):
    nodal_response = []
    # load data
    name = tka_path + mat + str(node) + '.TKA'
    data = np.loadtxt(name, delimiter=',', skiprows=1)
    erg = np.arange(-0.253, len(data)*.273, 0.273)
    counts = data

    # locate peak indices
    peak_indices = signal.find_peaks_cwt(counts, np.arange(1, 150), min_length=100, noise_perc=50)

    # store data on peaks
    peak_data = []
    for i in peak_indices:
        peak_data.append((erg[i], np.sum(counts[i-20:i+20])))

    for pk_erg, t_half, br_ratio in pk_data:
        loc = 0
        closest = 2000
        for i, peak in enumerate(peak_data):
            if abs(pk_erg - peak[0]) < closest:
                closest = abs(pk_erg - peak[0])
                loc = i
        r = peak_data[loc][1]
        r *= (1 / hpge_efficiency(pk_erg))
        r *= exp((log(2)/t_half) * t_w)
        r *= (1 / br_ratio)
        r *= (1 / mass)
        nodal_response.append(r)
    return nodal_response


def single_node(materials, node, wait_times, masses):
    # energies of interest, halflife, branching ratio
    peak_data = {}
    peak_data['in'] = ((1293, 54*60, 0.8), (335, 4.36*3600, 0.5))  # keV, s
    # peak_data['incd'] = ((1293, 54*60, 0.8), (335, 4.36*3600, 0.5))  # keV, s
    # peak_data['au'] = ((412, 2.7*3600*24, 0.95), (356, 6.18*3600*24, 0.94))  # keV, s
    peak_data['aucd'] = [(412, 2.7*3600*24, 0.95)]  # keV, s
    # peak_data['rh'] = ((51, 4.4*60, 0.47), (40, 46.12*60, 0.004))  # keV, s
    # peak_data['al'] = ((1780, 2.246*60, 1.0), (1369, 15.03*3600, 1.0), (840, 9.458*60, 0.7))  # keV, s

    single_node_response = []
    for foil, t, m in zip(materials, wait_times, masses):
        single_node_response += single_foil(foil, node, peak_data[foil], t, m)
    return np.array(single_node_response)


def store_all_response_vectors():
    masses = np.array([[1.3, 1.5, 1.5, 1.8], [1.5, 0.7, 1.6, 1.8], [0.6, 0.6, 0.3, 0.4], [0.4, 0.6, 0.5, 0.8]])
    masses *= 1e-3  # convert mg to g
    for i in range(4):
        r = single_node(['in', 'aucd'], i+1, [3600, 3600], masses[i])
        np.savetxt('response_vectors/experiment_6_25_18_node_{}.txt'.format(i+1), r)

if __name__ == '__main__':
    store_all_response_vectors()
