rf_template = '''c TRIGA In-Core Foil Response Function Generator
c *****************************************************************************
c ------------------------------ CELL CARD ------------------------------------
c *****************************************************************************
10   {}   -10              imp:n=1  $ Foil
11   {}    10 -11          imp:n=1  $ Cd Covering
c
21   13  -0.001662    11 -21 -99      imp:n=1  $ Argon
22   12  -2.650       21 -22 -99      imp:n=1  $ Silica
23   13  -0.001662    22 -23 -99      imp:n=1  $ Argon
24   11  -4.506       23 -24 -99      imp:n=1  $ Titanium
25   10  -1.000       24     -99      imp:n=1  $ Water
c
99    0            99              imp:n=0  $ Graveyard
c -----------------------------------------------------------------------------
c *****************************************************************************

c *****************************************************************************
c ----------------------------- SURFACE CARD ----------------------------------
c *****************************************************************************
c -----------------------------------------------------------------------------
10  rpp  -0.05    0.05    -0.05    0.05   -0.005   0.005         $  Foil
11  rcc   0.00    0.00    -0.05    0.00    0.00    0.1   0.0875  $ Cd Covering
c
21 cz 0.100000
22 cz 0.235000
23 cz 0.238125
24 cz 0.396875
c
99  rcc   0.00    0.00    -10      0.00    0.00    20   5    $ Problem Space
c -----------------------------------------------------------------------------
c *****************************************************************************

c *****************************************************************************
c ------------------------------- DATA CARD -----------------------------------
c *****************************************************************************
c -----------------------------------------------------------------------------
c --------------------------- Source Definition -------------------------------
c -----------------------------------------------------------------------------
SDEF POS=0 0 0 EXT=d2 AXS=0 0 1 PAR=1 ERG=d3 RAD=d1       $ Source Term
SI1 0 2                                                   $ Radius of Source
SP1 -21 1                                                 $ Uniform Sampling
SI2 -1 1                                                  $ Zmin to Zmax
SP2 -21 0                                                 $ Uniform Sampling
c                               Energy Bins
{}c
c
c
c
nps 10000                                             $ Number of Particles
c
c -----------------------------------------------------------------------------
c ---------------------------- Tally Detectors --------------------------------
c -----------------------------------------------------------------------------
Mode N                                      $ Mode Neutron
c
F4:N  10
FM4   {}                          $ Tally Multiplier
FT4 SCX 3
c -----------------------------------------------------------------------------
c ------------------------------- Materials -----------------------------------
c -----------------------------------------------------------------------------
c indium 7.31 g/cm3
m1         49000.80c -1.0
c gold 19.32 g/cm3
m2         79000.80c -1.0
c rhodium 12.41 g/cm3
m3         45000.80c -1.0
c aluminum 2.7 g/cm3
m4         13000.80c -1.0
c water
m10         1001.80c -0.11209788
           1002.80c -2.5765672e-05
           8016.80c -0.88751705
           8017.80c -0.00035930374
c titanium (4.506 g/cm3)
m11       22000.80c -1.0
c silica
m12        8016.80c -0.53345939
          14028.80c -0.46654061
c argon
m13       18036.80c -0.0030036131
          18038.80c -0.00059774404
          18040.80c -0.99639864
c cadmium
m14       22000.80c -1.0
c -----------------------------------------------------------------------------
c *****************************************************************************
'''
