# Implementing queue Using Class
# Define a cap (number of elements which can fit in the queue)

class Queue():
    def __init__(self,cap) -> None:
        self.queue = [None]*cap
        print("Queue is Created")
        self.capacity = cap
        
        # Index of first element
        self.front = 0
        # Index of the last element
        self.rear = self.capacity-1
        # Length of queue (Number of elements in the queue)
        self.size = 0
        
    
    def is_full(self):
        if self.size == self.capacity:
            print('OverFlow, Can not Enqueue. Queue is full')
        
        return self.size == self.capacity
    
    def is_empty(self):
        if self.size == 0:
            print("UnderFlow, Can not Dequeue. Queue is Empty")
        return self.size == 0
    
    def enqueue(self, element):
        if self.is_full():
            print("Can't enqueue, queue is full")
            return
        
        # For the first element, self.rear is the 0th index, then 1st then 2nd and so on
        self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = element
        self.size += 1
        print(self.queue[self.rear], "Enqueued to queue")
    
    def dequeue(self):
        if self.is_empty():
            print("Can't dequeue, Queue is already empty")
            return 
        
        # This is line of code is not neccessary
        item = self.queue[self.front]
        
        # Just shift the front of the queue one index
        self.front = (self.front+1) % self.capacity
        self.size -= 1
        print(item, "Dequeue from queue")

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            i = self.front
            j = 0
            print("Queue : ", end=' ')
            
            while j < self.size:
                print(self.queue[(i+j)%self.capacity], end=' ')
                j+=1






myQueue = Queue(5)

myQueue.display()
myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)
myQueue.enqueue(40)
myQueue.enqueue(50)
myQueue.display()
print()
myQueue.dequeue()
print()
myQueue.enqueue(60)
myQueue.display()
# myQueue.enqueue(70)
# myQueue.display()
# myQueue.enqueue(80)

