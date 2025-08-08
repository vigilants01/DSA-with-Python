class ComplexNumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __add__(self,other):
        resultReal=0
        resultImage=0
        resultReal=self.real+other.real
        resultImage=self.imag+other.imag
        ans=ComplexNumber(resultReal,resultImage)
        return ans
    def __sub__(self,other):
        resultReal=0
        resultImage=0
        resultReal=self.real-other.real
        resultImage=self.imag-other.imag
        ans=ComplexNumber(resultReal,resultImage)
        return ans
    def __mul__(self,other):
        resultReal=0
        resultImage=0
        resultReal=self.real*other.real - self.imag*other.imag
        resultImage=self.real*other.imag + self.imag*other.real
        ans=ComplexNumber(resultReal,resultImage)
        return ans

    def __str__(self):
        if self.real == 0:
            s=f"({self.imag}i)"
            return s
        elif self.imag<0:
            s=f"({self.real}{self.imag}i)"
            return s
        else:
            s=f"({self.real}+{self.imag}i)"
            return s

    def conjucate(self):
        return ComplexNumber(self.real,-1*self.imag)

s1=ComplexNumber(2,-4)
s2=ComplexNumber(1,4)
s=s1*s2
print(s)


