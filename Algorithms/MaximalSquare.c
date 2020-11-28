int maximalSquare(char** matrix, int matrixSize, int* matrixColSize){
    /*

    Given a matrix withs 1's and 0's, find the maximum area of a square 
    that is formed by the 1's in the matrix. 

    Time: O(n*m)
    Space: O(n*m)
    */
    
    int dp[matrixSize+1][*(matrixColSize)+1];
    //initialize array with value 0
    memset(dp, 0, (matrixSize+1)*(*(matrixColSize)+1)*sizeof(int));
    
    /*
    Subproblems to solve: For a square to exist, we need the surroudning elements to be > 0.
    We need to check the neighbours of the current element. We only want to increase the length
    if all the elements are the same size. We can achieve this by taking the minimum value. Since 
    a sqaure can be 1x1 (1 element matrix) and each increase of dimension of the square increases 
    the side lengths by 1, we can add 1 to the minimum and store that.

    Recursive formuala: dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    Final solution: max side of a square found * itself
    */
    int max = 0;
    int min = 0;
    
    for(int x = 1; x < matrixSize+1; x++) {
        for(int y = 1; y < *(matrixColSize)+1; y++) {
            if(matrix[x-1][y-1] == '1') {
                min = dp[x-1][y-1] <= dp[x-1][y] ? dp[x-1][y-1]: dp[x-1][y];
                min = min <= dp[x][y-1] ? min: dp[x][y-1];
                dp[x][y] = min + 1;
                max = dp[x][y] > max ? dp[x][y]: max;
            }
        }
    }
    
    return max*max;

}