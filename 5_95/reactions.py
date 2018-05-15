from roi import calc_roi

reactions = {}

reactions['Al_np'] = ['../xs/13-Al-27(n,p)', 1E4, 1E7]
reactions['Al_na'] = ['../xs/13-Al-27(n,&alpha;)', 5E6, 1E7]

for key, vals in reactions.items():
    reactions[key].append(calc_roi(*vals))

for key, vals in reactions.items():
    print('{}: {:4.2e} eV  to  {:4.2e} eV'.format(key, *vals[-1]))
