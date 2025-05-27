class stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values=[x]+self.values
    def pop(self):
        if self.values:
            return self.values.pop(0)  # Remove from the top
        else:
            return "Stack is empty"
    
s=stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(s.values)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())