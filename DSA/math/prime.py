class solution:
    def prime(self,num):
        d=[]
        for i in range(1,num+1):
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count==2:
                d.append(i)
                # print(i,end=",")
        return d

s=solution()
print(s.prime(30))