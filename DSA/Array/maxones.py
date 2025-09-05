class solution:
    def mcount(self,num):
        count=0
        max=0
        for i in num:
            if i == 1:
                count+=1
                if count > max:
                    max = count
            else:
                count=0
        return max
    
s=solution()
num = [1,1,0,1,1,1]
print(s.mcount(num))