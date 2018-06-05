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
        np.savetxt('data/' + name + '.txt', r)
        np.savetxt('data/' + name + '_err.txt', e)
    return response

if __name__ == '__main__':
    read_mcnp('mcnp/in.io', ['in_n,gamma', 'in_n,inelastic'], 2)
