class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    
    def insert_at_head(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    def insert_at_last(self,data):
        new_node=Node(data)
        tmp=self.head
        while tmp.next != None:
            tmp=tmp.next
        tmp.next=new_node
    
    def Print(self):
        tmp =self.head
        while tmp:
            print(tmp.data,end=' ')
            tmp=tmp.next
        print("None")

ll=linkedlist()
ll.insert_at_head(30)
ll.insert_at_head(20)
ll.insert_at_head(10)
ll.insert_at_last(40)
ll.Print()