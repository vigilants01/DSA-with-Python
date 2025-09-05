class solution:
    def __init__(self):
        self.stack=[]

    def push(self,x):
        self.stack.append(x)
        print(f"{x} Appended")

    def pop(self):
        if self.is_empty():
            return "Empty stack"
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            return "Empty stack"
        return self.stack[-1]
    
    def is_empty(self):
            return len(self.stack) == 0
        
s=solution()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
print("Top element:", s.top())
print("Popped:", s.pop())       
print("Is stack empty?", s.is_empty())  
# print("Stack size:", s.sizeof())
# print(s.all())