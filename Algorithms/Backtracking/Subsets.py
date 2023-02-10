'''
Given an integer array nums of unique elements, the algorithm returns all possible 
subsets

Time: O(n * 2^n)
Space: O(n * 2^n)
'''

def subsets(nums):
    def backtrack(start, subset):
        result.append(subset[:])
        
        # we have two choices - either include current element or dont
        for i in range(start, len(nums)):
            # include current element
            subset.append(nums[i])
            backtrack(i + 1, subset)
            # dont include current element
            subset.pop()
    
    result = []
    backtrack(0, [])
    return result

nums = [1,2,3]
assert sorted(subsets(nums)) == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])