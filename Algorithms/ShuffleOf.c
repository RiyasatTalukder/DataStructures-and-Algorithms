#include <string.h>
#include <stdio.h>

int isShuffleOf(char x[], char y[], char z[]) {
    /*
    Given a target string and two other strings, the algorithm checks 
    if the the given strings can be intervaled to form the target string.
    This algorithm uses a dynamic porgram approach.

    Time: O(m*n)
    Space: O(m*n)
    */
    if(strlen(x)+strlen(y) != strlen(z)) {
        return 0;
    }
    int A[strlen(x)+1][strlen(y)+1];
    int i,j = 0;
    A[i][j] = 1;

    //setup inital conditions
    for(i = 1; i < strlen(x)+1; i++) {
        if(x[i-1] == z[i-1]) {
            A[i][0] = A[i-1][0];
        } else {
            A[i][0] = 0;
        }
    }
    for(j = 1; j < strlen(y)+1; j++) {
        if(y[j-1] == z[j-1]) {
            A[0][j] = A[0][j-1];
        } else {
            A[0][j] = 0;
        }
    }
    //fill the rest of the array for the results of the sub problems
    for(i = 1; i < strlen(x)+1; i++){
        for(j = 1; j < strlen(y)+1; j++) {
            if(x[i-1] == z[i+j-1] || y[j-1] == z[i+j-1]) {
                A[i][j] = A[i-1][j] || A[i][j-1];
                
            } else {
                A[i][j] = 0;
            }
        }
    }

    //final solution is the last entry of the array
    return A[strlen(x)][strlen(y)];
}

int main(void) {
    char x[] = "aba";
    char y[] = "lama";
    char z[] = "alabama";
    printf("%d\n", isShuffleOf(x,y,z));
    return 0;
}