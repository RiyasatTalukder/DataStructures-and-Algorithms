#include <stdio.h>
int nextFit(double capacity, double weights[], int n){
    /*

    Given a capacity of a container and a set of weights to place in containers.
    The algorithm will return the number of containers required to fit the weights.
    Since this is a NP hard problem, the algorithm will approximate the number of 
    containers needed to store the weights. 

    The approximation is <= 2*optimal number of containers.

    Time: O(n)
    Space: O(1)
    */

    double remaining_capacity = capacity;
    double containers = 1;

    for(int x = 0; x < n; x++) {
        if(weights[x] <= remaining_capacity) {
            remaining_capacity = remaining_capacity -  weights[x];
        } else {
            containers++;
            remaining_capacity = capacity - weights[x];
        }
    }
    return containers;
}
int main() {
    double test[5] = {0.5, 0.25, 0.75, 0.5, 0.75};
    printf("%d\n", nextFit(1.0, test, 5));
    return 0;
}