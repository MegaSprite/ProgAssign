#! /usr/bin/python

import csv
import numpy as np
import time
import sys                                                      # import 'sys' module to access the
                                                                # list of command line arguments
filename, rowA, colA, rowB, colB = sys.argv

def utime_now():
    return int(time.time() * 1E6)

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
        readerA = csv.reader(a)
        matA = list(readerA)

    with open('B.csv', 'rb') as b:
        readerB = csv.reader(b)
        matB = list(readerB)

    if len(matA) < rowA or len(matB) < rowB or len(matA[0]) < colA or len(matB[0]) < colB:
        sys.stderr.write('ERROR: The row/col numbers entered are too large\n')

    else:

        for i in range(0, rowA):
            for j in range(0, colA):
                matA[i][j] = float(matA[i][j])
        for i in range(0, rowB):
            for j in range(0, colB):
                matB[i][j] = float(matB[i][j])

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

        # print out just for easier reference

        print "Print out the multiplication result just for easier reference:"
        for entry in matC.tolist():
            print ', '.join(map(str,entry))