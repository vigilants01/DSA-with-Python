class solution:
    def sum(self,n,sum=0):
        if n < 1:
            print(sum)
            return
        else:
            self.sum(n-1,sum+n)

s=solution()
s.sum(3)