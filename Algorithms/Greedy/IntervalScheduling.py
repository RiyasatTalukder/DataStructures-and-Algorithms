def scheduleInterval(a):
    """
    Given a set of intervals, the algorithm find the maximum
    number of schdules that can be fit between the minimum 
    start time and the maximum finish time in the set

    Time: O(nlogn)
    Space: O(n)
    """
    a.sort(key=lambda x:x[1])
    optimized_schedule = []
    max_f = 0
    for interval in a:
        if(interval[0] >= max_f):
            optimized_schedule.append(interval)
            max_f = interval[1]
    
    #returns a cardinality feasible set 
    return optimized_schedule

A = [[1,3], [1,4], [5,6], [7,10]]
print(scheduleInterval(A))
