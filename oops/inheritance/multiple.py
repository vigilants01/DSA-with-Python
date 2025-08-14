class Father:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name} , Age: {self.age}"
    
    def speak(self):
        return "Father speaks"
    
class Mother:
    def __init__(self,name,food):
        self.name=name
        self.food=food

    def show_food(self):
        return f"Favorite Food: {self.food}"
    
    def speak(self):
        return "Mother speaks"
    
class Child(Father,Mother):
    def __init__(self,name,age,food,hobby):
        Father.__init__(self,name,age)
        Mother.__init__(self,name,food)
        self.hobby=hobby

    def show_hobby(self):
        return f"Hobby: {self.hobby}"
    
    # def speak(self):
    #     return "Child speaks"
    
c1=Child("Lovenesh",20,"Pizza","GYM")
print(c1.show_hobby())
print(c1.speak())
print(c1.show_food())
print(c1.name,c1.age,c1.hobby,c1.food)