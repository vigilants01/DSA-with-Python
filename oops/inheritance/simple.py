class GrandFather:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def details(self):
        return f"Name: {self.name},Age: {self.age} "
    
    def speak(self):
        print("GrandFather Speaks")

class Father(GrandFather):
    def __init__(self,name,age,occupation):
        super().__init__(name,age)
        self.occupation=occupation

    def show_occupation(self):
        return f"Occupation: {self.occupation}"
    
    def speak(self):
        return ("Father speaks")

s1=Father("Lovenesh",20,"Docter")
print(s1.speak())
print(s1.show_occupation())
print(s1.name,s1.age,s1.occupation)