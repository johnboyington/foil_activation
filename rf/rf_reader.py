import numpy as np


def read_mcnp(filename, num_reactions):
    '''
    Reads an mcnp output file and parses out data from a single tally
    '''

    with open(filename, 'r') as F:
        s = F.read()

    s = s.split('1tally')[1].split('===')[0].split('\n')[11:-3][::4]
    response = np.zeros((num_reactions, len(s)//num_reactions))
    error = np.zeros((num_reactions, len(s)//num_reactions))
    for r in range(num_reactions):
        for i, val in enumerate(s[r::num_reactions]):
            response[r, i] = float(val.split()[0])
            error[r, i] = float(val.split()[1])
    print(len(response[0]))
    return response

if __name__ == '__main__':
    read_mcnp('mcnp/in.inpo', 2)
