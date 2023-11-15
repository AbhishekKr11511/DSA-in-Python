# This is circular queue

class Circular_Queue():
    def __init__(self, cap) -> None:
        self.queue = [None] * cap
        self.capacity = cap
        self.front = -1
        self.rear = -1
        self.size = 0
    
    def is_full(self):
        if self.size == self.capacity:
            print('Queue is full, can not push more')
        return self.size == self.capacity
    
    def is_Empty(self):
        if self.front == -1 and self.rear == -1:
            print('Queue is empty, can not dequeue')
        return self.size == 0
    
    def enqueue(self, element):
        if self.is_full():
            print("Can't Enqueue as it is full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1
    
    def dequeue(self):
        if self.is_Empty():
            print('Queue is already empty, can not dequeue')
            return
        
    # This is the condition if we remove the last element in queue
        if self.rear == self.front:
            self.rear = self.front = -1
            self.size -= 1
    
    # This is the condition when queue has more than 1 element
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
    
    def display(self):
        if self.is_Empty():
            print("There are not elements in the queue")
            return
        i = 0
        print("Queue : ", end='')
        while i!= self.rear:
            print(self.queue[i], end=' ')
            i = (i + 1) % self.capacity
        
        # This for the last of rear element
        print(self.queue[i])