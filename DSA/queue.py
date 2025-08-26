class queue:
    def __init__(self):
        self.q=[]

    def enqueue(self,x):
        self.q.append(x)
        print(f"{x} Appended")
    
    def is_empty(self):
        return len(self.q)==0
    
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.q[0]
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.q.pop(0)
    
    def size(self):
        return len(self.q)
    
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front element:", q.front())
print("Dequeued:", q.dequeue()) 