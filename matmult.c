#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <sys/time.h>

double* readMatrixFromFile(char*, int, int); 
int writeMatrixToFile(char*, double*, int, int);
void copy(double [], double [], long int);
double* multmat(double [], double [],int, int, int, int);
int64_t utime_now (void);

int main(int argc, char* argv[]){
    
    int rowA, colA, rowB, colB;
    
    rowA=colA=rowB=colB=0;

    if (((rowA =atoi(argv[1])) > 0) && ((colA=atoi(argv[2])) > 0) &&\
     ((rowB=atoi(argv[3])) > 0) && ((colB=atoi(argv[4])) > 0)){
         if (colA == rowB){
             ;
         }
         else
         {
            printf("The two matrices are not compatible\n");
            return -1;
         }

     }
     else {
         printf("Plz input non-zero positive integers\n");
         return -1;
     }
    
    double matA[rowA*colA], matB[rowB*colB], matC[rowA*colB];

    copy(matA,readMatrixFromFile("A.csv",rowA,colA),rowA*colA);
    copy(matB,readMatrixFromFile("B.csv",rowB,colB),rowB*colB);

    copy(matC, multmat(matA, matB, rowA, colA, rowB, colB),rowA*colB);
    
    /* Timing*/
    int64_t begintime, endtime;
    begintime = utime_now();
    multmat(matA, matB, rowA, colA, rowB, colB);        // for timing purposes, functionally redundant
    endtime = utime_now();

    printf("Time elapsed running matrix multiplication is %ld microseconds\n", endtime - begintime);

    return writeMatrixToFile("C.csv", matC, rowA, colB);
}



/**
 * Allocates a matrix which must be free'd by the calling code.
 * i.e. free()
 */
double* readMatrixFromFile(char* fileName, int height, int width) {
  FILE* fp = fopen(fileName, "r");
  if (fp == NULL) {
    fprintf(stderr, "Can't open %s.\n", fileName);
    return NULL ;
  }
  double val;
  double* M = (double*) malloc(height * width * sizeof(double));
  for(int i = 0; i < height; i++) {
    for(int j = 0; j < width; j++) {
      if (fscanf(fp, " %lf", &val) != 1) {
        fprintf(stderr, "Couldn't read value.\n");
        return NULL;
      }
      // Discard the comma without checking.
      fgetc(fp);
      M[i * width + j] = val;
    }
  }
  fclose(fp);
  return M;
}

int writeMatrixToFile(char* fileName, double* matrix, int height, int width) {
  FILE* fp = fopen(fileName, "w");
  if (fp == NULL) {
    return 1;
  }
 
  for (int i = 0; i < height; i++) {
    for (int j = 0; j < width; j++) {
      if (j > 0) {
        fputc(',', fp);
      }
      fprintf(fp, "%lf", matrix[i*width +j]);
    }
    fputs("\r\n", fp);
  }
  fclose(fp);
  return 0;
}

/*copy contents of one array to the other*/
void copy(double to[], double from[], long int len )
{
    int i;

    for (i=0;i<len;++i){
        to[i]=from[i];
    }
}

double* multmat(double matA[], double matB[],int rowA, int colA, int rowB, int colB)
{
    int i, j;
    double val;
    double* M = (double*) malloc(rowA * colB * sizeof(double));
    for(int i = 0; i < rowA; i++) {
        for(int j = 0; j < colB; j++) {
            val = 0.0;

            int n;

            for (n = 0;n<colA;n++){
                val = val + (matA[i*colA+n])*(matB[n*rowB+j]);
            }
        M[i * colB + j] = val;
        }
    }
    return M;

}

int64_t utime_now (void){
    struct timeval tv;
    gettimeofday (&tv, NULL);
    return (int64_t) tv.tv_sec * 1000000 + tv.tv_usec;
}