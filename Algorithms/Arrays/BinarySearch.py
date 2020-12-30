def search(nums, target):
    """
    Given a sorted array and a target element, the algorithm
    finds the index of the target element (if present in array)
    and returns it.

    Time: O(logn)
    Space: O(1)
    """
    #upper bound and lower bound
    low = 0
    high = len(nums)

    while(high > low):
        #midpoint/pivot
        mid = (high+low)//2
        #if target found, return index
        if(nums[mid] == target):
            return mid
        #look into the right subarray from the midpoint
        if(nums[mid] < target):
            low = mid + 1
        #look into the left subarray from the midpoint
        else:
            high = mid
    #if element not present, return -1
    return -1

A = [1,2,3,4,5]
assert 3 == search(A, 4)