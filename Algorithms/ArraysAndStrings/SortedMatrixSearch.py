def searchMatrix(matrix, target):
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

def searchMatrixDandC(matrix, target):
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

def searchMatrixBinarySearch(matrix, target):
    """
    This a Binary Search algorithm that finds the element
    in the sorted matrix. 

    Time: O(logm + logn)
    Space: O(1)
    """
    i_start, i_end = 0, len(matrix)
    row = 0

    # search rown
    while i_start < i_end:
        row = (i_start + i_end) // 2
        if matrix[row][-1] < target:
            i_start = row + 1
        elif matrix[row][0] > target:
            i_end = row 
        else:
            break     
    
    if i_start == i_end:
        return False
    
    # search column
    j_start, j_end = 0, len(matrix[0])  
    while j_start < j_end:
        j_mid = (j_start + j_end) // 2
        if matrix[row][j_mid] == target:
            return True
        elif matrix[row][j_mid] < target:
            j_start = j_mid + 1
        else:
            j_end = j_mid
    
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
assert searchMatrixBinarySearch(matrix, target) == True
target = 13
assert searchMatrixBinarySearch(matrix, target) == False