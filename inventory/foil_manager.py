from foil import Foil


def initialize_dictionary():
    foils = {}
    # import list of foil keys and store in dictionary
    with open('foil_ids.txt', 'r') as F:
        foil_keys = F.read().splitlines()
    for key in foil_keys:
        foils[key] = Foil(key)
    return foils, foil_keys


def store_foil_masses(foils, foil_keys):
    # store foil masses
    with open('masses.txt', 'r') as F:
        lines = F.readlines()

    for i, line in enumerate(lines):
        line = line.split()
        assert len(line) >= 2, 'Problem reading line {} of masses.txt.'.format(i)
        assert line[0] in foils, 'Foil mass in line {} not included in foil_ids.txt.'.format(i)
        mass = 0
        if len(line) == 2:
            mass = float(line[1])
        else:
            for val in line[1:]:
                mass += float(val)
            mass = mass / len(line[1:])
        foils[line[0]].store_mass(mass)
    return foils


foils, foil_keys = initialize_dictionary()
foils = store_foil_masses(foils, foil_keys)
