"""
Given two arrays, find the intersection of them
and return them in a list. No duplicate elements.

Let n > m
Time: O(n*logn)
Space: O(m)
"""

def intersection(nums1, nums2):
    #sort the arrays and assign the pointers
    nums1, nums2 = sorted(nums1), sorted(nums2)
    l, r, result = 0, 0, []
    
    while(l < len(nums1) and r < len(nums2)):
        #3 cases
        #left is smaller. Since sorted, move left pointer to catch up to right
        if nums1[l] < nums2[r]:
            l+=1
        #right is smaller. Since sorted, move right pointer to catch up to left
        elif nums1[l] > nums2[r]:
            r+=1
        #Found matching elemnts
        else:
            result.append(nums1[l])
            #check for duplicates and move pointer's accordingly
            current = nums1[l]
            while l < len(nums1) and nums1[l] == current:
                l+=1
            while r < len(nums2) and nums2[r] == current:
                r+=1

    return result


assert intersection([2, 3, 5, 1, 2], [3, 3, 3, 2]) == [2, 3]