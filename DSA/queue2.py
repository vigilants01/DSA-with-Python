class solution:
    def __init__(self):
        self.queue=[]

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def sizeof(self):
        return len(self.queue)
    
    def all(self):
        return self.queue
    
q = solution()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front element:", q.front())
print("Dequeued:", q.dequeue()) 
print(q.all())
print("Front element:", q.front())