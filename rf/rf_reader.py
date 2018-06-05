import numpy as np


def read_mcnp(readfile, writefiles, num_reactions):
    '''
    Reads an mcnp output file and parses out data from a single tally
    '''

    assert len(writefiles) == num_reactions, 'Inconsistency in input.'

    with open(readfile, 'r') as F:
        s = F.read()

    s = s.split('1tally')[1].split('===')[0].split('\n')[11:-3][::4]
    response = np.zeros((num_reactions, len(s)//num_reactions))
    error = np.zeros((num_reactions, len(s)//num_reactions))
    for r in range(num_reactions):
        for i, val in enumerate(s[r::num_reactions]):
            response[r, i] = float(val.split()[0])
            error[r, i] = float(val.split()[1])
    for name, r, e in zip(writefiles, response, error):
        np.savetxt('data/' + name + '.txt', r[:-1])
        np.savetxt('data/' + name + '_err.txt', e[:-1])
    return response

# read all
read_mcnp('mcnp/in.inpo', ['in_n,gamma', 'in_n,inelastic'], 2)
read_mcnp('mcnp/in_cd.inpo', ['in_cd_n,gamma', 'in_cd_n,inelastic'], 2)
read_mcnp('mcnp/au.inpo', ['au_n,gamma', 'au_n,inelastic', 'au_n,2n'], 3)
read_mcnp('mcnp/au_cd.inpo', ['au_cd_n,gamma', 'au_cd_n,inelastic', 'au_cd_n,2n'], 3)
read_mcnp('mcnp/rh.inpo', ['rh_n,gamma', 'rh_n,inelastic'], 2)
read_mcnp('mcnp/al.inpo', ['al_n,gamma', 'al_n,p', 'al_n,alpha'], 3)
