class solution:
    def majority(self,nums):
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for key in d:
            n=len(nums)
            if d[key] > n/2:
                return key
            
s=solution()
nums=[1,1,1,1,1,1,1,2,2,2,3,4]
print(s.majority(nums))