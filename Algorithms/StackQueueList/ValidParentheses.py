"""
 Given a string containing only parentheses, the aglorithm will make
 sure the parentheses have both openning and closing bracket of the same
 type and they are closed in the same order.

 Time: O(n)
 Space: O(n)
"""       
def isValid(s):
    #possible parentheses
    open_paran = {'(': ')', '{': '}', '[': ']'}
    #stack to keep track of the open parentheses
    stack = []
    for i in s:
        if i in open_paran:
            stack.append(i)
        else:
            #make sure there was an opening and the previous opening corresponds to the closing
            if(len(stack) == 0 or open_paran[stack.pop()] != i):
                return False
    #all the opening parentheses must have a closing parentheses
    return len(stack) == 0

assert isValid("((([[[]]{}])))") == True
assert isValid("(((())])") == False