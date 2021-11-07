"""
Given a list of numbers, determine the number of
subarrays that sum to k.

Time: O(n)
Space: O(k)
"""

def subarraySum(nums, k):
    sums, prev, result = 0, {}, 0
    
    for i, num in enumerate(nums):
        sums += num
        if sums - k in prev:
            #add the frequency
            result += prev[sums - k]
        if sums == k:
            result += 1
        
        if sums in prev: 
            prev[sums] += 1
        else:
            prev[sums] = 1

    return result
            