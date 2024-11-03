class Node:

    def __init__(self,data=None):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:

    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if self.head:
            self.head.prev=new_node
        self.head=new_node

    def insert_at_end(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        new_node.prev=last

    def insert_after_node(self,prev_node,data):
        if not prev_node:
            print("Previous Node cannot be Null!")
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next:
            new_node.next.prev=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print( )
        return
    
dl=DoublyLinkedList()
dl.insert_at_beginning(1)
dl.insert_at_end(2)
dl.insert_at_end(3)
dl.insert_at_end(4)
dl.insert_at_end(5)
dl.display()


# 1 <->end
# 4 <-> 1
