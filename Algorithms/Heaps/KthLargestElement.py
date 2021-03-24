import heapq
"""
Given a list of numbers, the algorithm finds the k-th 
largest elment in the list.

Time: O(nlogk)
Space: O(k)
"""
def findKthLargest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)
    
    for i in range(k, len(nums)):
        heapq.heappush(heap, nums[i])
        heapq.heappop(heap)
    
    return heap[0]

assert findKthLargest([1,2,3,4,5,6], 3) == 4
assert findKthLargest([4,1,6,3,5,2], 3) == 4
