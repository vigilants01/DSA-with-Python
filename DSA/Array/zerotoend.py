class solution:
    def zerotoend(self,num):
        l1=[]
        l2=[]
        for i in num:
            if i != 0:
                l1.append(i)
            else:
                l2.append(i)
        return l1+l2
    
s=solution()
num = [0,1,0,3,12]
print(s.zerotoend(num))