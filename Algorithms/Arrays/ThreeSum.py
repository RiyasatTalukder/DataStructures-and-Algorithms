def threeSum(A, target):
    """
    This algorithm finds triplets of numbers that add up to the target.
    It sorts the elements in A and uses a two-pointer approach to find 
    optimal pairs.

    Time: O(n^2)
    Space: O(n)
    """
    A.sort()
    result = []
    for i in range(len(A)-2):
        start = i+1
        end = len(A)-1
        while(end > start):
            curr_sum = A[i] + A[start] + A[end]
            if(curr_sum == target):
                result.append([A[i], A[start], A[end]])
                start+=1
                end-=1
            elif(curr_sum < target):
                start+=1
            else:
                end-=1
    return result

A = [1,2,3,4,5,6,7]
print(threeSum(A, 10))

    
