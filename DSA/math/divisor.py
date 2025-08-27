class solution:
    def divisor(self,num):
        for i in range(1,num+1):
            if num%i == 0:
                print(i,end=",")
            else:
                continue

s=solution()
s.divisor(36)