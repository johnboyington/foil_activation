          Code Name & Version = MCNP6, 1.0
  
     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/
    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       
   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    
  _/      _/      _/             _/    _/_/       _/           _/    _/   
 _/      _/        _/_/_/       _/      _/       _/             _/_/      
  
  +---------------------------------------------------------------------+
  | Copyright 2008. Los Alamos National Security, LLC.  All rights      |
  | reserved.                                                           |
  |   This material was produced under U.S. Government contract         |
  | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      |
  | operated by Los Alamos National Security, LLC, for the U.S.         |
  | Department of Energy. The Government is granted for itself and      |
  | others acting on its behalf a paid-up, nonexclusive, irrevocable    |
  | worldwide license in this material to reproduce, prepare derivative |
  | works, and perform publicly and display publicly. Beginning five    |
  | (5) years after 2008, subject to additional five-year worldwide     |
  | renewals, the Government is granted for itself and others acting on |
  | its behalf a paid-up, nonexclusive, irrevocable worldwide license   |
  | in this material to reproduce, prepare derivative works, distribute |
  | copies to the public, perform publicly and display publicly, and to |
  | permit others to do so. NEITHER THE UNITED STATES NOR THE UNITED    |
  | STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, |
  | NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, |
  | OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  |
  | COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, |
  | OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE |
  | PRIVATELY OWNED RIGHTS.                                             |
  +---------------------------------------------------------------------+
  
1mcnp     version 6     ld=05/08/13                     06/04/18 17:30:05 
 *************************************************************************                 probid =  06/04/18 17:30:05 
 name=in.i tasks 26                                                              

 
  warning.  Physics models disabled.
         1-       c TRIGA In-Core Foil Response Function Generator                                
         2-       c ***************************************************************************** 
         3-       c ------------------------------ CELL CARD ------------------------------------ 
         4-       c ***************************************************************************** 
         5-       10    1  -7.31       -10              imp:n=1  $ Foil                           
         6-       11   14  -8.650       10 -11          imp:n=1  $ Cd Covering                    
         7-       c                                                                               
         8-       21   13  -0.001662    11 -21 -99      imp:n=1  $ Argon                          
         9-       22   12  -2.650       21 -22 -99      imp:n=1  $ Silica                         
        10-       23   13  -0.001662    22 -23 -99      imp:n=1  $ Argon                          
        11-       24   11  -4.506       23 -24 -99      imp:n=1  $ Titanium                       
        12-       25   10  -1.000       24     -99      imp:n=1  $ Water                          
        13-       c                                                                               
        14-       99    0            99              imp:n=0  $ Graveyard                         
        15-       c ----------------------------------------------------------------------------- 
        16-       c ***************************************************************************** 
        17-                                                                                       
        18-       c ***************************************************************************** 
        19-       c ----------------------------- SURFACE CARD ---------------------------------- 
        20-       c ***************************************************************************** 
        21-       c ----------------------------------------------------------------------------- 
        22-       10  rpp  -0.05    0.05    -0.05    0.05   -0.005   0.005         $  Foil        
        23-       11  rcc   0.00    0.00    -0.05    0.00    0.00    0.1   0.0875  $ Cd Covering  
        24-       c                                                                               
        25-       21 cz 0.100000                                                                  
        26-       22 cz 0.235000                                                                  
        27-       23 cz 0.238125                                                                  
        28-       24 cz 0.396875                                                                  
        29-       c                                                                               
        30-       99  rcc   0.00    0.00    -5      0.00    0.00    10   5    $ Problem Space     
        31-       c ----------------------------------------------------------------------------- 
        32-       c ***************************************************************************** 
        33-                                                                                       
        34-       c ***************************************************************************** 
        35-       c ------------------------------- DATA CARD ----------------------------------- 
        36-       c ***************************************************************************** 
        37-       c ----------------------------------------------------------------------------- 
        38-       c --------------------------- Source Definition ------------------------------- 
        39-       c ----------------------------------------------------------------------------- 
        40-       SDEF POS=0 0 0 EXT=d2 AXS=0 0 1 PAR=1 ERG=d3 RAD=d1       $ Source Term         
        41-       SI1 0 2                                                   $ Radius of Source    
        42-       SP1 -21 1                                                 $ Uniform Sampling    
        43-       SI2 -1 1                                                  $ Zmin to Zmax        
        44-       SP2 -21 0                                                 $ Uniform Sampling    
        45-       c                               Energy Bins                                     
        46-       SI3  H           1.000000e-11    4.000000e-09    1.000000e-08    2.530000e-08   
        47-                        4.000000e-08    5.000000e-08    6.000000e-08    8.000000e-08   
        48-                        1.000000e-07    1.500000e-07    2.000000e-07    2.500000e-07   
        49-                        3.250000e-07    3.500000e-07    3.750000e-07    4.500000e-07   
        50-                        6.250000e-07    1.010000e-06    1.080000e-06    1.130000e-06   
        51-                        5.000000e-06    6.250000e-06    6.500000e-06    6.880000e-06   
        52-                        7.000000e-06    2.050000e-05    2.120000e-05    2.180000e-05   
        53-                        3.600000e-05    3.710000e-05    6.500000e-05    6.750000e-05   
        54-                        1.010000e-04    1.050000e-04    1.160000e-04    1.180000e-04   
        55-                        1.880000e-04    1.920000e-04    2.250000e-03    3.740000e-03   
        56-                        1.700000e-02    2.000000e-02    5.000000e-02    2.000000e-01   
        57-                        2.700000e-01    3.300000e-01    4.700000e-01    6.000000e-01   
        58-                        7.500000e-01    8.610000e-01    1.200000e+00    1.500000e+00   
        59-                        1.850000e+00    3.000000e+00    4.300000e+00    6.430000e+00   
        60-                        2.000000e+01                                                   
        61-       SP3              0.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        62-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        63-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        64-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        65-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        66-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        67-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        68-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        69-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        70-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        71-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        72-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        73-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        74-                        1.000000e+00    1.000000e+00    1.000000e+00    1.000000e+00   
        75-                        1.000000e+00                                                   
        76-       c                                                                               
        77-       c                                                                               
        78-       c                                                                               
        79-       c                                                                               
        80-       nps 4e8                                             $ Number of Particles       
        81-       c                                                                               
        82-       c ----------------------------------------------------------------------------- 
        83-       c ---------------------------- Tally Detectors -------------------------------- 
        84-       c ----------------------------------------------------------------------------- 
        85-       Mode N                                      $ Mode Neutron                      
        86-       c                                                                               
        87-       F4:N  10                                                                        
        88-       FM4   -1 1 (102) (4)                          $ Tally Multiplier                
        89-       FT4 SCX 3                                                                       
        90-       c ----------------------------------------------------------------------------- 
        91-       c ------------------------------- Materials ----------------------------------- 
        92-       c ----------------------------------------------------------------------------- 
        93-       c indium 7.31 g/cm3                                                             
        94-       m1         49113.80c  0.0428                                                    
        95-                  49115.80c  0.9572                                                    
        96-       c gold 19.32 g/cm3                                                              
        97-       m2         79197.80c  1.0                                                       
  warning.  material        2 is not used in the problem.
        98-       c rhodium 12.41 g/cm3                                                           
        99-       m3         45103.80c  1.0                                                       
  warning.  material        3 is not used in the problem.
       100-       c aluminum 2.7 g/cm3                                                            
       101-       m4         13027.80c  1.0                                                       
  warning.  material        4 is not used in the problem.
       102-       c water                                                                         
       103-       m10         1001.80c -0.11209788                                                
       104-                  1002.80c -2.5765672e-05                                              
       105-                  8016.80c -0.88751705                                                 
       106-                  8017.80c -0.00035930374                                              
       107-       c titanium (4.506 g/cm3)                                                        
       108-       m11       22046.80c  0.0825                                                     
       109-                 22047.80c  0.0744                                                     
       110-                 22048.80c  0.7372                                                     
       111-                 22049.80c  0.0541                                                     
       112-                 22050.80c  0.0518                                                     
       113-       c silica                                                                        
       114-       m12        8016.80c -0.53345939                                                 
       115-                 14028.80c -0.46654061                                                 
       116-       c argon                                                                         
       117-       m13       18036.80c -0.0030036131                                               
       118-                 18038.80c -0.00059774404                                              
       119-                 18040.80c -0.99639864                                                 
       120-       c cadmium                                                                       
       121-       m14       48106.80c  0.0125                                                     
       122-                 48108.80c  0.0089                                                     
       123-                 48110.80c  0.1247                                                     
       124-                 48111.80c  0.1280                                                     
       125-                 48112.80c  0.2411                                                     
       126-                 48113.80c  0.1223                                                     
       127-                 48114.80c  0.2875                                                     
       128-                 48116.80c  0.0751                                                     
       129-       c ----------------------------------------------------------------------------- 
       130-       c ***************************************************************************** 
 
  comment.  total nubar used if fissionable isotopes are present.
 
  warning.    1 materials had unnormalized fractions. print table 40.
1cells                                                                                                  print table 60

                               atom        gram                                            neutron                                     
              cell      mat   density     density     volume       mass            pieces importance                                   

        1       10        1  3.83398E-02 7.31000E+00 1.00000E-04 7.31000E-04           0  1.0000E+00                                   
        2       11       14  4.63386E-02 8.65000E+00 0.00000E+00 0.00000E+00           0  1.0000E+00                                   
        3       21       13  2.50543E-05 1.66200E-03 3.11754E-01 5.18135E-04           1  1.0000E+00                                   
        4       22       12  7.98363E-02 2.65000E+00 1.42079E+00 3.76508E+00           1  1.0000E+00                                   
        5       23       13  2.50543E-05 1.66200E-03 4.64489E-02 7.71981E-05           1  1.0000E+00                                   
        6       24       11  5.66893E-02 4.50600E+00 3.16692E+00 1.42701E+01           1  1.0000E+00                                   
        7       25       10  1.00417E-01 1.00000E+00 7.80450E+02 7.80450E+02           1  1.0000E+00                                   
        8       99        0  0.00000E+00 0.00000E+00 0.00000E+00 0.00000E+00           0  0.0000E+00                                   

 total                                               7.85396E+02 7.98486E+02

    minimum source weight = 1.0000E+00    maximum source weight = 1.0000E+00

 ***************************************************
 * Random Number Generator  =                    1 *
 * Random Number Seed       =       19073486328125 *
 * Random Number Multiplier =       19073486328125 *
 * Random Number Adder      =                    0 *
 * Random Number Bits Used  =                   48 *
 * Random Number Stride     =               152917 *
 ***************************************************

 
  comment.  threading will be used when possible in portions of mcnp6.
 
  comment.  threading will be used for n/p/e table physics.
 
  comment.  threading will generally not be used for model physics.

         5 warning messages so far.
1cross-section tables                                                                                   print table 100
     XSDIR used: /home/john/opt/mcnp/MCNP_DATA/xsdir_mcnp6.1

     table    length

                        tables from file xdata/endf71x/H/1001.710nc                                      

 particle-production data for deuterons being expunged from   1001.80c
   1001.80c    3652  H1 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)          mat 125      12/17/12

                        tables from file xdata/endf71x/H/1002.710nc                                      

 particle-production data for protons   being expunged from   1002.80c
 particle-production data for tritons   being expunged from   1002.80c
   1002.80c    5924  H2 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)          mat 128      12/17/12

                        tables from file xdata/endf71x/O/8016.710nc                                      

 particle-production data for protons   being expunged from   8016.80c
 particle-production data for deuterons being expunged from   8016.80c
 particle-production data for tritons   being expunged from   8016.80c
 particle-production data for alphas    being expunged from   8016.80c
   8016.80c  171194  O16 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)         mat 825      12/13/12

                        tables from file xdata/endf71x/O/8017.710nc                                      

   8017.80c    4921  O17 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)         mat 828      12/13/12

                        tables from file xdata/endf71x/Si/14028.710nc                                    

 particle-production data for protons   being expunged from  14028.80c
 particle-production data for deuterons being expunged from  14028.80c
 particle-production data for tritons   being expunged from  14028.80c
 particle-production data for alphas    being expunged from  14028.80c
  14028.80c  105939  Si28 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat1425      12/14/12

                        tables from file xdata/endf71x/Ar/18036.710nc                                    

  18036.80c   11998  Ar36 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat1825      12/16/12

                        tables from file xdata/endf71x/Ar/18038.710nc                                    

  18038.80c   13256  Ar38 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat1831      12/16/12
                     probability tables used from 3.0000E-01 to 1.0000E+00 mev.

                        tables from file xdata/endf71x/Ar/18040.710nc                                    

  18040.80c  134198  Ar40 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat1837      12/15/12

                        tables from file xdata/endf71x/Ti/22046.710nc                                    

 particle-production data for protons   being expunged from  22046.80c
 particle-production data for alphas    being expunged from  22046.80c
  22046.80c  145305  Ti46 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat2225      12/13/12

                        tables from file xdata/endf71x/Ti/22047.710nc                                    

 particle-production data for protons   being expunged from  22047.80c
 particle-production data for alphas    being expunged from  22047.80c
  22047.80c  119224  Ti47 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat2228      12/13/12

                        tables from file xdata/endf71x/Ti/22048.710nc                                    

 particle-production data for protons   being expunged from  22048.80c
 particle-production data for alphas    being expunged from  22048.80c
  22048.80c  136941  Ti48 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat2231      12/13/12

                        tables from file xdata/endf71x/Ti/22049.710nc                                    

 particle-production data for protons   being expunged from  22049.80c
 particle-production data for alphas    being expunged from  22049.80c
  22049.80c  113471  Ti49 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat2234      12/13/12

                        tables from file xdata/endf71x/Ti/22050.710nc                                    

 particle-production data for protons   being expunged from  22050.80c
 particle-production data for alphas    being expunged from  22050.80c
  22050.80c   84997  Ti50 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)        mat2237      12/15/12

                        tables from file xdata/endf71x/Cd/48106.710nc                                    

  48106.80c   83616  Cd106 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4825      12/15/12

                        tables from file xdata/endf71x/Cd/48108.710nc                                    

  48108.80c   65207  Cd108 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4831      12/15/12
                     probability tables used from 6.0000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48110.710nc                                    

  48110.80c   89529  Cd110 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4837      12/13/12
                     probability tables used from 7.0000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48111.710nc                                    

  48111.80c  163107  Cd111 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4840      12/13/12
                     probability tables used from 2.3000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48112.710nc                                    

  48112.80c  113359  Cd112 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4843      12/13/12
                     probability tables used from 1.1500E-02 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48113.710nc                                    

  48113.80c  296003  Cd113 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4846      12/13/12
                     probability tables used from 5.0000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48114.710nc                                    

  48114.80c   86548  Cd114 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4849      12/13/12
                     probability tables used from 8.0000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/Cd/48116.710nc                                    

  48116.80c   58281  Cd116 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4855      12/13/12
                     probability tables used from 9.5000E-03 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/In/49113.710nc                                    

 
  warning.  fm/pert card rxn   4 is missing from  49113.80c
  49113.80c  137689  In113 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4925      12/15/12
                     probability tables used from 6.0000E-04 to 1.0000E-01 mev.

                        tables from file xdata/endf71x/In/49115.710nc                                    

 
  warning.  fm/pert card rxn   4 is missing from  49115.80c
  49115.80c  209983  In115 ENDF71x (jlconlin)  Ref. see jlconlin (ref 09/10/2012  10:00:53)       mat4931      12/19/12
                     probability tables used from 2.0000E-03 to 1.0000E-01 mev.

  total     2354342

1particles and energy limits                                                                            print table 101

                         particle      maximum       smallest      largest       always        always
                         cutoff        particle      table         table         use table     use model
   particle type         energy        energy        maximum       maximum       below         above

    1  n    neutron     0.0000E+00    1.0000E+36    2.0000E+01    1.5000E+02    1.0000E+36    1.0000E+36
 

 ***********************************************************************************************************************

 dump no.    1 on file in.ir     nps =           0     coll =              0     ctm =        0.00   nrn =              
   0

         7 warning messages so far.

 ***********************************************************************************************************************

 dump no.    2 on file in.ir     nps =    10212069     coll =      302561051     ctm =     1560.53   nrn =       
 5230039223

 ***********************************************************************************************************************

 dump no.    3 on file in.ir     nps =    20455639     coll =      606219087     ctm =     3121.01   nrn =      
 10479190312

 ***********************************************************************************************************************

 dump no.    4 on file in.ir     nps =    30677927     coll =      909324962     ctm =     4681.40   nrn =      
 15718616402

 ***********************************************************************************************************************

 dump no.    5 on file in.ir     nps =    40926865     coll =     1212978655     ctm =     6241.75   nrn =      
 20967480505

 ***********************************************************************************************************************

 dump no.    6 on file in.ir     nps =    51163159     coll =     1516379952     ctm =     7802.25   nrn =      
 26212156360

 ***********************************************************************************************************************

 dump no.    7 on file in.ir     nps =    61361086     coll =     1818676111     ctm =     9362.62   nrn =      
 31437559233

 ***********************************************************************************************************************

 dump no.    8 on file in.ir     nps =    71579285     coll =     2121581424     ctm =    10923.06   nrn =      
 36673713948

 ***********************************************************************************************************************

 dump no.    9 on file in.ir     nps =    81755521     coll =     2423096252     ctm =    12483.44   nrn =      
 41885502498

 ***********************************************************************************************************************

 dump no.   10 on file in.ir     nps =    91943418     coll =     2725041876     ctm =    14043.85   nrn =      
 47105020388

 ***********************************************************************************************************************

 dump no.   11 on file in.ir     nps =   102111261     coll =     3026550488     ctm =    15604.27   nrn =      
 52316952244

 ***********************************************************************************************************************

 dump no.   12 on file in.ir     nps =   112292620     coll =     3328170613     ctm =    17164.66   nrn =      
 57530763900

 ***********************************************************************************************************************

 dump no.   13 on file in.ir     nps =   122465041     coll =     3629897266     ctm =    18725.17   nrn =      
 62746632956

 ***********************************************************************************************************************

 dump no.   14 on file in.ir     nps =   132704275     coll =     3933428996     ctm =    20285.63   nrn =      
 67993502475

 ***********************************************************************************************************************

 dump no.   15 on file in.ir     nps =   142972725     coll =     4237750182     ctm =    21846.00   nrn =      
 73254068300

 ***********************************************************************************************************************

 dump no.   16 on file in.ir     nps =   153198883     coll =     4540733968     ctm =    23406.41   nrn =      
 78491430958

 ***********************************************************************************************************************

 dump no.   17 on file in.ir     nps =   163440737     coll =     4844360372     ctm =    24966.85   nrn =      
 83739742131

 ***********************************************************************************************************************

 dump no.   18 on file in.ir     nps =   173641934     coll =     5146542124     ctm =    26527.27   nrn =      
 88963305984

 ***********************************************************************************************************************

 dump no.   19 on file in.ir     nps =   183854136     coll =     5449366150     ctm =    28087.75   nrn =      
 94197863293

 ***********************************************************************************************************************

 dump no.   20 on file in.ir     nps =   194035172     coll =     5751063417     ctm =    29648.13   nrn =      
 99412813772

 ***********************************************************************************************************************

 dump no.   21 on file in.ir     nps =   204227972     coll =     6053232081     ctm =    31208.52   nrn =     
 104636139062

 ***********************************************************************************************************************

 dump no.   22 on file in.ir     nps =   214437558     coll =     6356015322     ctm =    32768.82   nrn =     
 109869998355

 ***********************************************************************************************************************

 dump no.   23 on file in.ir     nps =   224654564     coll =     6658853744     ctm =    34329.21   nrn =     
 115104813601

 ***********************************************************************************************************************

 dump no.   24 on file in.ir     nps =   234876031     coll =     6961846109     ctm =    35889.71   nrn =     
 120342303866

 ***********************************************************************************************************************

 dump no.   25 on file in.ir     nps =   245087369     coll =     7264474098     ctm =    37450.12   nrn =     
 125573477565

 ***********************************************************************************************************************

 dump no.   26 on file in.ir     nps =   255316793     coll =     7567854790     ctm =    39010.55   nrn =     
 130817696071

 ***********************************************************************************************************************

 dump no.   27 on file in.ir     nps =   265564093     coll =     7871541095     ctm =    40571.03   nrn =     
 136067206663

 ***********************************************************************************************************************

 dump no.   28 on file in.ir     nps =   275767692     coll =     8174023170     ctm =    42131.54   nrn =     
 141295987867

 ***********************************************************************************************************************

 dump no.   29 on file in.ir     nps =   285950791     coll =     8475955080     ctm =    43691.93   nrn =     
 146515124027

 ***********************************************************************************************************************

 dump no.   30 on file in.ir     nps =   296154600     coll =     8778286435     ctm =    45252.39   nrn =     
 151741093980

 ***********************************************************************************************************************

 dump no.   31 on file in.ir     nps =   306366592     coll =     9080966414     ctm =    46812.76   nrn =     
 156973255377

 ***********************************************************************************************************************

 dump no.   32 on file in.ir     nps =   316577268     coll =     9383651199     ctm =    48373.20   nrn =     
 162205431183

 ***********************************************************************************************************************

 dump no.   33 on file in.ir     nps =   326787952     coll =     9686320130     ctm =    49933.65   nrn =     
 167437344728

 ***********************************************************************************************************************

 dump no.   34 on file in.ir     nps =   337002661     coll =     9989198849     ctm =    51493.98   nrn =     
 172672810481

 ***********************************************************************************************************************

 dump no.   35 on file in.ir     nps =   347220321     coll =    10292068156     ctm =    53054.38   nrn =     
 177908245364

 ***********************************************************************************************************************

 dump no.   36 on file in.ir     nps =   357454549     coll =    10595515890     ctm =    54614.78   nrn =     
 183153686571

 ***********************************************************************************************************************

 dump no.   37 on file in.ir     nps =   367692467     coll =    10898872363     ctm =    56175.22   nrn =     
 188397464764

 ***********************************************************************************************************************

 dump no.   38 on file in.ir     nps =   377914923     coll =    11201917690     ctm =    57735.65   nrn =     
 193636101949

 ***********************************************************************************************************************

 dump no.   39 on file in.ir     nps =   388145118     coll =    11505102560     ctm =    59296.06   nrn =     
 198877115999

 ***********************************************************************************************************************

 dump no.   40 on file in.ir     nps =   398401130     coll =    11808986208     ctm =    60856.40   nrn =     
 204130136024
1problem summary                                                                                                           

      run terminated when   400000000  particle histories were done.
+                                                                                                    06/04/18 19:00:30 
      c TRIGA In-Core Foil Response Function Generator                                     probid =  06/04/18 17:30:05 

 neutron creation    tracks      weight        energy            neutron loss        tracks      weight        energy
                                 (per source particle)                                           (per source particle)

 source           400000000    1.0000E+00    5.6885E-01          escape           389476788    7.8969E-01    3.5725E-01
 nucl. interaction        0    0.            0.                  energy cutoff            0    0.            0.        
 particle decay           0    0.            0.                  time cutoff              0    0.            0.        
 weight window            0    0.            0.                  weight window            0    0.            0.        
 cell importance          0    0.            0.                  cell importance          0    0.            0.        
 weight cutoff            0    4.7292E-03    2.2589E-10          weight cutoff     10532095    4.7285E-03    2.6343E-10
 e or t importance        0    0.            0.                  e or t importance        0    0.            0.        
 dxtran                   0    0.            0.                  dxtran                   0    0.            0.        
 forced collisions        0    0.            0.                  forced collisions        0    0.            0.        
 exp. transform           0    0.            0.                  exp. transform           0    0.            0.        
 upscattering             0    0.            2.2565E-07          downscattering           0    0.            2.0389E-01
 photonuclear             0    0.            0.                  capture                  0    2.1033E-01    7.4285E-03
 (n,xn)               17763    4.2337E-05    7.8559E-05          loss to (n,xn)        8880    2.1165E-05    3.5305E-04
 prompt fission           0    0.            0.                  loss to fission          0    0.            0.        
 delayed fission          0    0.            0.                  nucl. interaction        0    0.            0.        
 prompt photofis          0    0.            0.                  particle decay           0    0.            0.        
 tabular boundary         0    0.            0.                  tabular boundary         0    0.            0.        
 tabular sampling         0    0.            0.                  elastic scatter          0    0.            0.        
     total        400017763    1.0048E+00    5.6893E-01              total        400017763    1.0048E+00    5.6893E-01

   number of neutrons banked                    8883        average time of (shakes)              cutoffs
   neutron tracks per source particle     1.0000E+00          escape            3.5837E+03          tco   1.0000E+33
   neutron collisions per source particle 2.9641E+01          capture           4.4012E+03          eco   0.0000E+00
   total neutron collisions              -2147483648          capture or escape 3.7557E+03          wc1  -5.0000E-01
   net multiplication              1.0000E+00 0.0000          any termination   3.7887E+03          wc2  -2.5000E-01

 computer time so far in this run 61102.24 minutes            maximum number ever in bank         2
 computer time in mcrun           61100.37 minutes            bank overflows to backup file       0
 source particles per minute            6.5466E+03
 random numbers generated             204950134182            most random numbers used was        8793 in history   202504689

 range of sampled source weights = 1.0000E+00 to 1.0000E+00

 number of histories processed by each thread
    15381868    15343721    15380949    15368691    15374470    15418111    15364761    15360590    15405965    15356746
    15390336    15394894    15380759    15367168    15391415    15379943    15335736    15403730    15394039    15419762
    15397057    15408823    15401362    15394152    15389828    15395124
1neutron  activity in each cell                                                                         print table 126

                       tracks     population   collisions   collisions     number        flux        average      average
              cell    entering                               * weight     weighted     weighted   track weight   track mfp
                                                          (per history)    energy       energy     (relative)      (cm)

        1       10      135562       134882         5033    1.2213E-05   1.4428E-03   6.7460E-01   9.9195E-01   3.5414E+00
        2       11     1516072      1382609       773110    1.5898E-03   5.5944E-04   6.0663E-01   9.7616E-01   3.0783E+00
        3       21    35395540     31511340          252    5.3899E-07   4.6471E-05   2.5200E-01   8.5083E-01   3.7551E+04
        4       22   116163661     67769493      8255982    1.7480E-02   4.6710E-05   2.5245E-01   8.4876E-01   3.9015E+00
        5       23   160681592     68475961           25    5.2735E-08   4.7076E-05   2.5323E-01   8.4520E-01   3.7617E+04
        6       24   223706657    106252672     32498274    6.7169E-02   4.6833E-05   2.5305E-01   8.4285E-01   3.1457E+00
        7       25   522119771    399781673  11814890905    2.3681E+01   2.8491E-05   1.9610E-01   8.2436E-01   7.8602E-01

           total    1059718855    675308630  11856423581    2.3767E+01

1tally        4        nps =   400000000
           tally type 4    track length estimate of particle flux.                             
           particle(s): neutrons 
           this tally is modified by   ft  scx

           volumes 
                   cell:      10                                                                                   
                         1.00000E-04
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.17314E-04 0.2253
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.83216E-04 0.1920
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.63614E-04 0.1704
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.40978E-04 0.1935
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.27506E-04 0.1648
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.53260E-04 0.1540
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.52490E-04 0.1845
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.17196E-04 0.2206
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.04906E-04 0.2377
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 7.85829E-05 0.3349
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 8.37933E-05 0.1835
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.33080E-04 0.1155
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 5.44780E-04 0.0650
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 7.77737E-04 0.0557
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.25162E-03 0.0421
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.41131E-03 0.0330
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.96672E-03 0.0294
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 9.48885E-03 0.0271
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.13451E-02 0.0275
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.23129E-02 0.0480
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.20484E-03 0.0678
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.72775E-03 0.0711
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.37451E-03 0.0712
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.91648E-03 0.0773
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.74171E-03 0.0681
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.13058E-03 0.0947
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.50128E-03 0.0751
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.15129E-03 0.0821
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.58345E-03 0.0763
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.66307E-03 0.0879
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.35519E-03 0.0912
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.12779E-03 0.0857
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.64748E-03 0.0911
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.07149E-03 0.0904
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.28185E-03 0.1038
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.99732E-03 0.1047
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.21250E-03 0.1020
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.47643E-03 0.1296
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.52129E-03 0.1309
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.00504E-03 0.1390
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 9.50262E-04 0.1516
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.08099E-03 0.1679
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 7.35294E-04 0.1724
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.14957E-04 0.2307
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 5.30199E-04 0.2398
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.29133E-04 0.2450
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.13329E-04 0.3372
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 2.48521E-04 0.2428
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.94497E-04 0.2870
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.90953E-04 0.2165
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.57554E-04 0.4472
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.02243E-04 0.3518
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.33322E-04 0.4060
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 4.94225E-05 0.4590
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 3.44152E-05 0.4352
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.25871E-05 0.4016
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1         102                                                                                   
                 1.05324E-01 0.0129
 
 cell  10                                                                                                                              
 multiplier bin:  -1.00000E+00         1           4                                                                                   
                 0.00000E+00 0.0000


 ===================================================================================================================================

           results of 10 statistical checks for the estimated answer for the tally fluctuation chart (tfc) bin of tally        4

 tfc bin     --mean--      ---------relative error---------      ----variance of the variance----      --figure of merit--     -pdf-
 behavior    behavior      value   decrease   decrease rate      value   decrease   decrease rate       value     behavior     slope

 desired      random       <0.10      yes      1/sqrt(nps)       <0.10      yes        1/nps           constant    random      >3.00
 observed     random        0.01      yes          yes            0.00      yes         yes            constant    random      10.00
 passed?        yes          yes      yes          yes             yes      yes         yes               yes        yes         yes

 ===================================================================================================================================


 this tally meets the statistical criteria used to form confidence intervals: check the tally fluctuation chart to verify.
 the results in other bins associated with this tally may not meet these statistical criteria.

 ----- estimated confidence intervals:  -----

 estimated asymmetric confidence interval(1,2,3 sigma): 1.0399E-01 to 1.0670E-01; 1.0263E-01 to 1.0806E-01; 1.0127E-01 to 1.0942E-01
 estimated  symmetric confidence interval(1,2,3 sigma): 1.0397E-01 to 1.0668E-01; 1.0261E-01 to 1.0804E-01; 1.0125E-01 to 1.0940E-01

1analysis of the results in the tally fluctuation chart bin (tfc) for tally        4 with nps =   400000000  print table 160


 normed average tally per history  = 1.05324E-01          unnormed average tally per history  = 1.05324E-05
 estimated tally relative error    = 0.0129               estimated variance of the variance  = 0.0018
 relative error from zero tallies  = 0.0027               relative error from nonzero scores  = 0.0126

 number of nonzero history tallies =      134876          efficiency for the nonzero tallies  = 0.0003
 history number of largest  tally  =   159285005          largest  unnormalized history tally = 5.58670E+00
 (largest  tally)/(average tally)  = 5.30429E+05          (largest  tally)/(avg nonzero tally)= 1.78855E+02

 (confidence interval shift)/mean  = 0.0002               shifted confidence interval center  = 1.05347E-01


 if the largest  history score sampled so far were to occur on the next history, the tfc bin quantities would change as follows:

      estimated quantities           value at nps           value at nps+1           value(nps+1)/value(nps)-1.

      mean                            1.05324E-01             1.05464E-01                     0.001326
      relative error                  1.28848E-02             1.29357E-02                     0.003951
      variance of the variance        1.75859E-03             1.83177E-03                     0.041614
      shifted center                  1.05347E-01             1.05347E-01                     0.000005
      figure of merit                 9.85834E-02             9.78090E-02                    -0.007855

 the estimated slope of the 200 largest  tallies starting at  1.67730E+00 appears to be decreasing at least exponentially.
 the large score tail of the empirical history score probability density function appears to have no unsampled regions.

 fom = (histories/minute)*(f(x) signal-to-noise ratio)**2 = (6.547E+03)*( 3.881E-03)**2 = (6.547E+03)*(1.506E-05) = 9.858E-02

1status of the statistical checks used to form confidence intervals for the mean for each tally bin


 tally   result of statistical checks for the tfc bin (the first check not passed is listed) and error magnitude check for all bins

        4   passed the 10 statistical checks for the tally fluctuation chart bin result               
         missed all bin error check:   114 tally bins had    57 bins with zeros and    34 bins with relative errors exceeding 0.10


 the 10 statistical checks are only for the tally fluctuation chart bin and do not apply to other tally bins.

 the tally bins with zeros may or may not be correct: compare the source, cutoffs, multipliers, et cetera with the tally bins.

 warning.       1 of the     1 tallies had bins with relative errors greater than recommended.
1tally fluctuation charts                              

                            tally        4
          nps      mean     error   vov  slope    fom
     32768000   1.0227E-01 0.0461 0.0260  3.5 9.4E-02
     65536000   1.0640E-01 0.0326 0.0118  4.3 9.4E-02
     98304000   1.0560E-01 0.0261 0.0073  6.6 9.8E-02
    131072000   1.0659E-01 0.0224 0.0055  9.3 9.9E-02
    163840000   1.0593E-01 0.0203 0.0050  9.1 9.7E-02
    196608000   1.0562E-01 0.0184 0.0040 10.0 9.8E-02
    229376000   1.0535E-01 0.0171 0.0034 10.0 9.8E-02
    262144000   1.0540E-01 0.0159 0.0028 10.0 9.9E-02
    294912000   1.0613E-01 0.0150 0.0024 10.0 9.8E-02
    327680000   1.0575E-01 0.0143 0.0021 10.0 9.8E-02
    360448000   1.0508E-01 0.0135 0.0019 10.0 9.9E-02
    393216000   1.0523E-01 0.0130 0.0017 10.0 9.9E-02
    400000000   1.0532E-01 0.0129 0.0018 10.0 9.9E-02

 ***********************************************************************************************************************

 dump no.   41 on file in.ir     nps =   400000000     coll =    11856423581     ctm =    61100.37   nrn =     
 204950134182

         8 warning messages so far.


 run terminated when   400000000  particle histories were done.

 computer time =61102.24 minutes

 mcnp     version 6     05/08/13                     06/04/18 19:00:30                     probid =  06/04/18 17:30:05 
