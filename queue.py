class queue:
    def __init__(self):
        self.values = []

    def enqueue(self,x):
        self.values.append(x)

    def dequeue(self):
        front=self.values[0]
        self.values=self.values[1:]
        return front
    
q=queue()
q.enqueue(10)
print(q.values)
q.enqueue(20)
print(q.values)
q.enqueue(30)
print(q.values)
q.enqueue(40)
print(q.values)
q.enqueue(50)
print(q.values)
q.dequeue()
print(q.values)
q.dequeue()
print(q.values)