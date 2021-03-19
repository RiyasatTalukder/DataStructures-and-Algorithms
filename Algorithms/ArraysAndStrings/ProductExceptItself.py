"""
Given an array of numbers (nums), the algorithm returns a new array such
that each element, i, corrosponds to the product of nums except nums[i]. 

Time: O(n)
Space: O(n) *for the output array*
"""
def productExceptSelf(nums):
    product = 1
    zero_count = 0
    #calculate the product of the array
    for i in range(len(nums)):
        if(nums[i] != 0):
            product = product*nums[i]
        else:
            #keep track of 0s
            zero_count+=1
    #if > 1 zeros exist, the product will be 0 for all elements regardless
    if(zero_count > 1):
        return [0]*len(nums)
    #if there are no zeros, the product except itself will be product//i
    #if there is 1 zero, the product will be 0 for non-zero elments and the product for the zero element
    return [product//i for i in nums] if zero_count == 0 else [product if i == 0 else 0 for i in nums] 

assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([1,0,3,4]) == [0,12,0,0]
assert productExceptSelf([0,0,3,4,5,6,7,10]) == [0,0,0,0,0,0,0,0]