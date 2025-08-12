class student:
    __school="GITS"
    __numberofstudent=0
    def __init__(self,name,marks,rollnumber):
        self.name=name
        self.__marks=marks
        self.rollnumber=rollnumber
        self.numberofstudent= student.__numberofstudent+1
        student.__numberofstudent=student.__numberofstudent+1
    @classmethod
    def info(cls,nschool):
        print(cls.__school,cls.__numberofstudent)
        cls.__school=nschool
        print("School Name Update")
        print(cls.__school)

    @staticmethod
    def information(newschool):
        print(student.__school)
        student.__school=newschool
        print(student.__school)


    def getMarks(self):
        return self.__marks
    
    def setMarks(self,newMarks,passCode):
        if passCode==self.__auth():
            self.__marks=newMarks
            return self.__marks
        else:
            return "Invaild Passcode"
        
    def __auth(self):
        return "000"
    
    def study(self):
        return "study"
    
s1=student("lovenesh",90,1)
s2=student("aditya",70,2)
print(s1.setMarks(20,"000"))
print(s1.getMarks())
student.info("NSUIT")
student.information("GNPS")
# print(s1.name,s1.marks,s1.rollnumber,s1.numberofstudent)
# print(s2.name,s2.marks,s2.rollnumber,s2.numberofstudent)