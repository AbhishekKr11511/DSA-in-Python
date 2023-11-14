# Steps for Infix to Prefix Conversion:
# 1. Reverse the Infix Expression: Start by reversing the infix expression. This step simplifies the process as you'll work from right to left.

# 2. Convert to Postfix: Use the reversed expression and convert it to postfix. This step involves the same logic as infix to postfix conversion but operating on the reversed expression.

# 3. Reverse the Postfix Expression: Once you have the postfix expression, reverse it to get the prefix expression.

def checkIfOperand(c):
    return c.isalpha() or c.isdigit()

def precendence(char, stack_element):
    ch = {
        "+":1,
        "-":1,
        "*":2,
        "/":2,
        "^":3,
    }
    
    try:
        a = ch[char]
        b = ch[stack_element]
        return a<=b
    except KeyError:
        return False

def infix_to_prefix(expr):
    expr = list(expr)
    expr.reverse()
    
    stack = []
    prefix = []

    for i in range(len(expr)):
        if checkIfOperand(expr[i]):
            prefix.append(expr[i])
        
        elif expr[i]=='(':
            stack.append(expr[i])
        
        elif expr[i]==')':
            while len(stack)>0 and stack[-1]!='(':
                prefix.append(stack.pop())
            if len(stack)>0 and stack[-1]!='(':
                return # Invalid expression as the bracker doesn't close
            
            else:
                stack.pop()
        
        else:
            while len(stack)>0 and precendence(expr[i], stack[-1]):
                prefix.append(stack.pop())
            
            stack.append(expr[i])
            
    while len(stack) > 0:
        prefix.append(stack.pop())
    print(prefix)
    prefix.reverse()
    print(prefix)
    print("".join(prefix))

expression = '3+4*2'

infix_to_prefix(expression)