class Node:

    def __init__(self,data=None):
        self.data=data
        self.next=None

class SinglyLinkedList:

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
    
    def delete(self,key):
        current=self.head

        if current and current.data==key:
            self.head=current.next
            current=None
            return
        
        prev=None
        while current and current.data != key:
            prev=current
            current=current.next
            

        if current == None:
            print("Element not found in the linked list") 
            return
        
        prev.next=current.next
        current=None

l=SinglyLinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.display()
l.delete(4)
l.display()
l.delete(7)

