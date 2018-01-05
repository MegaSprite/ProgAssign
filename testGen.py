#! ~/Rob550/venv/bin/python

import numpy as np
import sys

filename, row, col = sys.argv
if row.isdigit() == 0 or col.isdigit() == 0:
    sys.stderr.write('ERROR: expected two integer arguments')
else:
    row = int(row)
    col = int(col)
    m = np.random.randn(row,col)
    M = '\n'.join((','.join(str(a) for a in b)) for b in m)
print M