import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint, quad

from cross_sections import al_np, al_na, al_ng
from flux_spectrum import Flux


def decay(N, t, lam, timebreaks, R, P):
    '''
    Radioactive decay.
    '''
    # load in decay constant information
    lam_1 = lam[1]
    lam_2 = lam[2]
    lam_3 = lam[3]

    phi_i = (4E12 / 100) * P
    t_s = timebreaks[0]
    t_i = timebreaks[1]

    # flux info
    if t < t_s:
        phi = (phi_i * (t/t_s))
    elif t_s < t and t < t_i:
        phi = phi_i
    else:
        phi = 0

    R1 = R[1] * phi
    R2 = R[2] * phi
    R3 = R[3] * phi

    A = np.array([[0, 0, 0, 0],
                 [R1, -lam_1, 0, 0],
                 [R2, 0, -lam_2, 0],
                 [R3, 0, 0, -lam_3]])
    return A.dot(N)


# load in initial isotopic info
m = 0.2  # mg
M = 26.9815385  # g/mol
Na = 6.022E23


n_0 = (m * 1E-3 * Na) / M
n_1 = 0
n_2 = 0
n_3 = 0
N_i = np.array([n_0, n_1, n_2, n_3])

T_1 = 9.458 * 60  # s
l1 = np.log(2) / T_1

T_2 = 15.03 * 60 * 60  # s
l2 = np.log(2) / T_2

T_3 = 2.246 * 60  # s
l3 = np.log(2) / T_3

decay_constants = np.array([0, l1, l2, l3])
time_stops = np.array([300, 600])

# find normalized reaction rates
# load in spectrum
phi = Flux(1/0.833)

e_lo = 1E-5
e_hi = 1E9


def reaction_rate(e, phi, sigma):
    return (sigma(e) * 1E-24) * phi.evaluate(e)


total_phi = 0
total_rr1 = 0
total_rr2 = 0
total_rr3 = 0
e = np.logspace(-5, 9)
for i in range(len(e) - 1):
    total_phi += quad(phi.evaluate, e[i], e[i+1])[0]
    total_rr1 += quad(reaction_rate, e[i], e[i+1], args=(phi, al_np))[0]
    total_rr2 += quad(reaction_rate, e[i], e[i+1], args=(phi, al_na))[0]
    total_rr3 += quad(reaction_rate, e[i], e[i+1], args=(phi, al_ng))[0]
R1 = total_rr1 / total_phi
R2 = total_rr2 / total_phi
R3 = total_rr3 / total_phi

print(R1, R2, R3)
R = np.array([0, R1, R2, R3])

P = 100  # kW(th)
# define times and solve problem
t = np.linspace(0, 3600, 10000)
N = odeint(decay, N_i, t, args=(decay_constants, time_stops, R, P))
activities = decay_constants * N
N = N.T
activities = activities.T

# Bq to uCi
activities *= (1/3.7E10) * 1E6
total_activity = np.sum(activities, axis=0)

fig = plt.figure(0)
ax = fig.add_subplot(111)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Activity ($\mu$Ci)')
ax.set_yscale('log')
ax.plot(t, total_activity, 'k', label='Total')
ax.plot(t, activities[1], 'g:', label=r'($n,p$)')
ax.plot(t, activities[2], 'b-.', label=r'($n,\alpha$)')
ax.plot(t, activities[3], 'r--', label=r'($n,\gamma$)')

# vertical calculate bars
v1_x = [time_stops[0], time_stops[0]]
v1_y = [0, np.max(activities) * 1.1]

v2_x = [time_stops[1], time_stops[1]]
v2_y = [0, np.max(activities) * 1.1]
ax.plot(v1_x, v1_y, 'k')
ax.plot(v2_x, v2_y, 'k')
ax.text(v1_x[1], v1_y[1], '$t_s$')
ax.text(v2_x[1], v2_y[1], '$t_i$')

# calculate horizontal bars
h1_x = [0, t[-1]]
h1_y = [50, 50]

h2_x = [0, t[-1]]
h2_y = [2, 2]
ax.plot(h1_x, h1_y, 'k')
ax.plot(h2_x, h2_y, 'k')
plt.legend()

plt.savefig('decay.png', dpi=300)
