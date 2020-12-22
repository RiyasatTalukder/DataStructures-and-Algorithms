def mergeSort(A):
    """
    This sorting algorithm uses the divide and conquer
    technique to sort an array of integers.

    Time: O(nlogn)
    Space: O(n)
    """
    if(len(A) <= 1):
        return A
    
    left = mergeSort(A[:len(A)//2])
    right = mergeSort(A[len(A)//2:])

    return merge(left, right)

#merge sorted arrays
def merge(left, right):
    result = []
    i = 0
    j = 0
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while(i < len(left)):
        result.append(left[i])
        i+=1
    while(j < len(left)):
        result.append(right[j])
        j+=1
    return result
