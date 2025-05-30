def greatest(arr):
    greatest=arr[0]
    for num in arr:
        if num>greatest:
            greatest=num
    return greatest
arr=[10,23,45,66,75,5,6,7,4,6,4,3,66,99]
print("Greatest Element",greatest(arr))



