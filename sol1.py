class solution:
    def final_destination(self,path):
        x=0
        y=0
        i=0
        while i < len(path):
            dir = path[i]
            i+=1
            num =''
            while i < len(path) and path[i].isdigit():
                num+=path[i]
                i+=1
                steps=int(num)
                if dir == 'N':
                    y+=steps
                elif dir == 'S':
                    y-=steps
                elif dir == 'E':
                    x+=steps
                elif dir == 'W':
                    x-=steps
        return(x,y)
s=solution()
path='N9S4E8W2'
print(s.final_destination(path))
