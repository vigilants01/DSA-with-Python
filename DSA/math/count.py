class solution:
    def no_digit(self,num):
            count=0
            while(num>0):
                last_digit=num%10
                num=num//10
                count+=1
            return count
s=solution()
print(s.no_digit(1112))