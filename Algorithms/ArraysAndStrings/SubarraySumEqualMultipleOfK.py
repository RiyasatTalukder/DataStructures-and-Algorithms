'''
Given an integer array nums and an integer k, 
return true if nums has a continuous subarray of size at least two 
whose elements sum up to a multiple of k, or false otherwise.

Time: O(N)
Space: O(K)
'''

def checkSubarraySum(nums, k):

    # Formula: (i + (xk)) % k = i % k
    if k == 0:
        return False
    
    remainders, sums = {0:-1}, 0
    
    for i in range(len(nums)):
        #xk in the formula
        sums += nums[i]
        remainder = sums % k
        
        if remainder in remainders:
            if i - remainders[remainder] > 1:
                return True
        else:
            remainders[remainder] = i
    
    return False

assert True == checkSubarraySum([5, 3, 8, 10, 2], 5)
assert False == checkSubarraySum([5, 3, 8, 10, 1], 5)