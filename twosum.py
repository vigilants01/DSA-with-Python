class solution:
    def twosum(self,nums,target):
        mem={}

        for i,num in enumerate(nums):
            complement=target - num

            if complement in mem:
                return [mem[complement],i]
            mem[num]=i

s=solution()

nums=[1,2,3,4]
print(s.twosum(nums,target=6))