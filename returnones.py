class solution:
    def ones(self,nums):
        for i in range(0,len(nums)):
            num=nums[i]
            count=0
            for i in range(0,len(nums)):
                if nums[i] == num:
                    count+=1
            if count == 1:
                return num
s=solution()
nums=[1,1,2,3,2]
print(s.ones(nums))