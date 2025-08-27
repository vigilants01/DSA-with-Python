class solution:
    def largest(self,num):
        greatest=num[0]
        for i in range(0,len(num)):
            if num[i] >= greatest:
                greatest=num[i]
        slargest=0
        for i in range(0,len(num)):
            if num[i]>=slargest and num[i] != greatest:
                slargest=num[i]
        return slargest    
s=solution()
num=[1,4,5,3,4,9]
print(s.largest(num))