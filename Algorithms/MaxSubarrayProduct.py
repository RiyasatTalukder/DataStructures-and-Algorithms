def maxProductSubarray(self, nums: List[int]) -> int: 
    """
    Given an array of numbers, the algorithm finds the maximum
    product that can be achieved from a subarray. It takes a 
    dynamic programming approach.

    Time: O(n)
    Space: O(1)
    """   

    #dp approach: we need to keep building up from the previous product value for each elment

    maxi = float('-inf')
    dp_max = 1
    dp_min = 1

    for i in range(1, len(nums)+1):
        temp = dp_max
        #keeping track of the maximum multiple
        dp_max = max(max(temp*nums[i-1], dp_min*nums[i-1]), nums[i-1])
        #keeping track of negative multiples since dp_max does not consider them
        dp_min = min(min(temp*nums[i-1], dp_min*nums[i-1]), nums[i-1])
        #keeping track of the highest product
        maxi = max(dp_max, maxi)
    
    return maxi