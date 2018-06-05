import numpy as np
import matplotlib.pyplot as plt
from spectrum import Spectrum
from nice_plots import Nice_Plots

Nice_Plots()

name = 'in_n,gamma'

# load in data
erg = np.loadtxt('scale56.txt')
vals = np.loadtxt('data/' + name + '.txt')
err = np.loadtxt('data/' + name + '_err.txt')

# manipulate data
vals = vals[1:] / (erg[1:] - erg[:-1])

rf = Spectrum(erg, vals, err[1:])

# plot data
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.set_xscale('log')
ax.set_yscale('log')

ax.plot(rf.stepu_x, rf.stepu_y)
