class solution:
    def stock(self,nums):
        mini=nums[0]
        profit=0
        for i in range(0,len(nums)):
            cost=nums[i] - mini
            mini=min(mini,nums[i])
            profit=max(profit,cost)
        return profit

s=solution()
nums= [7,1,5,3,6,4]
print(s.stock(nums))