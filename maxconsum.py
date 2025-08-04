class solution:
    def con(self,nums):
        max=-99999999
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum >=0:
                if sum > max:
                    max=sum
            else:
                sum=0
        return max
s=solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.con(nums))
