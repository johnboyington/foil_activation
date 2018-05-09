

class Foil(object):
    def __init__(self, key):
        self.key = key
        self.store_mass(-1)

    def store_mass(self, m):
        '''
        Stores the foil mass (mg).
        '''
        self.mass = m
