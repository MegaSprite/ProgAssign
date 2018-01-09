# R550_01_ProgAssign
A and B are 10x10 matrices
Program				Time consumption (microseconds)
matmult.c				13
matmult_pure.py				442
matmult_npy.py				34

A and B are 100x100 matrices
Program				Time consumption (microseconds)
matmult.c				5,343
matmult_pure.py				302,667
matmult_npy.py				388

A and B are 1000x1000 matrices
Program				Time consumption (microseconds)
matmult.c				6,706,348
matmult_pure.py				394,940,210
matmult_npy.py				223,056

Comments: I used "term-by-term for loop" for matrix multiplication for both matmult.c and matmult_pure.py. Apparently, the program in C implements the task much faster. However, with the help of python libraries and modules like numpy that are created by some extraodinary programmers, python programs can still be superior to the little program I wrote, especially when it comes to large datasets.
