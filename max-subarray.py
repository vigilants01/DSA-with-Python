class solution:
    def subarray(self,nums):
        max=-999999999
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            if sum > max:
                max = sum
            if sum < 0:
                sum = 0
        return max
    
s=solution()
nums=[1,-1,2,2,-3,-8,3,7,9]
print(s.subarray(nums))