"""
Given a set of intervals, the algorithm returns a new set
of intervals that merges all overlapping intervals.

Time: O(nlogn)
Space: O(n)
"""
def merge(intervals):
    results = []
    #sort by start times to check for overlaps
    intervals.sort(key=lambda x:x[0])
    
    for i in intervals:
        #finish of previous interval < start of current (interval does not overlap)
        if not results or results[-1][1] < i[0]:
            results.append(i)
        #interval overlaps, take the maximum finish time for the merged interval
        else:
            results[-1][1] = max(i[1], results[-1][1])
    
    return results

assert merge([[1,2],[1,6],[8,10]]) == [[1,6],[8,10]]
assert merge([[1,4],[3,6],[4,10]]) == [[1,10]]