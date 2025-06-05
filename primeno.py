class solution:
    def prime(self,n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    def print(self,x):
        for num in range(2,x+1):
            if self.prime(num):
                print(num,end=' ')


s=solution()
s.print(10)

