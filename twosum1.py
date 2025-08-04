class solution:
    def two(self,nums,target):
        a={}
        for i,n in enumerate(nums):
            t=target-n
            if t in a:
                return(a[t],i)
            a[n]=i
s=solution()
nums=[2,7,11,15]
print(s.two(nums,9))
