'''
Given a list of non-overlapping intervals sorted by start time,
the algorithm inserts a new interval mainting the property

Time: O(n)
Space: O(n)
'''

def insert(intervals, newInterval):
    # checks for overlapping intervals
    def overlap(a, b):
        return a[0] <= b[1] and b[0] <= a[1]
    # merges overlapping intervals
    def merge(a, b):
        return [min(a[0], b[0]), max(a[1], b[1])]

    results = []
    for i in range(len(intervals)):
        # overlapping, merge and set new interval
        if overlap(intervals[i], newInterval):
            newInterval = merge(intervals[i], newInterval)
        # not overlapping and valid spot for new interval, return
        elif intervals[i][0] > newInterval[1]:
            results.append(newInterval)
            return results + intervals[i:]
        # not valid spot for new interval, keep looping
        elif intervals[i][1] < newInterval[0]:
            results.append(intervals[i])
    
    results.append(newInterval)
    return results

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
assert insert(intervals, newInterval) == [[1,2],[3,10],[12,16]]