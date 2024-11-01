class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        
        if self.head==None:
            self.head=new_node
            return
        
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node

    def display(self):
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
