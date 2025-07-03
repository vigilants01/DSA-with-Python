class solution:
    def twosum(self,nums,target):
        mem={}
        for i,n in enumerate (nums):
            t=target-n
            if t in mem:
                return (mem[t],i)
            mem[n]=i



s=solution()

nums=[1,2,3,4]
print(s.twosum(nums,target=6))