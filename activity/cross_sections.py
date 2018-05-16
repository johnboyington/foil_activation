from scipy.interpolate import interp1d
import numpy as np


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt(xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    return f


# foils
Al = {}
Al['M'] = 26.9815385  # g/mol
Al['rho'] = 2.7  # g/cm3
Al['reactions'] = {}

Al['reactions']['n,p'] = {}
Al['reactions']['n,p']['func'] = extract('13-Al-27(n,p)')
Al['reactions']['n,p']['halflife'] = 9.458 * 60  # s
Al['reactions']['n,p']['label'] = r'($n,p$)'

Al['reactions']['n,alpha'] = {}
Al['reactions']['n,alpha']['func'] = extract('13-Al-27(n,&alpha;)')
Al['reactions']['n,alpha']['halflife'] = 15.03 * 60 * 60  # s
Al['reactions']['n,alpha']['label'] = r'($n,\alpha$)'

Al['reactions']['n,gamma'] = {}
Al['reactions']['n,gamma']['func'] = extract('13-Al-27(n,&gamma;)')
Al['reactions']['n,gamma']['halflife'] = 2.246 * 60  # s
Al['reactions']['n,gamma']['label'] = r'($n,\gamma$)'

# all foils
foils = {}
foils['Al'] = Al
