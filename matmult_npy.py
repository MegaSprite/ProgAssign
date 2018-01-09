#! /usr/bin/python

import csv
import numpy as np
import time
import sys                                                      # import 'sys' module to access the
                                                                # list of command line arguments

def utime_now():
    return int(time.time() * 1E6)

filename, rowA, colA, rowB, colB = sys.argv

if rowA.isdigit() == 0 or colA.isdigit() == 0 or rowB.isdigit() == 0 or colB.isdigit() == 0 \
        or int(rowA) == 0 or int(colA) == 0 or int(rowB) == 0 or int(colB) == 0: # Check the validity of the inputs
    sys.stderr.write('ERROR: expected two non-negative integer arguments\n')
elif int(colA) != int(rowB):
    sys.stderr.write('ERROR: the two matrices are not compatible\n')
else:
    rowA = int(rowA)
    colA = int(colA)
    rowB = int(rowB)
    colB = int(colB)

    with open('A.csv', 'rb') as a:
        readerA = list(csv.reader(a))

    with open('B.csv', 'rb') as b:
        readerB = list(csv.reader(b))

    if len(readerA) < rowA or len(readerB) < rowB or len(readerA[0]) < colA or len(readerB[0]) < colB:
        sys.stderr.write('ERROR: The row/col numbers entered are too large\n')

    else:
        matA = [[] for m in range(rowA)]
        matB = [[] for m in range(rowB)]
        for i in range(0, rowA):
            for j in range(0, colA):
                matA[i].append(float(readerA[i][j]))

        for i in range(0, rowB):
            for j in range(0, colB):
                matB[i].append(float(readerB[i][j]))

        matA = np.matrix(matA,dtype=float)
        matB = np.matrix(matB,dtype=float)

        beginTime = utime_now()
        matC = np.dot(matA,matB)
        endTime = utime_now()

        print "\nTime elapsed running matrix multiplication is %ld microseconds\n" % (endTime - beginTime)

        f = open('C.csv','w')

        for entry in matC.tolist():
             f.write(', '.join(map(str,entry))+'\n')

        f.close()