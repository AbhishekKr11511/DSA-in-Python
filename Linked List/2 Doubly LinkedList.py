class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoubleList():
    def __init__(self) -> None:
        self.head = None
    
    def insertStart(self, data):
        newNode = Node(data)
        if self.calSize() == 0:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
            

    
    def insertEnd(self,data):
        newNode = Node(data)
        if self.calSize() == 0:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp
    
    def insertMiddle(self,data, position):
        size = self.calSize()
        if position<1 or size < position:
            print("Enter a valid position value.")
            return
        
        newNode = Node(data)
        temp = self.head
        for i in range(1, position):
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode
        newNode.prev = temp
        temp.next.prev = newNode
    
    def deleteStart(self):
        if self.calSize()==0:
            print("Can't delete as list is empty")
            return
        self.head = self.head.next
        self.head.prev = None
    
    def deleteEnd(self):
        if self.calSize() == 0:
            print("Can't delete as list is empty")
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next.prev = None
        temp.next = None
        
    def deleteMiddle(self, position):
        if self.calSize() == 0:
            print("Can't delete as list is empty")
            return
        if position<1 or position>self.calSize():
            print("Enter a valid postion for deletion")
            return
        temp = self.head
        for i in range(1 , position):
            temp = temp.next
        temp.next = temp.next.next 
        temp.next.prev = temp
        

    
    def display(self):
        if self.head is None:
            print('The List is Empty')
            return
        temp = self.head
        print("Double List : ", end='')
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        
    def calSize(self):
        size = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            size += 1
        return size

myList = DoubleList()
myList.insertEnd(1)
myList.insertEnd(2)
myList.insertEnd(3)
myList.insertEnd(4)
myList.insertMiddle(10, 2)
myList.insertMiddle(11, 2)
myList.deleteMiddle(2)
myList.deleteMiddle(2)
myList.display()