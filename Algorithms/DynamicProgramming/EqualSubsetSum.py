def canPartition(nums):
    """
    Given an array of numbers, check if it
    is possible to partition the array into 2 subarrays
    that obtain the same sum across the elements in each subarray.

    Time: O(nC)
    Space: O(nC)
    """

    #sum of all the elements
    capacity = sum(nums)
    #if odd sum, it is not possible to partiion into equal subarrays
    if(capacity & 1):
        return False
    
    #target sum
    capacity = capacity//2

    #dp approach: We need to see of it is possible for the elements to sum to the target capacity
    #We can break down this down to the 0/1 knapsack problem and treat the elements as weights and values
    #Therefore, the recursive formula we have:
    #   - dp[i-1][j] or dp[i-1][j-nums[i-1]], if j >= nums[i-1] (weight/value)
    #   - dp[i-1][j], otherwise (we dont add the item)

    dp = [[False]*(capacity+1) for i in range(len(nums)+1)]
    dp[0][0] = True
        
    for i in range(1, len(nums)+1):
        for j in range(1, capacity+1):
            if(nums[i-1] <= j):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[len(nums)][capacity]

A = [1,2,3,4,10]
assert True == canPartition(A)