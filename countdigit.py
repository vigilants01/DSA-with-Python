class solution:
    def digit(self,num):
        count=0
        while(num>0):
            lastdigit=num%10
            num=num//10
            count+=1
        return count
        
s=solution()
num=12
print(s.digit(num))