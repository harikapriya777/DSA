#sortings
#1.Bubble sorting
'''arr=list(map(int,input("Enter elements:").split()))
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Sorted array",arr)'''

#2. selection sort
arr=list(map(int,input("Enter elements:").split()))
n=len(arr)
for i in range(n):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print("sorted array",arr)