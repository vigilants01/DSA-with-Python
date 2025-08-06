class solution:
    def arm(self,num):
        sum=0
        check=num
        while(num>0):
            lastdigit=num%10
            sum+=(lastdigit*lastdigit*lastdigit)
            num=num//10
        if check == sum:
            return True
        else:
            return False
s=solution()
num=371
print(s.arm(num))