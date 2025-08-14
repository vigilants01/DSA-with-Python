def sum2(a,b):
    res=a+b
    return res
print(sum2(2,3))
def sum1(a,b,c):
    res=a+b+c
    return res
print(sum1(2,3,7))
def sum(a,b,c=0):
    if c!=0:
        return sum1(a,b,c)
    else:
        return sum2(a,b)
print(sum(2,3))
