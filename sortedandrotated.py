class solution:
    def rotate(self,nums):
        drop=0
        n=len(nums)
        for i in range(0,n):
            if nums[i] > nums[(i+1)%n]:
                drop+=1
                if drop > 1:
                    return False
        return True
        
s=solution()
nums=[3,4,5,1,2]
print(s.rotate(nums))
            