class Solution:
    def printGfg(self, n,count=1):
        if count > n:
            return
        else:
            print("GFG",end=' ')
            self.printGfg(n,count+1)
        