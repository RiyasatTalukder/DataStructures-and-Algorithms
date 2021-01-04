def rotate(matrix):
    """
    Given a matrix, the algorithm rotates the elements of the 
    matrix by 90 degrees clockwise. 

    Time: O(n^2)
    Space: O(1)
    """
    #get the transpose of the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    #reverse all the rows of the transpose matrix
    for i in range(len(matrix)):
        matrix[i].reverse()

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]
output = [
    [7,4,1],
    [8,5,2],
    [9,6,3]]
    
rotate(A)
assert A == output