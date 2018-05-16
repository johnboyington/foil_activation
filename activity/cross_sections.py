from scipy.interpolate import interp1d
import numpy as np


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt(xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    return f


# aluminum
Al = {}
Al['M'] = 26.9815385  # g/mol
Al['rho'] = 2.7  # g/cm3
Al['reactions'] = {}

Al['reactions']['n,p'] = {}
Al['reactions']['n,p']['func'] = extract('13-Al-27(n,p)')
Al['reactions']['n,p']['halflife'] = 9.458 * 60  # s
Al['reactions']['n,p']['label'] = r'($n,p$)'
Al['reactions']['n,p']['erg'] = [(.0086, 170.82), (.718, 843.76), (.282, 1014.52)]  # keV (placeholder)

Al['reactions']['n,alpha'] = {}
Al['reactions']['n,alpha']['func'] = extract('13-Al-27(n,&alpha;)')
Al['reactions']['n,alpha']['halflife'] = 15.03 * 60 * 60  # s
Al['reactions']['n,alpha']['label'] = r'($n,\alpha$)'
Al['reactions']['n,alpha']['erg'] = [(0.00210, 996.6), (99.9936, 1368.626)]  # keV (placeholder) this line is totally wrong - like so wrong

Al['reactions']['n,gamma'] = {}
Al['reactions']['n,gamma']['func'] = extract('13-Al-27(n,&gamma;)')
Al['reactions']['n,gamma']['halflife'] = 2.246 * 60  # s
Al['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Al['reactions']['n,gamma']['erg'] = [(1, 1778.987)]  # keV (placeholder)


# rhodium
Rh = {}
Rh['M'] = 102.90550  # g/mol
Rh['rho'] = 12.41  # g/cm3
Rh['reactions'] = {}

Rh['reactions']['n,inelastic'] = {}
Rh['reactions']['n,inelastic']['func'] = extract('45-Rh-103(n,inelastic).txt')
Rh['reactions']['n,inelastic']['halflife'] = 56.12 * 60  # s
Rh['reactions']['n,inelastic']['label'] = r"($n,n'$)"


# indium
In = {}
In['M'] = 114.818  # g/mol
In['rho'] = 7.31  # g/cm3
In['reactions'] = {}

In['reactions']['n,gamma'] = {}
In['reactions']['n,gamma']['func'] = extract('49-In-115(n,&gamma;).txt')
In['reactions']['n,gamma']['halflife'] = 54 * 60  # s
In['reactions']['n,gamma']['label'] = r'($n,\gamma$)'


# gold
Au = {}
Au['M'] = 196.96657  # g/mol
Au['rho'] = 19.32  # g/cm3
Au['reactions'] = {}

Au['reactions']['n,gamma'] = {}
Au['reactions']['n,gamma']['func'] = extract('79-Au-197(n,&gamma;).txt')
Au['reactions']['n,gamma']['halflife'] = 2.7 * 60 * 60 * 24  # s
Au['reactions']['n,gamma']['label'] = r'($n,\gamma$)'

# all foils
foils = {}
foils['Al'] = Al
foils['Rh'] = Rh
foils['In'] = In
foils['Au'] = Au
