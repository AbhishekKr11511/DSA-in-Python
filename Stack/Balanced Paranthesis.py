def compare(value1, value2):
    return (value1=='(' and value2==')') or (value1=='{' and value2=='}') or (value1=='[' and value2==']')

def checkParanthesis(brackets):
    stack = []
    for i in range(len(brackets)):
        if brackets[i]=='(' or brackets[i]=='{' or brackets[i]=='[':
            stack.append(brackets[i])
        elif brackets[i]==')' or brackets[i]=='}' or brackets[i]==']':
            if len(stack)!=0:
                compareResult = compare(stack[len(stack)-1], brackets[i])
                if compareResult:
                    stack.pop()
                else:
                    return False
            else:
                return False
        else:
            return False
    if len(stack)==0:
        return True
    else:
        return False

output = checkParanthesis('()')
print(output)
