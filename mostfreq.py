from collections import Counter

class solution:
    def mostfreq(self,arr):
        counter=Counter(arr)
        most_com=counter.most_common(1)[0]
        return most_com

s=solution()
s.mostfreq
arr=[1,1,1,2,2,5,7,9,0,0,0,0,0,0,0,0,]
most_common = s.mostfreq(arr)
print("Element with highest frequency:", most_common[0])
print("Frequency:", most_common[1])