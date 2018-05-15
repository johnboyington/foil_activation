from scipy.interpolate import interp1d
import numpy as np


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt(xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    return f

al_np = extract('13-Al-27(n,p)')
al_na = extract('13-Al-27(n,&alpha;)')
al_ng = extract('13-Al-27(n,&gamma;)')
