class solution:
    def missing(self,num):
        n=len(num)
        total=n*(n+1)//2
        return total-sum(num)

s=solution()
num=[0,1,2,3,4,5]
print(s.missing(num))