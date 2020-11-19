#include <string.h>
#include <stdio.h>

int isShuffleOf(char x[], char y[], char z[]) {
    //NOT FINISHED
    if(strlen(x)+strlen(y) != strlen(z)) {
        return 0;
    }
    int A[strlen(x)+1][strlen(y)+1] = {0};
    int i,j = 0;
    A[i++][j++] = 1;
    //printf("%d\n", A[0][0]);

    //setup inital conditions
    while(x[i-1] != '\0') {
        if(x[i-1] == z[i-1]) {
            A[i][0] = A[i-1][0];
        } else {
            A[i][0] = 0;
        }
        i++;
    }
    while(y[j-1] != '\0') {
        if(y[j-1] == z[j-1]) {
            A[0][j] = A[0][j-1];
        } else {
            A[0][j] = 0;
        }
        j++;
    }
    printf("%d\n", A[1][0]);
    /*for(i = 0; i < strlen(x)+1; i++){
        for(j = 0; j < strlen(y)+1; j++) {
            printf("%d\n", A[i][j]);
        }
    }*/

    for(i = 1; i < strlen(x)+1; i++){
        for(j = 1; j < strlen(y)+1; j++) {
            if(x[i-1] == z[i+j-1]) {
                A[i][j] = A[i-1][j];
            } else if (y[j-1] == z[i+j-1]) {
                A[i][j] = A[i][j-1];
            } else if (x[i-1] == z[i+j-1] || y[j] == z[i+j-1]) {
                A[i][j] = A[i-1][j] || A[i][j-1];
            } else {
                A[i][j] = 0;
            }
            //printf("%d\n", A[i][j]);
        }
    }

    return A[strlen(x)][strlen(y)];
}

int main(void) {
    char x[] = "aba";
    char y[] = "lama";
    char z[] = "alabama";
    isShuffleOf(x,y,z);
    //printf("%d\n", isShuffleOf(x,y,z));
    return 0;
}