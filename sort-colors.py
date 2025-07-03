class solution:
    def sortcolors(self,nums):
        low=0
        mid=0
        high=len(nums)-1
        while(mid<=high):
            if nums[mid] == 0:
                nums[low],nums[mid]=nums[mid],nums[low]
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[high]=nums[high],nums[mid]
                high-=1
        return nums

s=solution()
nums=[1,1,0,0,2,0,2,1,0]
print(s.sortcolors(nums))