import numpy as np
import matplotlib.pyplot as plt

names = ['in_n,gamma', 'in_n,inelastic', 'in_cd_n,gamma', 'in_cd_n,inelastic',
         'au_n,gamma', 'au_n,inelastic', 'au_n,2n',
         'au_cd_n,gamma', 'au_cd_n,inelastic', 'au_cd_n,2n',
         'rh_n,gamma', 'rh_n,inelastic',
         'al_n,gamma', 'al_n,p', 'al_n,alpha']


def package_rfs(rf_indices):
    '''
    Given indices of various responses, prepares response matrix.
    '''
    erg = np.loadtxt('/home/john/workspace/foil_activation/rf/scale56.txt')
    rf_matrix = np.zeros((len(rf_indices), len(erg) - 1))

    for i, rf in enumerate(rf_indices):
        name = names[rf]
        vals = np.loadtxt('/home/john/workspace/foil_activation/rf/data/' + name + '.txt')
        rf_matrix[i] = vals
    return rf_matrix


if __name__ == '__main__':
    test = package_rfs([0, 2, 4, 6, 7, 9, 10, 12, 13, 14])
    for i, row in enumerate(test):
        test[i] = test[i] / np.sum(row)
        test[i] = test[i] * (1 / np.max(test[i]))
    print(test)
    plt.imshow(test, cmap='YlOrRd')
