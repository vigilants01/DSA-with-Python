class solution:
    def duplicates(self,nums):
        res=[]
        for i in nums:
            if i not in res:
                res.append(i)
        return res
    
s=solution()
nums=[0,0,1,1,2,2,3,3]
print(s.duplicates(nums))
