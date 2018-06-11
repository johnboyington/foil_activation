import numpy as np
import matplotlib.pyplot as plt
from spectrum import Spectrum
from nice_plots import Nice_Plots

Nice_Plots()

names = ['in_n,gamma', 'in_n,inelastic', 'in_cd_n,gamma', 'in_cd_n,inelastic',
         'au_n,gamma', 'au_n,inelastic', 'au_n,2n',
         'au_cd_n,gamma', 'au_cd_n,inelastic', 'au_cd_n,2n',
         'rh_n,gamma', 'rh_n,inelastic',
         'al_n,gamma', 'al_n,p', 'al_n,alpha']
labels = ['In ($n,\gamma$)', "In ($n,n'$)", 'In ($n,\gamma$) Cd', "In ($n,n'$) Cd",
          'Au ($n,\gamma$)', "Au ($n,n'$)", 'Au ($n,2n$)',
          'Au ($n,\gamma$) Cd', "Au ($n,n'$) Cd", 'Au ($n,2n$) Cd',
          'Rh ($n,\gamma$)', "Rh ($n,n'$)",
          'Al ($n,\gamma$)', "Al ($n,p$)", r'Al ($n,\alpha$)']

# plotting params
colors = ['k', 'purple', 'blue', 'green', 'orange', 'red', 'brown']
colors += colors
colors += colors
linestyles = ['-', '-.', '--', ':']
linestyles += linestyles
linestyles += linestyles


# plot data
fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim(1e-11, 20)
ax.set_ylim(1e-7, 1)

for i, name in enumerate(names):
    # load in data
    erg = np.loadtxt('/home/john/workspace/foil_activation/rf/scale56.txt')
    vals = np.loadtxt('data/' + name + '.txt')
    err = np.loadtxt('data/' + name + '_err.txt')

    # manipulate data
    # vals = vals / (erg[1:] - erg[:-1])

    rf = Spectrum(erg, vals, vals * err)

    ax.plot(rf.stepu_x, rf.stepu_y, color=colors[i], label=labels[i], linestyle=linestyles[i], linewidth=0.4)
    ax.errorbar(rf.midpoints, rf.values, rf.error, color=colors[i], linestyle='none', linewidth=0.4)

ax.legend()
fig.savefig('rf.png', dpi=300)
