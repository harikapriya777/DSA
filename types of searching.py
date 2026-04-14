'''arr=list(map(int,input("Enter the elements:").split()))
target=int(input("Enter element to be searched:"))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index:",i)
        found=True
        break
if not found:
    print("Element not found!!!!!")'''

#unsorted array
'''arr=list(map(int,input("Enter the elements:").split()))
arr.sort()
target=int(input("Enter element to be searched:"))
found=False
left=0
right=len(arr)-1
while left<=right:
    mid=(left+right)//2
    if arr[mid]==target:
        print("Element found at index:",mid)
        found=True
        break
    elif target<arr[mid]:
        right=mid-1
    else:
        left=mid+1
if not found:
    print("Element not found!!!!!")+3'''
