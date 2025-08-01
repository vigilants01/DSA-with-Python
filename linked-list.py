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

    def insert_at_k(self,data,k):
        if self.head == None:
            if k == 1:
                new_node=Node(data)
                return new_node
            else:
                return None
        if k == 1:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
        if k > 1:
            count=1
            tmp=self.head
            while tmp != None:
                if count == k-1:
                    new_node=Node(data)
                    new_node.next=tmp.next
                    tmp.next=new_node
                    break
                tmp=tmp.next
                count+=1

    def delete_at_head(self):
        self.head=self.head.next
    
    def delete_at_tale(self):
        tmp = self.head
        while tmp.next.next != None:
            tmp=tmp.next
        tmp.next=None
    
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
ll.delete_at_tale()



# ll.insert_at_k(25,3)
ll.Print()