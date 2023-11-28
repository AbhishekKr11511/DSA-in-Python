class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None

# This is through recursion
def insertInBST(node, val):
    if node == None:
        return Node(val)
    elif node.val < val:
        return insertInBST(node.right, val)
    elif node.val > val:
        return insertInBST(node.left, val)
    return node

# This is by interation
def insertion(node, val):
    while node!=None:
        if node.val<val:
            node = node.right
        elif node.val>val:
            node = node.left
    return Node(val)



myRoot = Node(70)
myRoot.left = Node(50)
myRoot.right = Node(90)


print((insertion(myRoot, 20)).val)