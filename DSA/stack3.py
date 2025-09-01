class dsa:
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)
        return f"{x} Appended"
    def sizeof(self):
        if self.is_empty():
            return "Empty Stack"
        return len(self.stack)
    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def top(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.stack[-1]
    def all(self):
        return self.stack
s=dsa()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
print("Top element:", s.top())
print("Popped:", s.pop())       
print("Is stack empty?", s.is_empty())  
print("Stack size:", s.sizeof())
print(s.all())