from matplotlib import rc, rcParams
import matplotlib.pyplot as plt
import numpy as np


def plot_activities(name, reaction_list, t, activities, total_activity, t_s, t_i, t_ci, t_cf, bars=True):
    rc('font', **{'family': 'serif'})
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['xtick.labelsize'] = 18
    rcParams['ytick.labelsize'] = 18
    rcParams['lines.linewidth'] = 1.85
    rcParams['axes.labelsize'] = 20
    rcParams.update({'figure.autolayout': True})

    fig = plt.figure(0)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Activity ($\mu$Ci)')
    ax.set_yscale('log')
    ax.set_ylim(1E-5, 1E3)

    if bars:
        # vertical calculate bars
        v1_x = [t_s, t_s]
        v1_y = [0, np.max(activities) * 1.3]
        v2_x = [t_i, t_i]
        v2_y = [0, np.max(activities) * 1.3]
        v3_x = [t_ci, t_ci]
        v3_y = [0, np.max(activities) * 1.3]
        v4_x = [t_cf, t_cf]
        v4_y = [0, np.max(activities) * 1.3]
        ax.plot(v1_x, v1_y, 'k')
        ax.plot(v2_x, v2_y, 'k')
        ax.plot(v3_x, v3_y, 'k')
        ax.plot(v4_x, v4_y, 'k')
        ax.text(v1_x[1], v1_y[1], '$t_s$')
        ax.text(v2_x[1], v2_y[1], '$t_i$')
        ax.text(v3_x[1], v3_y[1], 'Counting Window')

        # calculate horizontal bars
        h1_x = [0, t[-1]]
        h1_y = [50, 50]

        h2_x = [0, t[-1]]
        h2_y = [2, 2]
        ax.plot(h1_x, h1_y, 'k')
        ax.plot(h2_x, h2_y, 'k')

    # plot total activity
    ax.plot(t, total_activity, 'k', label='Total')

    # plot individual activities
    styles = ['g:', 'b-.', 'r--', 'm:', 'c--']
    activities = activities.T
    for i, act in enumerate(activities[1:]):
        ax.plot(t, act, styles[i], label=reaction_list[i]['label'])

    plt.legend()
    plt.savefig(name, dpi=300)
    plt.close(fig)
    return
