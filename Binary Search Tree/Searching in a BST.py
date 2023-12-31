class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

path = []

# Recursive
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

# Iterative
def searchTree(node,val):
    while node!=None:
        if node.val == val:
            path.append(node.val)
            return path
        elif node.val > val:
            path.append(node.val)
            node = node.left
        elif node.val<val:
            path.append(node.val)
            node = node.right
    return False


myRoot = Node(70)
myRoot.left = Node(50)
myRoot.right = Node(90)
myRoot.left.left = Node(30)
myRoot.left.right = Node(60)
myRoot.right.left = Node(80)
myRoot.right.right = Node(110)

result = searchTree(myRoot, 10)
print(result)