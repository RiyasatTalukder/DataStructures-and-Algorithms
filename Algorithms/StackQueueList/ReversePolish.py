def evalRPN(tokens):
    """
    Given an arithmetic expression in reverse
    polish notation, the algorithm evaluates 
    the expression and returns the result.

    Time: O(n)
    Space:O(n)
    """
    #we need the previous 2 values that appear before an operand
    #a stack is used to pop these values in constant time
    stack = []
    ops = "+-*/"
    for i in tokens:
        if i not in ops:
            stack.append(int(i))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if(i == '+'):
                stack.append(num2+num1)
            elif(i == '-'):
                stack.append(num2-num1)
            elif(i == '*'):
                stack.append(num2*num1)
            elif(i == '/'):
                print(num2, num1)
                stack.append(int(num2/num1))
    return stack.pop()

expression = ["4", "13", "5", "/", "+"]
assert 6 == evalRPN(expression)