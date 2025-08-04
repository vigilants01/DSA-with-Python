class solution:
    def colors(self,nums):
        low=0
        mid=0
        high=len(nums)-1
        while(mid<=high):
            if nums[mid] ==0:
                nums[low],nums[mid]=nums[mid],nums[low]
                mid+=1
                low+=1
            elif nums[mid] ==1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1

s=solution()
nums=[0,2,2,1,0,2,1,0]
s.colors(nums)
print(nums)