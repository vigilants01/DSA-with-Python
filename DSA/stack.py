class stack:
    def __init__(self):
        self.st=[]

    def push(self,x):
        self.st.append(x)
        print(f"{x} Appended")

    def top(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.st[-1]
    
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.st.pop()
    
    def is_empty(self):
        return len(self.st)==0
    
    def size(self):
        return len(self.st)

s = stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.push(60)
print("Top element:", s.top())
print("Popped:", s.pop())       
print("Is stack empty?", s.is_empty())  
print("Stack size:", s.size())