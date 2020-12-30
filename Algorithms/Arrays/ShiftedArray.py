def search(nums, target):
    """
    Given a sorted array that is shifted by an unknown amount,
    the algorithm returns the index of the target (if present)
    in the array.

    Time: O(logn)
    Space: O(1)
    """
    if(len(nums) == 0):
        return -1
    low = 0
    high = len(nums)
    #index where the elements are shifted
    pivot = 0
    while(high > low):
        mid = (low+high)//2
        #pivot found
        if(mid < len(nums)-1 and nums[mid] > nums[mid+1]):
            pivot = mid
            break
        #sorted property is maintained, search right
        if(nums[mid] >= nums[0]):
            low = mid+1
        #sorted violated, so search left for pivot
        else:
            high = mid
    #binary search implementation
    def binarySearch(nums, i, j, target):
        while(j > i):
            mid = (i+j)//2
            if(nums[mid] == target):
                return mid
            if(nums[mid] < target):
                i = mid+1
            else:
                j = mid
        return -1
    
    #search on the individual sorted arrays
    index = binarySearch(nums, 0, pivot+1, target)
    index2 = binarySearch(nums, pivot, len(nums), target) if index == -1 else -1
    
    return index if index != -1 else index2

A = [5,6,7,8,1,2,3,4]
assert 4 == search(A, 1)