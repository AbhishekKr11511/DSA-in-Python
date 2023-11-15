# You can implement a queue in a list kind of way

queue = []

# Adding elements to the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

print('Initial Queue')
print(queue)

print('Front: ', queue[0])
print('Rear: ', queue[-1])

# Removing the elements from the queue FIFO

print('\nElements dequeued frm the queue')
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print('\nQueue after removing elements')
print(queue)

# If we remove all the elements from the queue,
# Since this is actually a list, it will return an error