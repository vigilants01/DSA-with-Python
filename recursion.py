class Solution:    
    def printNos(self,n,count=1):
        if count > n:
            return
        else:
            print(count,end=' ')
            self.printNos(n,count+1)