from collections import deque

def prevGreaterEle(arr):
    stack = deque()
    spans = ['-']
    stack.append(arr[0])
    i = 1
    while i<len(arr):
        if len(stack)==0:
            spans.append('-')
            stack.append(arr[i])
            i+=1
        elif arr[i]<stack[-1]:
            spans.append(stack[-1])
            stack.append(arr[i])
            i+=1
        elif arr[i]>stack[-1]:
            stack.pop()
            continue
    return spans

print(prevGreaterEle([12,10,20,22,15,14,18,32,20,22,19]))