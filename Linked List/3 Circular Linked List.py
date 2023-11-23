
class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class CircularList():
    def __init__(self) -> None:
        self.head = None
        print("Circular Linked List Created")
    
    def insertStart(self, data):
        newNode = Node(data)
        if self.sizeOfList() == 0:
            self.head = newNode
            self.next = self.head
            print(f"{data}, inserted as first element in the list")
            return
        newNode.next = self.head.next
        self.head.next = newNode
        # We Swap the data
        self.head.data, self.next.data = self.next.data, self.head.data
        print(f"{data} is inserted in the list")
        
    def sizeOfList(self):
        size = 0
        temp = self.head
        while temp != self.head:
            temp = temp.next
            size += 1
        return size
    
    def display(self):
        temp = self.head
        print("Circular list :", end=" ")
        for i in range(self.sizeOfList()):
            print(temp.data, end=" ")
            temp = temp.next
        return

myList = CircularList()
myList.insertStart(1)
myList.display()