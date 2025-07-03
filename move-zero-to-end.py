def solution(nums):
    a=[]
    b=[]
    for i in range(0,len(nums)):
        if nums[i]==0:
            a.append(nums[i])
        else:
            b.append(nums[i])
    return b+a

nums=[1,0,2,0,3,0,3,4,5]
print(solution(nums))