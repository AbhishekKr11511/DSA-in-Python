# In this method we use the OOPs concepts 


class Stack:
    def __init__(self) -> None:
        self.stack = []
        print("Stack has been created.")
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)
        print(f"{element} has been pushed to stack")
    
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(f"{self.stack.pop()} has been popped")
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(f"Top element is {self.stack[len(self.stack)-1]}")
    
    def size(self):
        print(f"Size of Stack = {len(self.stack)}")
#------------------------------------

myStack = Stack()

print(myStack)

print(myStack.isEmpty())

myStack.pop()

myStack.push(12)
myStack.push(22)
myStack.push(32)

print(myStack.stack)

myStack.peek()

myStack.pop()

myStack.peek()

myStack.size()
