class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

path = []

def searchItem(node,val):
    global path
    if node == None:
        return False
    elif node.val == val:
        path.append(node.val)
        return path
    elif node.val < val:
        path.append(node.val)
        return searchItem(node.right, val)
    elif node.val > val:
        path.append(node.val)
        return searchItem(node.left, val)
    else:
        return False


myRoot = Node(70)
myRoot.left = Node(50)
myRoot.right = Node(90)
myRoot.left.left = Node(30)
myRoot.left.right = Node(60)
myRoot.right.left = Node(80)
myRoot.right.right = Node(110)

result = searchItem(myRoot, 90)
print(result)