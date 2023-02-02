'''
Given an aray of heights, the algorithm finds the max area between two heights
such that it can hold the most water

Time: O(n)
Space: O(1)
'''

def maxArea(height):
    max_area = 0
    l, r = 0, len(height) - 1

    while r > l:
        l_height, r_height = height[l], height[r]
        length = r - l
        max_area = max(max_area, min(l_height, r_height) * length)

        # we want max area, only move if lower height
        if height[r] > height[l]:
            l += 1
        else:
            r -= 1
    
    return max_area

height = [1,8,6,2,5,4,8,3,7]
assert maxArea(height) == 49