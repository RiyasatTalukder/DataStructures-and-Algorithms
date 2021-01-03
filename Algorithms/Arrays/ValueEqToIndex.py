def index_equals_value_search(arr):
    """
    Given a sroted array of distinct integers,
    the algorithm returns the lowest index such
    that the value of arr[index] = index.

    Time: O(logn)
    Space: O(1)
    """
    left = 0
    right = len(arr)
    index = float('inf')
    while(right > left):
        mid = (left+right)//2
        #if we found an element, we store the index and continue the search
        if(mid == arr[mid]):
            index = min(index, mid)
        #search left
        if(mid <= arr[mid]): 
            right = mid
        #search right
        else: 
            left = mid+1
    return index if index != float('inf') else -1

A = [0,1,2,6,78,100]
assert 0 == index_equals_value_search(A)
