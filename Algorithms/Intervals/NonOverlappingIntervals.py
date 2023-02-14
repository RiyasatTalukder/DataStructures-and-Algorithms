'''
Given an array of intervals intervals where intervals[i] = [starti, endi], 
the algorithm return the minimum number of intervals you need to remove to 
make the rest of the intervals non-overlapping.

Time: O(nlogn)
Space: O(1)
'''

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    def overlap(a, b):
        return a[0] < b[1] and b[0] < a[1]
    
    intervals = sorted(intervals, key = lambda x : x[0])
    prev = intervals[0]
    min_remove = 0

    for i in range(1, len(intervals)):
        if overlap(prev, intervals[i]):
            min_remove += 1
            # we want to keep the minimum end value to reduce our chances of overlapping with other intervals
            prev = intervals[i] if intervals[i][1] < prev[1] else prev
        else:
            prev = intervals[i]
    
    return min_remove

intervals = [[1,2],[2,3],[3,4],[1,3]]
assert eraseOverlapIntervals(intervals) == 1