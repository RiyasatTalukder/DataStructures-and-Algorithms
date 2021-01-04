def searchMatrix(matrix: List[List[int]], target: int):
    """
    Given a sorted matrix, the algorithm finds the target 
    value within the matrix and returns True if the value exists.

    Time: O(n+m)
    Space: O(1)
    """
    
    i = 0
    j = len(matrix[i])-1
    while(i < len(matrix) and j >= 0):
        if(matrix[i][j] == target):
            return True
        if(matrix[i][j] < target):
            i+=1
        else:
            j-=1
            
    return False

def searchMatrixDandC(matrix: List[List[int]], target: int):
    """
    This a Divide and Conquer algorithm that finds the element
    in the sorted matrix. It eliminates the 1st or 4th quadrant 
    from the matrix based on the target value and if it is < or > 
    than the middle element.

    Time: O(n^1.58)
    Space: O(1)
    """
    if(len(matrix) == 1):
        return matrix[0][0] == target
    
    i = len(matrix)//2
    j = len(matrix[i])//2
    
    if(matrix[i][j] == target):
        return True
    
    if(matrix[i][j] < target):
        return (self.searchMatrix([matrix[k][:j] for k in range(i)], target) 
                or self.searchMatrix([matrix[k][j:] for k in range(i)], target)
                or self.searchMatrix([matrix[k][:j] for k in range(i, i*2)], target))
    
    else:
        return (self.searchMatrix([matrix[k][j:] for k in range(i)], target) 
                or self.searchMatrix([matrix[k][:j] for k in range(i, i*2)], target) 
                or self.searchMatrix([matrix[k][j:] for k in range(i, i*2)], target))
