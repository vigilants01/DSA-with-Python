class GrandFather:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name} , Age: {self.age}"
    
    def speak(self):
        return "GrandFather speaks"
    
class Father(GrandFather):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation=occupation

    def show_occupation(self):
        return f"Occupation: {self.occupation}"
    
    # def speak(self):
    #     return "Father speaks"
    
class Child(Father):
    def __init__(self,name,age,hobby):
        super().__init__(name,age,"Engineer")
        self.hobby=hobby

    def show_hobby(self):
        return f"Hobby: {self.hobby}"
    
    # def speak(self):
    #     return "Child speaks"
    
c1=Child("Lovenesh",30,"GYM")
print(c1.show_hobby())
print(c1.speak())
print(c1.show_occupation())

