from foil_manager import foils


s = '''\\begin{{table*}}[h]
\\centering
\\begin{{tabular}}{{ {} }}
 \\hline
 {}
 \\hline
{}
 \\hline
\\end{{tabular}}
\\end{{table*}}'''


def tabulate_foil_info(foils, s, num_cols):
    '''
    Produces latex readable table with foil ids and masses.
    '''
    num_foils = len(foils.keys())
    col_str = '|' + 'c|' * (num_cols * 2)
    header_str = 'Foil ID & Mass ($\mu g$) & ' * num_cols
    header_str = header_str[:-2] + '\\\\'
    data_str = ''
    for i, f in enumerate(foils.values()):
        data_str += '{} & {:6.2f}'.format(f.key, f.mass)
        if not (i + 1) % 3:
            data_str += ' \\\\ \n'
        else:
            data_str += ' & '
    data_str += '& ' * (((3 - (num_foils % num_cols)) * 2) - 1)
    if num_foils % num_cols != 0:
        data_str += '\\\\'
    s = s.format(col_str, header_str, data_str)
    print(s)

tabulate_foil_info(foils, s, 3)
