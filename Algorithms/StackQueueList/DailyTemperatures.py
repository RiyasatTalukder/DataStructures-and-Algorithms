'''
Given an array of daily temperatures, the algorithm returns the number of days
till the next warmer temperature from each record.

Time: O(n)
Space: O(n)
'''

def dailyTemperatures(temperatures):
    # stack to store temperatures and pop them if matching pair (warmer) is found
    stack, result = [], [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and stack[-1][1] < temperatures[i]:
            prev_temp = stack.pop()
            result[prev_temp[0]] = i - prev_temp[0]
        stack.append([i, temperatures[i]])
    
    return result

temperatures = [73,74,75,71,69,72,76,73]
assert(dailyTemperatures(temperatures) == [1,1,4,2,1,1,0,0])