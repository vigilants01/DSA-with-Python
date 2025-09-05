class solution:
    def occur(self,num):
        for i in range(0,len(num)):
            count=0
            nums = num[i]
            for i in range(0,len(num)):
                if num[i] == nums:
                    count+=1
            if count == 1:
                return nums

s=solution()
num=[2,2,1]
print(s.occur(num))