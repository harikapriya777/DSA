#flip sort Pancake
'''def flip(arr,k):
    start=0
    while start<k:
        arr[start],arr[k]=arr[k],arr[start]
        start=-1
        k-=1
def pancake(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        max_index=0
        for j in range(1,i+1):
            if arr[j]>arr[max_index]:
                max_index=j
            if max_index!=0:
                flip(arr,i)
    return arr
arr=list(map(int,input("Enter elements:").split()))
sortedarray=pancake(arr)
print("Sorted array",sortedarray)'''

#Quick sort
def quick(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick(arr,low,pi-1)
        quick(arr,pi+1,high)
def partition(arr,low,high):
    piviot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<piviot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=list(map(int,input("Enter elements:").split()))
quick(arr,0,len(arr)-1)
print("Sorted array",arr)