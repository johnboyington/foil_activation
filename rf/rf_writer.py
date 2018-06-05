import numpy as np
from rf_template import rf_template


def cardWriter(card, data, elements):
    '''
    Function: cardWriter

    This will write multiline cards for SI and SP distributions for mcnp inputs

    Input Data:
        card - name and number of the card
        data array - a numpy array containing the data you'd like placed in the card.
        Outputs:
            a string that can be copied and pasted into an mcnp input file
    '''
    s = '{}   '.format(card)
    empty_card = '   ' + ' ' * len(card)
    elements_per_row = elements
    row_counter = 0
    element = '{:6}  ' if data.dtype in ['int32', 'int64'] else '{:14.6e}  '
    for i, d in enumerate(data):
        s += element.format(d)
        row_counter += 1
        if row_counter == elements_per_row and i + 1 != len(data):
            row_counter = 0
            s += '\n{}'.format(empty_card)
    s += '\n'
    return s


def write_mcnp(reaction, cadmium):
    '''
    Writes an mcnp input capable of generating a response function for
    a given foil and reaction.
    '''

    assert reaction in ['in', 'au', 'rh', 'al'], 'Not a valid foil!'

    name = reaction

    # foil
    foil_cards = {}
    foil_cards['in'] = (' 1  -7.31    ', '-1 1 (102) (4)')
    foil_cards['au'] = (' 2  -19.32   ', '-1 2 (102) (4) (16)')
    foil_cards['rh'] = (' 3  -12.41   ', '-1 3 (102) (4)')
    foil_cards['al'] = (' 4  -2.7     ', '-1 4 (102) (103) (107)')

    # which foil?
    foil_s, reaction_s = foil_cards[reaction]

    # cadmium
    if cadmium:
        cd_s = '14  -8.650   '
        name += '_cd'
    else:
        cd_s = '13  -0.001662'

    # source term
    erg = np.loadtxt('scale56.txt')
    source_s = cardWriter('SI3  H      ', erg, 4)
    erg_ones = np.ones(len(erg))
    erg_ones[0] = 0
    source_s += cardWriter('SP3         ', erg_ones, 4)

    inp = rf_template.format(foil_s, cd_s, source_s, reaction_s)

    with open('mcnp/' + name + '.inp', 'w+') as F:
        F.write(inp)


# write all
write_mcnp('in', False)
write_mcnp('in', True)
write_mcnp('au', False)
write_mcnp('au', True)
write_mcnp('rh', False)
write_mcnp('al', False)
