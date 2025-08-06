num=342
n=int(str(num)[::-1])
print(n)

class solution:
    def rev(self,num):
        resv=0
        while(num>0):
            lastdigit=num%10
            num=num//10
            resv=(resv*10)+lastdigit
        return resv
s=solution()
num=74646
print(s.rev(num))