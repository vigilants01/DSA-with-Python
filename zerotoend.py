class solution:
    def zero(self,nums):
        n=len(nums)
        tmp=[]
        for i in range(0,n):
            if nums[i] != 0:
                tmp.append(nums[i])
        for i in range(len(tmp)):
            nums[i]=tmp[i]
        for i in range(len(tmp),n):
            nums[i] = 0
        return nums
s=solution()
nums=[1,0,3,0,4,0,6,7]
print(s.zero(nums))