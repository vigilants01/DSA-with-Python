class solution:
    def ones(self,nums):
        count=0
        max=0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                count+=1
                if count > max:
                    max = count
            else:
                count=0
        return max
s=solution()
nums=[1,1,2,3,1,1,1,1,1]
print(s.ones(nums))