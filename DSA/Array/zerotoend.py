class solution:
    def zerotoend(self,num):
        l=[]
        for i in num:
            if i == 0:
                l.append(i)
        return num+l