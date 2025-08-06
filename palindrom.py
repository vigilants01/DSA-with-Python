# def pali(num):
#     n=int(str(num)[::-1])
#     if num == n:
#         return True
#     else:
#         return False
# num=121
# print(pali(num))

class solution:
    def drome(self,nums):
        check=nums
        resv=0
        while(nums>0):
            lastdigit=nums%10
            nums=nums//10
            resv=(resv*10)+lastdigit
        if check == resv:
            return True
        else:
            return False
s=solution()
nums=121
print(s.drome(nums))
