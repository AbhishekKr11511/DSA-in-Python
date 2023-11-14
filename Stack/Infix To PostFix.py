# Infix to postfix is the type of algorithm to push the operator to the right and the oprands to left
# Here is an example

# 3+4*2
# (5+6)*2-8
#8 *(3+4)-6

# Answer
# 3 4 2 * +
# 5 6 + 2 * 8 -
# 8 3 4 + * 6 -

def checkIfOperand(c):
    # .isalpha() returns true if string contains alphabets
    # .isdigit() returns true if string contains numbers
    return c.isalpha() or c.isdigit()

# This function defines the precedence of the characters
def precedence(ch, stack):
    prec = {'+':1, '-':1, '*':2,'/':2, '^':3}
    try:
        a = prec[ch]
        b = prec[stack]
        return a<=b
    except KeyError:
        return False


def infixToPostfix(expr):
    stack = []
    result = []

    for i in range(len(expr)):
        if checkIfOperand(expr[i]):
            result.append(expr[i])
        
        elif expr[i] == '(':
            stack.append(expr[i])
        
        elif expr[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())

            if len(stack) > 0 and stack[-1] != '(':
                return # Invalid expression
            else:
                stack.pop()
        
        else:
            while len(stack)>0 and precedence(expr[i], stack[-1]):
                result.append(stack.pop())

            stack.append(expr[i])
    
    while len(stack) > 0:
        result.append(stack.pop())

    print(''.join(result))

expression = 'a+b*(c^d-e)^(f+g*h)-i'
infixToPostfix(expression)