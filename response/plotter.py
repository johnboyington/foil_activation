import matplotlib.pyplot as plt
import numpy as np
from spectrum import Spectrum
import glob
import scipy.signal as signal

# turns all .csv files in a particular folder into a list
foillist = glob.glob("/home/john/workspace/foil_activation/response/data/6_25_18/in*.TKA")

# foillist = ['data/al1.csv']
# creates a loop to run each .csv independently
for j, foil in enumerate(foillist):
    values = foil

    # allows the script to read the .csv
    data = np.loadtxt(values, unpack=True, delimiter=',', skiprows=1)

    # sets the y variable as the 4th column and x as the second column of the data
    x = np.arange(-0.253, len(data)*.273, 0.273)
    y = data

    # function that locates the peaks of the data
    peak_indices = signal.find_peaks_cwt(y, np.arange(1, 150), min_length=100,
                                         noise_perc=50)
    peak_x = []
    peak_y = []
    for i in peak_indices:
        peak_x.append(x[i])
        peak_y.append([i])

    graph = Spectrum(x, y)

    plt.figure(j)
    plt.plot(graph.stepu_x, graph.stepu_y)
    # plt.plot(peak_x, peak_y, 'ko')
    plt.xlabel('Energy')
    plt.ylabel('Net CR')
    plt.suptitle(foil)
    plt.xlim(330, 360)
    plt.ylim(0, 500)
    # plt.show()

    # sums the area under each peak and relays that with the given energy peak
    '''
    peak_data = []
    for i in peak_indices:
        peak_data.append((x[i], np.sum(y[i-20:i+20])))
    for d in peak_data:
        # print(d)
        pass
    '''
