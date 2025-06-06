def greatest(arr):
    great=arr[0]
    for i in arr:
        if i > great:
            great = i
    slarge=-1
    for i in arr:
        if i > slarge and i!=great:
            slarge = i
    return slarge
        

arr=[1,4,5,45,4,100,99,100,101,102]
print("secondlargest = ", greatest(arr))