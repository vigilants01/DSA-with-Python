class solution:
    def armstrong(self,num):
        sum=0
        power=len(str(num))
        original=num
        while(num>0):
            last_digit=num%10
            num=num//10
            sum+=last_digit**power
            # sum+=(last_digit*last_digit*last_digit)
        return original==sum
    
s=solution()
print(s.armstrong(9474))

