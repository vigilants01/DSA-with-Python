class solution:
    def alter(self,nums):
        pos=[]
        neg=[]
        for i in range(0,len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        res=[]
        for i in range(len(pos)):
            res.append(pos[i])
            res.append(neg[i])
        return res
s=solution()
nums = [3,1,-2,-5,2,-4]
print(s.alter(nums))