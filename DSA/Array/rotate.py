class solution:
    def rotate(self,num,k):
        num[:] = num[-k:]+num[:-k]
        return num
    
s=solution()
num=[1,2,3,4,5,6,7]
print(s.rotate(num,1))