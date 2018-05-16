import numpy as np

from scipy.integrate import odeint, quad
from scipy.interpolate import interp1d

from cross_sections import foils
from plotting import plot_activities
from flux_spectrum import Flux


def activity_calc(foil, m, P, t_s, t_i, t_c, t_f, plotname='decay.png'):
    '''
    Stuff.
    '''
    reaction_list = list(foil['reactions'].values())
    num_reactions = len(reaction_list)

    # facts of life
    Na = 6.022E23  # atoms / mol

    # set up N_i
    N_i = np.zeros(num_reactions + 1)
    N_i[0] = (m * 1E-3 * Na) / foil['M']

    # calculate decay constants with halflifes
    half_lives = np.ones(num_reactions + 1)
    for i, reaction in enumerate(reaction_list):
        half_lives[i+1] = reaction['halflife']
    decay_constants = np.log(2) / half_lives
    decay_constants[0] = 0

    # find normalized reaction rates
    # load in spectrum
    phi = Flux(1/0.833)

    def reaction_rate(e, phi, sigma):
        return (sigma(e) * 1E-24) * phi.evaluate(e)

    R = np.zeros(num_reactions + 1)
    R[0] = 1
    total_phi = 0
    e = np.logspace(-5, 9, 100)
    for i in range(len(e) - 1):
        total_phi += quad(phi.evaluate, e[i], e[i+1])[0]
        for j, reaction in enumerate(reaction_list):
            R[j+1] += quad(reaction_rate, e[i], e[i+1], args=(phi, reaction['func']))[0]
    R = R / total_phi
    R[0] = 0

    def decay(N, t, lam, t_s, t_i, R, P, num_reactions):
        '''
        Radioactive decay.
        '''
        phi_i = (1/100) * 4E12 * (1 + 1/0.833) * P  # flux at a certain power

        # flux info
        if t < t_s:
            phi_0 = (phi_i * (t/t_s))
        elif t_s < t and t < t_i:
            phi_0 = phi_i
        else:
            phi_0 = 0

        A = np.diag(-lam)
        A[:, 0] = R * phi_0
        return A.dot(N)

    # solve
    times = np.linspace(0, t_f, 10000)
    N = odeint(decay, N_i, times, args=(decay_constants, t_s, t_i, R, P, num_reactions))
    activities = decay_constants * N

    # counting
    counts = list(np.zeros(num_reactions))  # fix this this is garbage wow
    for i, reaction in enumerate(reaction_list):
        act_fun = interp1d(times, activities[:, i+1], bounds_error=False, fill_value=0)
        counts[i] = (reaction['erg'], quad(act_fun, t_c, t_f)[0])

    # Bq to uCi
    activities *= (1/3.7E10) * 1E6
    total_activity = np.sum(activities, axis=1)

    # plotting
    if plotname:
        plot_activities(plotname, reaction_list, times, activities, total_activity, t_s, t_i, True)

    return counts


if __name__ == '__main__':
    # user defined parameters
    foil = foils['Al']
    m = 0.2  # mg
    t_s = 300  # s
    t_i = 600  # s
    t_c = 3000  # s
    t_f = 3600  # s
    P = 100  # kW(th)
    activity_calc(foil, m, P, t_s, t_i, t_c, t_f)
