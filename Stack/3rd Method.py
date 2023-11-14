# List can become slow due to long length and append method may take longer time
# Deque is a better alternative since, deque provides O(1) time complexity at both ends
# that O(1) append or pop, while list has O(n) time complexity

from collections import deque

stack = deque()

stack.append(11)
stack.append(22)
stack.append(33)

print(stack)

top = stack[-1]
print(top)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
print(stack)