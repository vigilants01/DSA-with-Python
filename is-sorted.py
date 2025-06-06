def sort(arr):
    num = -1
    for i in arr:
        if i >= num:
            num = i
        else:
            return False 
    return True
        

arr=[1,2,3,4,5]
result=sort(arr)
if result == True:
    print("sorted")
else:
    print("not sorted")