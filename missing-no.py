class solution:
    def missing(self,nums):
        n = len(nums)
        total = n * (n+1) // 2
        return total - sum(nums)
    
s=solution()
nums=[0,1,2,4,5]
print(s.missing(nums))