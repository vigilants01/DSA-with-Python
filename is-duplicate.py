def dup(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
            
    return i+1
arr=[1,1,3,3,4,4,5,5]

print(arr[:dup(arr)])

arr = [1, 1, 3, 3, 4, 4, 5, 5]
unique = list(set(arr))
print(unique)