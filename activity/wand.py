from activity import activity_calc
from cross_sections import foils
from hpge import HPGe
import numpy as np

###############################################################################
#                     USER DEFINED PARAMETERS
###############################################################################

# aluminum
mat = 'Al'
masses = np.array([0.3, 0.1, 0.2, 0.2])  # mg
t_s = 300  # s
t_i = 600  # s
t_c = 3000  # s
t_f = 6000  # s
P = 100  # kW(th)


counts = activity_calc(foils['Al'], masses[0], P, t_s, t_i, t_c, t_f, plotname=False)
HPGe(counts, t_f - t_c)
'''
for i, m in enumerate(masses):
    counts = activity_calc(foils['Al'], m, P, t_s, t_i, t_c, t_f, plotname='{}{}_activity.png'.format(mat.lower(), i + 1))
    HPGe(counts, t_f - t_c, plotname='{}{}_pulseheight.png'.format(mat.lower(), i + 1))
'''
