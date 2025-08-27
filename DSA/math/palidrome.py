class solution:
    def palidrome(self,num):
        original=num
        rev=0
        while(num>0):
            last_digit=num%10
            num=num//10
            rev=(rev*10)+last_digit
        return original==rev
s=solution()
print(s.palidrome(121))