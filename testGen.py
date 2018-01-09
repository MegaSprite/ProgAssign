#! /usr/bin/python

import numpy as np                                              # import 'numpy' pkg
import sys                                                      # import 'sys' module to access the
                                                                # list of command line arguments
filename, row, col = sys.argv
if row.isdigit() == 0 or col.isdigit() == 0 or int(row)<=0 or int(col)<=0:# Check the validity of the inputs
    sys.stderr.write('ERROR: expected two positive integer arguments\n')
else:
    row = int(row)
    col = int(col)
    matrix = np.random.standard_normal(size = (row,col))

    for entry in matrix:
        print ', '.join(map(str,entry))