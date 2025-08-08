class student:
    numberofstudent=0
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        self.numberofstudent=student.numberofstudent+1
        student.numberofstudent=student.numberofstudent+1

    def study(self):
        print("study: "+self.name)
    def play(self):
        print("play: "+self.name)

s1=student('lovenesh', 20)
s2=student('aditya',30)
s3=student('mayank', 40)


print(s1.name,s1.marks,s1.numberofstudent)
print(s2.name,s2.marks,s2.numberofstudent)
print(s3.name,s3.marks,s3.numberofstudent)
s1.study()
s2.play()