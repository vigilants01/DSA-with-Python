class solution:
    def maximum(self,nums):
        max=0
        count=1
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
                if count > max:
                    max = count
            else:
                count=0
        return max

s=solution()
nums=[1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1]
print(s.maximum(nums))
        