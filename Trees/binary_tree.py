class Node:
    
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:

    def __init__(self,root):
        self.root=Node(root)

    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.value,end=" ")
            self.in_order(node.right)

    def post_order(self,node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value,end=" ")

    def pre_order(self,node):
        if node:
            print(node.value,end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

t=BinaryTree(1)
t.root.left=Node(2)
t.root.right=Node(3)
t.root.left.left=Node(4)
t.root.left.right=Node(5)
t.root.right.left=Node(6)
t.root.right.right=Node(7)

t.in_order(t.root)
print()
t.post_order(t.root)

