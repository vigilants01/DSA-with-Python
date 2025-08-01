class solution:
    def pal(self,arr):
        i=0
        j=len(arr)-1
        ans=0
        while i<=j:
            if arr[i] < arr[j]:
                i+=1
                arr[i]+=arr[i-1]
                ans+=1
            elif arr[i] == arr[j]:
                i+=1
                j-=1
            else:
                j-=1
                arr[j]+=arr[j+1]
                ans+=1
        return ans
s=solution()
arr=[1,2,3,1]
print(s.pal(arr))