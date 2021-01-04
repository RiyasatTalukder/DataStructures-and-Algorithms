def shift(nums, k):
    """
    Given an array of integers, the algorithm
    shifts the elements of the array by 1 to 
    the right k times.

    Time: O(n)
    Space: O(1)
    """ 
    if(k == len(nums) or len(nums) == 0):
        return
    #reverse elements in an array
    def reverse(A, start, end):
        while(end > start):
            A[start], A[end] = A[end], A[start]
            start+=1
            end-=1
    
    #since to shift by k times, we move the last k elements to the start
    #we will reverse the whole array
    nums.reverse()
    #calculate shift amount
    shift = k if k < len(nums) else k-len(nums)
    #reverse the first k elements to obtain the orginal order
    reverse(nums, 0, shift-1)
    #reverse the remaining elements to obtain the orginal order
    reverse(nums, shift, len(nums)-1)

def shift2(nums, k):
    """
    This implementation utilizes more space,
    however, runs slightly faster.

    Time: O(n)
    Space: O(n)
    """ 
    if(k == len(nums) or len(nums) == 0):
        return
    shift = k if k < len(nums) else k-len(nums)
    #elements to move to the front of the array
    arr1 = nums[len(nums)-shift:]
    #elements to move to the back of the array
    arr2 = nums[:len(nums)-shift]
    #assign the values in the orginal array
    for i in range(len(arr1)):
        nums[i] = arr1[i]
    for i in range(len(arr2)):
        nums[len(arr1)+i] = arr2[i]  

nums = [1,2,3,4,5,6,7]
shift_by = 3
output = [5,6,7,1,2,3,4]
shift(nums, shift_by)
assert nums == output
nums = [1,2,3,4,5,6,7]
shift2(nums, shift_by)
assert nums == output