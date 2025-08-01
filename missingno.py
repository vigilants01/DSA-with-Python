class solution:
    def missing(self,nums):
        n=len(nums)
        target=n*(n+1)//2
        return target - sum(nums)
s=solution()
nums=[0,1,2,4]
print(s.missing(nums))