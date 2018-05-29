from scipy.interpolate import interp1d
import numpy as np


def extract(xs_string):
    xs_erg, xs_vals = np.loadtxt('xs/' + xs_string, delimiter=',', skiprows=1, unpack=True)
    f = interp1d(xs_erg, xs_vals, bounds_error=False, fill_value=0)
    region = xs_erg[0], xs_erg[-1]
    return f, region


# cadmium
Cd = {}
Cd['M'] = 112.411  # g/mol
Cd['rho'] = 8.69  # g/cm3
Cd['reactions'] = {}

cd_xs_data = [extract('48-Cd-106(n,total).txt')[0],
              extract('48-Cd-108(n,total).txt')[0],
              extract('48-Cd-110(n,total).txt')[0],
              extract('48-Cd-111(n,total).txt')[0],
              extract('48-Cd-112(n,total).txt')[0],
              extract('48-Cd-113(n,total).txt')[0],
              extract('48-Cd-114(n,total).txt')[0],
              extract('48-Cd-116(n,total).txt')[0]]

cd_weights = [0.0125, 0.0089, 0.1249, 0.1280, 0.2413, 0.1222, 0.2873, 0.0749]


def cd_xs_weighted(e):
    xs = 0
    for isotope in range(len(cd_weights)):
        xs += cd_weights[isotope] * cd_xs_data[isotope](e)
    return xs


Cd['reactions']['n,tot'] = {}
Cd['reactions']['n,tot']['func'] = cd_xs_weighted
Cd['reactions']['n,tot']['halflife'] = 0  # s
Cd['reactions']['n,tot']['label'] = r'($n,tot$)'

# aluminum
Al = {}
Al['M'] = 26.9815385  # g/mol
Al['rho'] = 2.7  # g/cm3
Al['reactions'] = {}

# Al27(n,p)Mg27
Al['reactions']['n,p'] = {}
f, r = extract('13-Al-27(n,p)')
Al['reactions']['n,p']['func'] = f
Al['reactions']['n,p']['region'] = r
Al['reactions']['n,p']['roi'] = r
Al['reactions']['n,p']['roi_cd'] = r
Al['reactions']['n,p']['halflife'] = 9.458 * 60  # s
Al['reactions']['n,p']['label'] = r'($n,p$)'
Al['reactions']['n,p']['erg'] = [(.007, 180), (.7, 840), (.3, 1013)]  # keV (placeholder)
Al['reactions']['n,p']['plotname'] = 'al_n,p'

# Al27(n,a)Na24
Al['reactions']['n,alpha'] = {}
f, r = extract('13-Al-27(n,&alpha;)')
Al['reactions']['n,alpha']['func'] = f
Al['reactions']['n,alpha']['region'] = r
Al['reactions']['n,alpha']['roi'] = r
Al['reactions']['n,alpha']['roi_cd'] = r
Al['reactions']['n,alpha']['halflife'] = 15.03 * 60 * 60  # s
Al['reactions']['n,alpha']['label'] = r'($n,\alpha$)'
Al['reactions']['n,alpha']['erg'] = [(1, 1369), (1, 2754)]  # keV
Al['reactions']['n,alpha']['plotname'] = 'al_n,alpha'

# Al27(n,g)Al28
Al['reactions']['n,gamma'] = {}
f, r = extract('13-Al-27(n,&gamma;)')
Al['reactions']['n,gamma']['func'] = f
Al['reactions']['n,gamma']['region'] = r
Al['reactions']['n,gamma']['roi'] = r
Al['reactions']['n,gamma']['roi_cd'] = r
Al['reactions']['n,gamma']['halflife'] = 2.246 * 60  # s
Al['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Al['reactions']['n,gamma']['erg'] = [(1, 1780)]  # keV (placeholder)
Al['reactions']['n,gamma']['plotname'] = 'al_n,gamma'


# rhodium
Rh = {}
Rh['M'] = 102.90550  # g/mol
Rh['rho'] = 12.41  # g/cm3
Rh['reactions'] = {}

Rh['reactions']['n,gamma'] = {}
f, r = extract('45-Rh-103(n,&gamma;).txt')
Rh['reactions']['n,gamma']['func'] = f
Rh['reactions']['n,gamma']['region'] = r
Rh['reactions']['n,gamma']['roi'] = r
Rh['reactions']['n,gamma']['roi_cd'] = r
Rh['reactions']['n,gamma']['halflife'] = 4.4 * 60  # s
Rh['reactions']['n,gamma']['label'] = r"($n,\gamma$)"
Rh['reactions']['n,gamma']['erg'] = [(0.47, 51), (0.025, 78), (0.026, 560), (0.0018, 770)]  # intensity, keV
Rh['reactions']['n,gamma']['plotname'] = 'rh_n,gamma'

Rh['reactions']['n,inelastic'] = {}
f, r = extract('45-Rh-103(n,inelastic).txt')
Rh['reactions']['n,inelastic']['func'] = f
Rh['reactions']['n,inelastic']['region'] = r
Rh['reactions']['n,inelastic']['roi'] = r
Rh['reactions']['n,inelastic']['roi_cd'] = r
Rh['reactions']['n,inelastic']['halflife'] = 56.12 * 60  # s
Rh['reactions']['n,inelastic']['label'] = r"($n,n'$)"
Rh['reactions']['n,inelastic']['erg'] = [(0.004, 40)]  # intensity, keV

# Rh['reactions']['n,2n'] = {}
# Rh['reactions']['n,2n']['func'] = extract('45-Rh-103(n,2n).txt')
# Rh['reactions']['n,2n']['halflife'] = 35.4 * 60 * 60  # s
# Rh['reactions']['n,2n']['label'] = r"($n,2n$)"
# Rh['reactions']['n,inelastic']['erg'] = [(0.004, 40)]  # intensity, keV

# Rh['reactions']['n,p'] = {}
# Rh['reactions']['n,p']['func'] = extract('45-Rh-103(n,inelastic).txt')
# Rh['reactions']['n,p']['halflife'] = 39.35 * 60 * 60 * 24  # s
# Rh['reactions']['n,p']['label'] = r"($n,p$)"


# indium
In = {}
In['M'] = 114.818  # g/mol
In['rho'] = 7.31  # g/cm3
In['reactions'] = {}

In['reactions']['n,gamma'] = {}
f, r = extract('49-In-115(n,&gamma;).txt')
In['reactions']['n,gamma']['func'] = f
In['reactions']['n,gamma']['region'] = r
In['reactions']['n,gamma']['roi'] = r
In['reactions']['n,gamma']['roi_cd'] = r
In['reactions']['n,gamma']['halflife'] = 54 * 60  # s
In['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
In['reactions']['n,gamma']['erg'] = [(0.03, 138), (0.36, 417), (0.17, 819), (0.53, 1090),
                                     (0.8, 1293), (0.11, 1508), (0.2, 2111)]  # intensity, keV
In['reactions']['n,gamma']['plotname'] = 'in_n,gamma'

In['reactions']['n,inelastic'] = {}
f, r = extract('49-In-115(n,inelastic).txt')
In['reactions']['n,inelastic']['func'] = f
In['reactions']['n,inelastic']['region'] = r
In['reactions']['n,inelastic']['roi'] = r
In['reactions']['n,inelastic']['roi_cd'] = r
In['reactions']['n,inelastic']['halflife'] = 4.36 * 60 * 60  # s
In['reactions']['n,inelastic']['label'] = r"($n,n'$)"
In['reactions']['n,inelastic']['erg'] = [(0.5, 335)]  # intensity, keV
In['reactions']['n,inelastic']['plotname'] = 'in_n,inelastic'


# gold
Au = {}
Au['M'] = 196.96657  # g/mol
Au['rho'] = 19.32  # g/cm3
Au['reactions'] = {}

Au['reactions']['n,gamma'] = {}
f, r = extract('79-Au-197(n,&gamma;).txt')
Au['reactions']['n,gamma']['func'] = f
Au['reactions']['n,gamma']['region'] = r
Au['reactions']['n,gamma']['roi'] = 6.7266e-03, 5.2684e+00  # computed
Au['reactions']['n,gamma']['roi_cd'] = 1, 9  # initial guess
Au['reactions']['n,gamma']['halflife'] = 2.7 * 60 * 60 * 24  # s
Au['reactions']['n,gamma']['label'] = r'($n,\gamma$)'
Au['reactions']['n,gamma']['erg'] = [(0.95, 412), (0.01, 676), (0.002, 1088)]  # intensity, keV
Au['reactions']['n,gamma']['plotname'] = 'au_n,gamma'

Au['reactions']['n,2n'] = {}
f, r = extract('79-Au-197(n,2n).txt')
Au['reactions']['n,2n']['func'] = f
Au['reactions']['n,2n']['region'] = r
Au['reactions']['n,2n']['roi'] = 8.8259e+06, 1.3510e+07  # computed
Au['reactions']['n,2n']['roi_cd'] = 8.8259e+06, 1.3510e+07  # initial guess
Au['reactions']['n,2n']['halflife'] = 6.18 * 60 * 60 * 24  # s
Au['reactions']['n,2n']['label'] = r'($n,2n$)'
Au['reactions']['n,2n']['erg'] = [(0.25, 333), (0.94, 356), (0.06, 426), (0.002, 1091)]  # intensity, keV
Au['reactions']['n,2n']['plotname'] = 'au_n,2n'

Au['reactions']['n,inelastic'] = {}
f, r = extract('79-Au-197(n,inelastic).txt')
Au['reactions']['n,inelastic']['func'] = f
Au['reactions']['n,inelastic']['region'] = r
Au['reactions']['n,inelastic']['roi'] = 3.2404e+05, 5.2532e+06  # computed
Au['reactions']['n,inelastic']['roi_cd'] = 3.2404e+05, 5.2532e+06  # initial guess
Au['reactions']['n,inelastic']['halflife'] = 7.8  # s
Au['reactions']['n,inelastic']['label'] = r"($n,n'$)"
Au['reactions']['n,inelastic']['erg'] = [(0.08, 130), (0.75, 279)]  # intensity, keV
Au['reactions']['n,inelastic']['plotname'] = 'au_n,inelastic'

# all foils
foils = {}
foils['Al'] = Al
foils['Rh'] = Rh
foils['In'] = In
foils['Au'] = Au
