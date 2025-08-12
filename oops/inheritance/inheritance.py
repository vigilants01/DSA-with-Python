class user:
    def __init__(self,name,id,school,amount):
        self.name=name
        self.id=id
        self._school=school
        self.__amount=500

    def login(self):
        print("Logged in")

    def logout(self):
        print("Logged out")

    def play(self):
        print("Father is  Playing")

class student(user):
    def __init__(self,name,id,marks,school,amount):
        super().__init__(name,id,school,amount)
        self.marks=marks
        print(self._school)

    def play(self):
        super().play()
        print("I'm Playing")

s1=student("Lavi",1,67,"GITS",200)
print(s1.name,s1.id,s1.marks)
s1.login()
s1.logout()
s1.play()