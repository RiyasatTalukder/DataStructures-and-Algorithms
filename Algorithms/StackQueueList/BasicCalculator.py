'''
Given the operators +, -, *, / and an expression,
evaluate the expression and return the result.

Time: O(n)
Space: O(n)
'''

def calculate(s):
    stack, i, num, sign = [], 0, 0, '+'
    
    while i < len(s):
        if s[i].isdigit():
            #parse number
            num = num*10 + int(s[i])
        
        #Note: the sign is previous sign
        if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            
            num = 0
            sign = s[i]
        
        i += 1
 
    return sum(stack)

assert 100 == calculate("12+8 - 10*2 +1000/10")