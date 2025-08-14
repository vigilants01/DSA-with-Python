class Temperature:
    def __init__(self,temp):
        if temp >= -273:
            self.__temp = temp
        else:
            print ("Enter Valid Temperature")

    def gettemp(self):
        return f"{self.__temp} C"
    
    def settemp(self,newtemp):
        if newtemp >= -273:
            self.__temp = newtemp
            return self.__temp
        else:
            raise ValueError("Enter Valid Temperature")
        
    def ctof(self):
        res=(self.__temp*1.8)+32
        return f"{res} F"
    
s=Temperature(-300)

print(s.gettemp())
print(s.settemp(55))
print(s.ctof())
    