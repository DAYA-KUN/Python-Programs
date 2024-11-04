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

    def delete_node(self,node):
        if self.head==None or node==None:
            return
        if self.head==node:
            self.head=node.next
        if node.next:
            node.next.prev=node.prev
        if node.prev:
            node.prev.next=node.next
        node=None

    def delete_node_by_value(self,value):
        if self.head is None:
            print(f"The Node {value} is not found in the linked list")
            return

        current=self.head
        while current and current.data!=value:
            current=current.next

        if current is None:
            print(f"The Node {value} is not found in the linked list")
            return

        

        if current == self.head:
            self.head = current.next
            if self.head:  # Update the new head's prev pointer, if there is a new head
                self.head.prev = None
        else:
            # Bypass the current node by adjusting pointers
            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev

        # Free up memory (optional)
        current = None
        return


    def display(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        return
    
dl=DoublyLinkedList()
dl.insert_at_beginning(1)
dl.insert_at_end(2)
dl.insert_at_end(3)
dl.insert_at_end(4)
dl.insert_at_end(5)
dl.delete_node(dl.head.next.next.next)
dl.delete_node_by_value(3)
dl.delete_node_by_value(7)
dl.display()


# 1 <->end
# 4 <-> 1
