from activity import activity_calc
from cross_sections import foils
import numpy as np


###############################################################################
#                                gold
###############################################################################
print('\n')
print('Gold')
mat = 'Au'
cd_cov = False
masses = np.array([5.0, 4.35, 4.30, 4.37])  # mg
t_s = 300  # s
t_i = 360  # s
t_w = 3000  # s
counting_time = 300
t_f = 3600  # s
P = 10  # kW(th)


removal_activity = 0
for i, m in enumerate(masses):
    t_ci = t_w + (i * counting_time)
    t_cf = t_w + ((i + 1) * counting_time)
    counts, act_rem = activity_calc(foils[mat], m, P, t_s, t_i, t_ci, t_cf, t_f,
                                    cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
    removal_activity += act_rem
print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))

###############################################################################
#                                indium
###############################################################################
print('\n')
print('Indium')
mat = 'In'
cd_cov = False
masses = np.array([1.7, 1.5, 1.4, 1.6])  # mg
t_s = 300  # s
t_i = 360  # s
t_w = 660  # s
counting_time = 300
t_f = 5000  # s
P = 0.1  # kW(th)

removal_activity = 0
for i, m in enumerate(masses):
    t_ci = t_w + (i * counting_time)
    t_cf = t_w + ((i + 1) * counting_time)
    counts, act_rem = activity_calc(foils[mat], m, P, t_s, t_i, t_ci, t_cf, t_f,
                                    cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
    removal_activity += act_rem
print('Removal Activity:  {:4.2e}  uCi'.format(removal_activity))
'''
###############################################################################
#                               rhodium
###############################################################################
print('\n')
print('Rhodium')
mat = 'Rh'
cd_cov = False
masses = np.array([0.7, 0.55, 0.5, 0.55])  # mg
t_s = 300  # s
t_i = 600  # s
t_c = 6000  # s
t_f = 6600  # s
P = 100  # kW(th)


for i, m in enumerate(masses):
    counts = activity_calc(foils[mat], m, P, t_s, t_i, t_c, t_f,
                           cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))

###############################################################################
#                              aluminum
###############################################################################
print('\n')
print('Aluminum')
mat = 'Al'
cd_cov = False
masses = np.array([0.3, 0.2, 0.1, 0.2])  # mg
t_s = 300  # s
t_i = 3600  # s
t_c = 5000  # s
t_f = 5600  # s
P = 100  # kW(th)


for i, m in enumerate(masses):
    counts = activity_calc(foils[mat], m, P, t_s, t_i, t_c, t_f,
                           cd_cov, plotname='plot/{}{}_activity.png'.format(mat.lower(), i + 1))
'''