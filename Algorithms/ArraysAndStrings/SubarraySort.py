def subarrayToSort(nums):
    """
    Given an array, the algorithm finds the shortest unsorted 
    subarray such that sorting that array will sort the entire 
    array. The algorithm returns the index of those elements.

    Time: O(n)
    Space: O(1)
    """
    #initialize variables 
    mini = float('inf')
    maxx = float('-inf')
    minIndex = 0
    counter = 0
    maxIndex = len(nums)-1

    #go through the array and look for violation of sorted property
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            counter+=1
            #need to keep track of the minimum and maximum of the sub array
            if(nums[i+1] < mini):
                mini = nums[i+1]
            if(nums[i] > maxx):
                maxx = nums[i]
    
    #array is already sorted
    if(counter == 0):
        return []
    
    #finding the left index of the sub array
    while(nums[minIndex] <= mini):
        minIndex+=1
    
    #finding the right array of the sub array
    while(nums[maxIndex] >= maxx):
        maxIndex-=1
    return [minIndex, maxIndex]

A = [1,2,3,4,5,2,6,1,1,0,10,11]
print(subarrayToSort(A))
