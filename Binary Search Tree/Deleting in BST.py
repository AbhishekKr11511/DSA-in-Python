class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None


def deleteNode(root,val):
    if root == None:
        return
    
    if root.data > val:
        root.left = deleteNode(root.left,val)
    elif root.data < val:
        root.right = deleteNode(root.right, val)
    
    else:
        if root.left == None:
            temp = root.right
            return temp
        elif root.right == None:
            temp = root.left
            return temp
        else:
            successor = inorderSuccessor(root)
            root.data = successor.data
            root.right = deleteNode(root.right, successor.data)
    return root

myRoot = Node(70)
myRoot.left = Node(50)
myRoot.right = Node(90)
myRoot.left.left = Node(30)
myRoot.left.right = Node(60)
myRoot.right.left = Node(80)
myRoot.right.right = Node(110)