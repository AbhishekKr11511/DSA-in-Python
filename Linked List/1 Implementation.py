
class Node():
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self) -> None:
        self.head = None
        print("Linked List created")
    
    def insertStart(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
    
    def insertLast(self,data):
        newNode = Node(data)

        # If the head is empty
        if self.head is None:
            self.head = newNode
            return
        
        # Traverse to the last node
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        
        temp.next = newNode
    
    def insertMiddle(self, data, position):
        newNode = Node(data)
        size = self.calSize()

        # For Invalid Positions
        if position<1 or size<position:
            print("Can't insert, Insert a valid position")
            return

        # For traversing the list to the desired position
        temp = self.head
        for i in range(1,position):
            temp = temp.next
        
        newNode.next = temp.next
        temp.next = newNode

    def display(self):
        if self.head is None:
            print('The List is Empty')
            return
        
        temp = self.head
        print("Linked List : ", end=" ")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
    
    def deleteEnd(self):
        if self.head is None:
            print('List is empty, can not delete')
            return
        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None
    
    def deleteStart(self):
        if self.head is None:
            print('List is empty, can not delete')
            return
        self.head = self.head.next
    
    def deleteMiddle(self,position):
        size = self.calSize()
        if self.head is None:
            print('List is empty, can not delete')
            return
        if position<1 or size<position:
            print("Can't insert, Insert a valid position")
            return
        node = self.head
        for i in range(1, position):
            node = node.next
        node.next = node.next.next
        
    def calSize(self):
        size = 0
        node = self.head

        while node is not None:
            node = node.next
            size += 1
        return size

myList = LinkedList()
myList.insertLast(1)
myList.insertLast(2)
myList.insertLast(3)
myList.insertLast(10)
# myList.insertStart(10)
# myList.insertStart(20)
myList.insertMiddle(9,3)
myList.insertMiddle(8,3)
myList.insertMiddle(7,3)
myList.deleteMiddle(2)
myList.display()