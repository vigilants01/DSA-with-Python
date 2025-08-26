class solution:
    def reverse(self,num):
        rev=0
        while(num>0):
            last_digit=num%10
            num=num//10
            rev=(rev*10)+last_digit
        return rev
    
s=solution()
print(s.reverse(123456789))