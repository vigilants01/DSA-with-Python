from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimeter():
        pass

class circle(shape):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        a=self.r*self.r
        return a

    def perimeter(self):
        p=2*self.r
        return p

    def details(self):
        a=self.area()
        p=self.perimeter()
        return f"Area and Perimeter of circle is: {a} and {p}"

class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        a=self.l*self.b
        return a

    def perimeter(self):
        p=2*(self.l+self.b)
        return p

    def details(self):
        a=self.area()
        p=self.perimeter()
        return f"Area and Perimeter of Rectangle is: {a} and {p}"
    
def get_details(value):
    for i in value:
        print(i.details())

s=[circle(56),rectangle(10,12)]
get_details(s)