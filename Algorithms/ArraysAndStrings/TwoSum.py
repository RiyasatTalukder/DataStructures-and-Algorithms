def twoSum(A, target):
    """
    Given a set of numbers, this function returns two pair of numbers
    that sum up to the target.

    Time: O(n)
    Space: O(n)
    """

    #since we need 2 numbers x,y, we can treat x as the current element and store y in the Dictionary
    visited = {}
    for x in A:
        if(target - x in visited):
            return [x, target-x]
        else:
            visited[x] = True
    
    return []
