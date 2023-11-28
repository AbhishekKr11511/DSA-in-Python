class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None


def insertInBST(node, val):
    if node == None:
        return Node(val)
    elif node.val < val:
        return insertInBST(node.right, val)
    elif node.val > val:
        return insertInBST(node.left, val)
    return node



myRoot = Node(70)
myRoot.left = Node(50)
myRoot.right = Node(90)


print((insertInBST(myRoot, 20)).val)