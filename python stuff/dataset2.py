Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

==== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ====
     Kind Atom name Amino acid name    a  ... relative place     b   Atom   
0    ATOM         1               N  THR  ...         83.115  1.00  25.58  N
1    ATOM         2              CA  THR  ...         82.771  1.00  25.58  C
2    ATOM         3               C  THR  ...         82.647  1.00  25.58  C
3    ATOM         4               O  THR  ...         83.646  1.00  25.58  O
4    ATOM         5              CB  THR  ...         83.817  1.00  25.58  C
..    ...       ...             ...  ...  ...            ...   ...    ... ..
148  ATOM     41505              HE  ARG  ...         85.777  1.00   0.00  H
149  ATOM     41506            HH11  ARG  ...         86.835  1.00   0.00  H
150  ATOM     41507            HH12  ARG  ...         85.822  1.00   0.00  H
151  ATOM     41508            HH21  ARG  ...         87.560  1.00   0.00  H
152  ATOM     41509            HH22  ARG  ...         87.110  1.00   0.00  H

[153 rows x 12 columns]

==== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ====
     Kind        Atom name Amino acid name  ...       z relative place      b Atom
0    ATOM      1         N             THR  ...  83.115           1.00  25.58    N
1    ATOM      2        CA             THR  ...  82.771           1.00  25.58    C
2    ATOM      3         C             THR  ...  82.647           1.00  25.58    C
3    ATOM      4         O             THR  ...  83.646           1.00  25.58    O
4    ATOM      5        CB             THR  ...  83.817           1.00  25.58    C
..    ...    ...       ...             ...  ...     ...            ...    ...  ...
148  ATOM  41505        HE             ARG  ...  85.777           1.00   0.00    H
149  ATOM  41506      HH11             ARG  ...  86.835           1.00   0.00    H
150  ATOM  41507      HH12             ARG  ...  85.822           1.00   0.00    H
151  ATOM  41508      HH21             ARG  ...  87.560           1.00   0.00    H
152  ATOM  41509      HH22             ARG  ...  87.110           1.00   0.00    H

[153 rows x 12 columns]

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
     Kind        Atom name Amino acid name  ...       z relative place        Atom
0    ATOM      1         N             THR  ...  83.115           1.00  25.58    N
1    ATOM      2        CA             THR  ...  82.771           1.00  25.58    C
2    ATOM      3         C             THR  ...  82.647           1.00  25.58    C
3    ATOM      4         O             THR  ...  83.646           1.00  25.58    O
4    ATOM      5        CB             THR  ...  83.817           1.00  25.58    C
..    ...    ...       ...             ...  ...     ...            ...    ...  ...
148  ATOM  41505        HE             ARG  ...  85.777           1.00   0.00    H
149  ATOM  41506      HH11             ARG  ...  86.835           1.00   0.00    H
150  ATOM  41507      HH12             ARG  ...  85.822           1.00   0.00    H
151  ATOM  41508      HH21             ARG  ...  87.560           1.00   0.00    H
152  ATOM  41509      HH22             ARG  ...  87.110           1.00   0.00    H

[153 rows x 12 columns]

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 17, in <module>
    new_database=pd.DataFrame(my_database['Amino acid name'==THR,'x','y','z'])
NameError: name 'THR' is not defined

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:\Users\noamu\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3621, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas\_libs\index.pyx", line 136, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 160, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\index.pyx", line 201, in pandas._libs.index.IndexEngine._get_loc_duplicates
  File "pandas\_libs\index.pyx", line 209, in pandas._libs.index.IndexEngine._maybe_get_bool_indexer
  File "pandas\_libs\index.pyx", line 107, in pandas._libs.index._unpack_bool_indexer
KeyError: (False, 'x', 'y', 'z')

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 17, in <module>
    new_database=pd.DataFrame(my_database['Amino acid name'=='THR','x','y','z'])
  File "C:\Users\noamu\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\frame.py", line 3505, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\noamu\AppData\Local\Programs\Python\Python310\lib\site-packages\pandas\core\indexes\base.py", line 3623, in get_loc
    raise KeyError(key) from err
KeyError: (False, 'x', 'y', 'z')

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
    Amino acid name        x        y       z
0               THR  134.446  145.572  83.115
1               THR  133.075  145.924  82.771
2               THR  132.933  147.438  82.647
3               THR  132.901  148.151  83.646
4               THR  132.072  145.397  83.817
..              ...      ...      ...     ...
148             ARG  129.546  148.041  85.777
149             ARG  126.981  150.955  86.835
150             ARG  128.349  151.362  85.822
151             ARG  126.681  148.820  87.560
152             ARG  127.817  147.568  87.110

[153 rows x 4 columns]

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
    Amino acid name        x        y       z
0               THR  134.446  145.572  83.115
1               THR  133.075  145.924  82.771
2               THR  132.933  147.438  82.647
3               THR  132.901  148.151  83.646
4               THR  132.072  145.397  83.817
..              ...      ...      ...     ...
148             ARG  129.546  148.041  85.777
149             ARG  126.981  150.955  86.835
150             ARG  128.349  151.362  85.822
151             ARG  126.681  148.820  87.560
152             ARG  127.817  147.568  87.110

[153 rows x 4 columns]

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
0       True
1       True
2       True
3       True
4       True
       ...  
148    False
149    False
150    False
151    False
152    False
Name: Amino acid name, Length: 153, dtype: bool

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
   Amino acid name        x        y       z
0              THR  134.446  145.572  83.115
1              THR  133.075  145.924  82.771
2              THR  132.933  147.438  82.647
3              THR  132.901  148.151  83.646
4              THR  132.072  145.397  83.817
5              THR  132.308  144.005  84.053
6              THR  130.648  145.573  83.321
7              THR  132.835  145.475  81.807
8              THR  132.200  145.948  84.749
9              THR  132.910  143.903  84.794
10             THR  135.074  145.932  82.410
11             THR  134.534  144.567  83.162
12             THR  134.681  145.972  84.012
13             THR  129.952  145.196  84.071
14             THR  130.516  145.018  82.392
15             THR  130.453  146.631  83.144
84             THR  129.966  143.678  88.842
85             THR  129.749  144.303  87.547
86             THR  130.284  145.727  87.481
87             THR  130.185  146.361  86.428
88             THR  128.255  144.303  87.199
89             THR  127.556  145.205  88.065
90             THR  127.671  142.913  87.352
91             THR  129.350  143.922  89.605
92             THR  130.271  143.711  86.795
93             THR  128.130  144.631  86.167
94             THR  127.675  144.930  88.977
95             THR  126.611  142.934  87.101
96             THR  127.793  142.579  88.382
97             THR  128.189  142.226  86.683

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 10, in <module>
    text=file.name
AttributeError: 'list' object has no attribute 'name'

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 10, in <module>
    text=os.path.basename('A_THR_13_5Angs_noHOH.pdb')
NameError: name 'os' is not defined

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 10, in <module>
    text=file.path.basename('A_THR_13_5Angs_noHOH.pdb')
AttributeError: 'list' object has no attribute 'path'

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
['ATOM      1  N   THR A  13     134.446 145.572  83.115  1.00 25.58           N  \n', 'ATOM      2  CA  THR A  13     133.075 145.924  82.771  1.00 25.58           C  \n', 'ATOM      3  C   THR A  13     132.933 147.438  82.647  1.00 25.58           C  \n', 'ATOM      4  O   THR A  13     132.901 148.151  83.646  1.00 25.58           O  \n', 'ATOM      5  CB  THR A  13     132.072 145.397  83.817  1.00 25.58           C  \n', 'ATOM      6  OG1 THR A  13     132.308 144.005  84.053  1.00 25.58           O  \n', 'ATOM      7  CG2 THR A  13     130.648 145.573  83.321  1.00 25.58           C  \n', 'ATOM      8  HA  THR A  13     132.835 145.475  81.807  1.00  0.00           H  \n', 'ATOM      9  HB  THR A  13     132.200 145.948  84.749  1.00  0.00           H  \n', 'ATOM     10  HG1 THR A  13     132.910 143.903  84.794  1.00  0.00           H  \n', 'ATOM     11  H1  THR A  13     135.074 145.932  82.410  1.00  0.00           H  \n', 'ATOM     12  H2  THR A  13     134.534 144.567  83.162  1.00  0.00           H  \n', 'ATOM     13  H3  THR A  13     134.681 145.972  84.012  1.00  0.00           H  \n', 'ATOM     14 HG21 THR A  13     129.952 145.196  84.071  1.00  0.00           H  \n', 'ATOM     15 HG22 THR A  13     130.516 145.018  82.392  1.00  0.00           H  \n', 'ATOM     16 HG23 THR A  13     130.453 146.631  83.144  1.00  0.00           H  \n', 'ATOM     17  N   VAL A  14     132.854 147.922  81.409  1.00 25.72           N  \n', 'ATOM     18  CA  VAL A  14     132.748 149.344  81.116  1.00 25.72           C  \n', 'ATOM     19  C   VAL A  14     131.575 149.559  80.170  1.00 25.72           C  \n', 'ATOM     20  O   VAL A  14     131.076 148.630  79.538  1.00 25.72           O  \n', 'ATOM     21  CB  VAL A  14     134.044 149.923  80.512  1.00 25.72           C  \n', 'ATOM     22  CG1 VAL A  14     135.201 149.769  81.483  1.00 25.72           C  \n', 'ATOM     23  CG2 VAL A  14     134.357 149.259  79.185  1.00 25.72           C  \n', 'ATOM     24  H   VAL A  14     132.868 147.272  80.636  1.00  0.00           H  \n', 'ATOM     25  HA  VAL A  14     132.539 149.871  82.047  1.00  0.00           H  \n', 'ATOM     26  HB  VAL A  14     133.890 150.987  80.332  1.00  0.00           H  \n', 'ATOM     27 HG11 VAL A  14     134.951 150.254  82.427  1.00  0.00           H  \n', 'ATOM     28 HG12 VAL A  14     135.390 148.710  81.658  1.00  0.00           H  \n', 'ATOM     29 HG13 VAL A  14     136.093 150.232  81.062  1.00  0.00           H  \n', 'ATOM     30 HG21 VAL A  14     133.512 149.384  78.508  1.00  0.00           H  \n', 'ATOM     31 HG22 VAL A  14     134.540 148.196  79.345  1.00  0.00           H  \n', 'ATOM     32 HG23 VAL A  14     135.244 149.719  78.749  1.00  0.00           H  \n', 'ATOM    121  N   LEU A  21     126.550 147.137  79.101  1.00 28.25           N  \n', 'ATOM    122  CA  LEU A  21     127.677 146.458  79.737  1.00 28.25           C  \n', 'ATOM    123  C   LEU A  21     127.848 145.106  79.048  1.00 28.25           C  \n', 'ATOM    124  O   LEU A  21     127.123 144.148  79.343  1.00 28.25           O  \n', 'ATOM    125  CB  LEU A  21     127.451 146.310  81.237  1.00 28.25           C  \n', 'ATOM    126  CG  LEU A  21     127.293 147.604  82.040  1.00 28.25           C  \n', 'ATOM    127  CD1 LEU A  21     126.898 147.300  83.471  1.00 28.25           C  \n', 'ATOM    128  CD2 LEU A  21     128.574 148.415  82.006  1.00 28.25           C  \n', 'ATOM    129  H   LEU A  21     125.619 146.788  79.277  1.00  0.00           H  \n', 'ATOM    130  HA  LEU A  21     128.578 147.049  79.576  1.00  0.00           H  \n', 'ATOM    131  HB2 LEU A  21     128.304 145.769  81.647  1.00  0.00           H  \n', 'ATOM    132  HB3 LEU A  21     126.558 145.704  81.389  1.00  0.00           H  \n', 'ATOM    133  HG  LEU A  21     126.500 148.196  81.584  1.00  0.00           H  \n', 'ATOM    134 HD11 LEU A  21     125.977 146.717  83.478  1.00  0.00           H  \n', 'ATOM    135 HD12 LEU A  21     126.741 148.234  84.011  1.00  0.00           H  \n', 'ATOM    136 HD13 LEU A  21     127.692 146.730  83.954  1.00  0.00           H  \n', 'ATOM    137 HD21 LEU A  21     128.844 148.625  80.971  1.00  0.00           H  \n', 'ATOM    138 HD22 LEU A  21     129.375 147.849  82.483  1.00  0.00           H  \n', 'ATOM    139 HD23 LEU A  21     128.424 149.353  82.540  1.00  0.00           H  \n', 'ATOM    160  N   GLN A  23     130.154 142.803  79.173  1.00 26.57           N  \n', 'ATOM    161  CA  GLN A  23     130.489 141.670  80.026  1.00 26.57           C  \n', 'ATOM    162  C   GLN A  23     129.252 141.104  80.706  1.00 26.57           C  \n', 'ATOM    163  O   GLN A  23     129.130 139.884  80.861  1.00 26.57           O  \n', 'ATOM    164  CB  GLN A  23     131.532 142.076  81.065  1.00 26.57           C  \n', 'ATOM    165  CG  GLN A  23     132.954 142.048  80.542  1.00 26.57           C  \n', 'ATOM    166  CD  GLN A  23     133.404 140.656  80.159  1.00 26.57           C  \n', 'ATOM    167  OE1 GLN A  23     133.410 139.746  80.984  1.00 26.57           O  \n', 'ATOM    168  NE2 GLN A  23     133.781 140.482  78.901  1.00 26.57           N  \n', 'ATOM    169  H   GLN A  23     130.522 143.720  79.381  1.00  0.00           H  \n', 'ATOM    170  HA  GLN A  23     130.920 140.889  79.400  1.00  0.00           H  \n', 'ATOM    171  HB2 GLN A  23     131.462 141.390  81.909  1.00  0.00           H  \n', 'ATOM    172  HB3 GLN A  23     131.306 143.084  81.413  1.00  0.00           H  \n', 'ATOM    173  HG2 GLN A  23     133.619 142.429  81.317  1.00  0.00           H  \n', 'ATOM    174  HG3 GLN A  23     133.022 142.695  79.668  1.00  0.00           H  \n', 'ATOM    175 HE21 GLN A  23     133.759 141.258  78.255  1.00  0.00           H  \n', 'ATOM    176 HE22 GLN A  23     134.090 139.573  78.588  1.00  0.00           H  \n', 'ATOM    177  N   VAL A  24     128.317 141.967  81.102  1.00 27.38           N  \n', 'ATOM    178  CA  VAL A  24     127.074 141.489  81.693  1.00 27.38           C  \n', 'ATOM    179  C   VAL A  24     126.215 140.790  80.644  1.00 27.38           C  \n', 'ATOM    180  O   VAL A  24     125.581 139.767  80.927  1.00 27.38           O  \n', 'ATOM    181  CB  VAL A  24     126.330 142.652  82.373  1.00 27.38           C  \n', 'ATOM    182  CG1 VAL A  24     125.049 142.160  83.010  1.00 27.38           C  \n', 'ATOM    183  CG2 VAL A  24     127.220 143.304  83.411  1.00 27.38           C  \n', 'ATOM    184  H   VAL A  24     128.471 142.959  80.992  1.00  0.00           H  \n', 'ATOM    185  HA  VAL A  24     127.327 140.758  82.461  1.00  0.00           H  \n', 'ATOM    186  HB  VAL A  24     126.079 143.394  81.615  1.00  0.00           H  \n', 'ATOM    187 HG11 VAL A  24     124.421 141.694  82.251  1.00  0.00           H  \n', 'ATOM    188 HG12 VAL A  24     125.285 141.430  83.784  1.00  0.00           H  \n', 'ATOM    189 HG13 VAL A  24     124.518 143.002  83.455  1.00  0.00           H  \n', 'ATOM    190 HG21 VAL A  24     128.137 143.652  82.937  1.00  0.00           H  \n', 'ATOM    191 HG22 VAL A  24     127.465 142.578  84.186  1.00  0.00           H  \n', 'ATOM    192 HG23 VAL A  24     126.698 144.150  83.857  1.00  0.00           H  \n', 'ATOM   1768  N   THR A 124     129.966 143.678  88.842  1.00 20.34           N  \n', 'ATOM   1769  CA  THR A 124     129.749 144.303  87.547  1.00 20.34           C  \n', 'ATOM   1770  C   THR A 124     130.284 145.727  87.481  1.00 20.34           C  \n', 'ATOM   1771  O   THR A 124     130.185 146.361  86.428  1.00 20.34           O  \n', 'ATOM   1772  CB  THR A 124     128.255 144.303  87.199  1.00 20.34           C  \n', 'ATOM   1773  OG1 THR A 124     127.556 145.205  88.065  1.00 20.34           O  \n', 'ATOM   1774  CG2 THR A 124     127.671 142.913  87.352  1.00 20.34           C  \n', 'ATOM   1775  H   THR A 124     129.350 143.922  89.605  1.00  0.00           H  \n', 'ATOM   1776  HA  THR A 124     130.271 143.711  86.795  1.00  0.00           H  \n', 'ATOM   1777  HB  THR A 124     128.130 144.631  86.167  1.00  0.00           H  \n', 'ATOM   1778  HG1 THR A 124     127.675 144.930  88.977  1.00  0.00           H  \n', 'ATOM   1779 HG21 THR A 124     126.611 142.934  87.101  1.00  0.00           H  \n', 'ATOM   1780 HG22 THR A 124     127.793 142.579  88.382  1.00  0.00           H  \n', 'ATOM   1781 HG23 THR A 124     128.189 142.226  86.683  1.00  0.00           H  \n', 'ATOM   1782  N   GLN A 125     130.849 146.242  88.567  1.00 21.67           N  \n', 'ATOM   1783  CA  GLN A 125     131.281 147.629  88.616  1.00 21.67           C  \n', 'ATOM   1784  C   GLN A 125     132.771 147.813  88.853  1.00 21.67           C  \n', 'ATOM   1785  O   GLN A 125     133.383 148.646  88.184  1.00 21.67           O  \n', 'ATOM   1786  CB  GLN A 125     130.508 148.389  89.703  1.00 21.67           C  \n', 'ATOM   1787  CG  GLN A 125     130.773 149.881  89.711  1.00 21.67           C  \n', 'ATOM   1788  CD  GLN A 125     129.621 150.674  90.285  1.00 21.67           C  \n', 'ATOM   1789  OE1 GLN A 125     128.868 150.179  91.117  1.00 21.67           O  \n', 'ATOM   1790  NE2 GLN A 125     129.482 151.916  89.845  1.00 21.67           N  \n', 'ATOM   1791  H   GLN A 125     130.982 145.656  89.379  1.00  0.00           H  \n', 'ATOM   1792  HA  GLN A 125     131.039 148.086  87.656  1.00  0.00           H  \n', 'ATOM   1793  HB2 GLN A 125     129.442 148.230  89.541  1.00  0.00           H  \n', 'ATOM   1794  HB3 GLN A 125     130.779 147.980  90.676  1.00  0.00           H  \n', 'ATOM   1795  HG2 GLN A 125     130.947 150.210  88.686  1.00  0.00           H  \n', 'ATOM   1796  HG3 GLN A 125     131.667 150.078  90.302  1.00  0.00           H  \n', 'ATOM   1797 HE21 GLN A 125     130.127 152.284  89.160  1.00  0.00           H  \n', 'ATOM   1798 HE22 GLN A 125     128.731 152.494  90.194  1.00  0.00           H  \n', 'ATOM   1874  N   PRO A 131     131.808 139.340  86.240  1.00 21.20           N  \n', 'ATOM   1875  CA  PRO A 131     130.507 139.070  86.860  1.00 21.20           C  \n', 'ATOM   1876  C   PRO A 131     130.210 137.578  86.941  1.00 21.20           C  \n', 'ATOM   1877  O   PRO A 131     130.758 136.762  86.198  1.00 21.20           O  \n', 'ATOM   1878  CB  PRO A 131     129.515 139.789  85.937  1.00 21.20           C  \n', 'ATOM   1879  CG  PRO A 131     130.235 139.976  84.659  1.00 21.20           C  \n', 'ATOM   1880  CD  PRO A 131     131.681 140.110  84.993  1.00 21.20           C  \n', 'ATOM   1881  HA  PRO A 131     130.472 139.510  87.857  1.00  0.00           H  \n', 'ATOM   1882  HB2 PRO A 131     129.231 140.753  86.359  1.00  0.00           H  \n', 'ATOM   1883  HB3 PRO A 131     128.630 139.171  85.783  1.00  0.00           H  \n', 'ATOM   1884  HG2 PRO A 131     129.881 140.877  84.158  1.00  0.00           H  \n', 'ATOM   1885  HG3 PRO A 131     130.081 139.109  84.016  1.00  0.00           H  \n', 'ATOM   1886  HD2 PRO A 131     132.305 139.686  84.206  1.00  0.00           H  \n', 'ATOM   1887  HD3 PRO A 131     131.938 141.156  85.162  1.00  0.00           H  \n', 'ATOM  41486  N   ARG M 130     133.686 151.756  87.136  1.00 21.50           N  \n', 'ATOM  41487  CA  ARG M 130     132.883 152.467  86.163  1.00 21.50           C  \n', 'ATOM  41488  C   ARG M 130     131.872 153.361  86.872  1.00 21.50           C  \n', 'ATOM  41489  O   ARG M 130     131.500 153.098  88.017  1.00 21.50           O  \n', 'ATOM  41490  CB  ARG M 130     132.145 151.490  85.243  1.00 21.50           C  \n', 'ATOM  41491  CG  ARG M 130     131.162 150.601  85.966  1.00 21.50           C  \n', 'ATOM  41492  CD  ARG M 130     130.213 149.910  85.019  1.00 21.50           C  \n', 'ATOM  41493  NE  ARG M 130     129.317 149.024  85.750  1.00 21.50           N  \n', 'ATOM  41494  CZ  ARG M 130     128.222 149.420  86.381  1.00 21.50           C  \n', 'ATOM  41495  NH1 ARG M 130     127.819 150.678  86.343  1.00 21.50           N  \n', 'ATOM  41496  NH2 ARG M 130     127.517 148.532  87.072  1.00 21.50           N  \n', 'ATOM  41497  H   ARG M 130     133.305 150.936  87.586  1.00  0.00           H  \n', 'ATOM  41498  HA  ARG M 130     133.539 153.092  85.557  1.00  0.00           H  \n', 'ATOM  41499  HB2 ARG M 130     131.602 152.066  84.494  1.00  0.00           H  \n', 'ATOM  41500  HB3 ARG M 130     132.879 150.862  84.737  1.00  0.00           H  \n', 'ATOM  41501  HG2 ARG M 130     130.583 151.210  86.660  1.00  0.00           H  \n', 'ATOM  41502  HG3 ARG M 130     131.713 149.848  86.529  1.00  0.00           H  \n', 'ATOM  41503  HD2 ARG M 130     129.624 150.660  84.491  1.00  0.00           H  \n', 'ATOM  41504  HD3 ARG M 130     130.785 149.328  84.297  1.00  0.00           H  \n', 'ATOM  41505  HE  ARG M 130     129.546 148.041  85.777  1.00  0.00           H  \n', 'ATOM  41506 HH11 ARG M 130     126.981 150.955  86.835  1.00  0.00           H  \n', 'ATOM  41507 HH12 ARG M 130     128.349 151.362  85.822  1.00  0.00           H  \n', 'ATOM  41508 HH21 ARG M 130     126.681 148.820  87.560  1.00  0.00           H  \n', 'ATOM  41509 HH22 ARG M 130     127.817 147.568  87.110  1.00  0.00           H  \n']

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
['A', 'THR', '13', '5Angs', 'noHOH.pdb']

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
['A', 'THR', '13', '5Angs', 'noHOH.pdb']

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
Traceback (most recent call last):
  File "C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py", line 11, in <module>
    amino_acid_name=text_name.split(0,'_')
TypeError: 'str' object cannot be interpreted as an integer

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
THR

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
THR
   Amino acid name        x        y       z
0              THR  134.446  145.572  83.115
1              THR  133.075  145.924  82.771
2              THR  132.933  147.438  82.647
3              THR  132.901  148.151  83.646
4              THR  132.072  145.397  83.817
5              THR  132.308  144.005  84.053
6              THR  130.648  145.573  83.321
7              THR  132.835  145.475  81.807
8              THR  132.200  145.948  84.749
9              THR  132.910  143.903  84.794
10             THR  135.074  145.932  82.410
11             THR  134.534  144.567  83.162
12             THR  134.681  145.972  84.012
13             THR  129.952  145.196  84.071
14             THR  130.516  145.018  82.392
15             THR  130.453  146.631  83.144
84             THR  129.966  143.678  88.842
85             THR  129.749  144.303  87.547
86             THR  130.284  145.727  87.481
87             THR  130.185  146.361  86.428
88             THR  128.255  144.303  87.199
89             THR  127.556  145.205  88.065
90             THR  127.671  142.913  87.352
91             THR  129.350  143.922  89.605
92             THR  130.271  143.711  86.795
93             THR  128.130  144.631  86.167
94             THR  127.675  144.930  88.977
95             THR  126.611  142.934  87.101
96             THR  127.793  142.579  88.382
97             THR  128.189  142.226  86.683

======================================================== RESTART: C:/Users/noamu/OneDrive/שולחן העבודה/python stuff/dataset1.py ========================================================
THR
   Amino acid name        x        y       z
0              THR  134.446  145.572  83.115
1              THR  133.075  145.924  82.771
2              THR  132.933  147.438  82.647
3              THR  132.901  148.151  83.646
4              THR  132.072  145.397  83.817
5              THR  132.308  144.005  84.053
6              THR  130.648  145.573  83.321
7              THR  132.835  145.475  81.807
8              THR  132.200  145.948  84.749
9              THR  132.910  143.903  84.794
10             THR  135.074  145.932  82.410
11             THR  134.534  144.567  83.162
12             THR  134.681  145.972  84.012
13             THR  129.952  145.196  84.071
14             THR  130.516  145.018  82.392
15             THR  130.453  146.631  83.144
84             THR  129.966  143.678  88.842
85             THR  129.749  144.303  87.547
86             THR  130.284  145.727  87.481
87             THR  130.185  146.361  86.428
88             THR  128.255  144.303  87.199
89             THR  127.556  145.205  88.065
90             THR  127.671  142.913  87.352
91             THR  129.350  143.922  89.605
92             THR  130.271  143.711  86.795
93             THR  128.130  144.631  86.167
94             THR  127.675  144.930  88.977
95             THR  126.611  142.934  87.101
96             THR  127.793  142.579  88.382
97             THR  128.189  142.226  86.683
