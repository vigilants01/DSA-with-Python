class solution:
    def divisor(self,num):
        count=0
        for i in range(1,num+1):
            if num % i == 0:
                count+=1
        if count ==2:
            print("Prime number")
        else:
            print("not a prime number")
s=solution()
num=11
s.divisor(num)