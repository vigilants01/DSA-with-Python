class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name},Age: {self.age}"
    
    def speak(self):
        return "Father Speaks"
    
class child1(father):
    def __init__(self,name,age,sports):
        super().__init__(name,age)
        self.sports=sports

    def show(self):
        return f"Sport: {self.sports}"
    
    def speak(self):
        return "Child1 speak"
    
class child2(father):
    def __init__(self,name,age,sports):
        super().__init__(name,age)
        self.sports=sports

    def show(self):
        return f"Sport: {self.sports}"
    
    def speak(self):
        return "Child2 speak"
    
c1=child1("Lovenesh",20,"GYM")
c2=child2("Aditya",20,"Swimming")
print(c1.speak())
print(c2.speak())
print(c1.details())
print(c2.details())
