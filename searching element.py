#searching an element and returning the index value
'''arr=list(map(int,input("Enter elements with spaces").split()))
search=int(input("Enter the element to be searches:"))
found=False
for i in range(len(arr)):
    if arr[i]== search:
        print("Element found at index:",i)
        found=True
        break
if not found:
    print("Element not found!!!")'''

#using string
'''arr=input("Enter elements with spaces")
search=input("Enter the element to be searches:")
found=False
for i in range(len(arr)):
    if arr[i]== search:
        print("Element found at index:",i)
        found=True
        break
if not found:
    print("Element not found!!!")'''

'''arr=list(map(int,input("Enter elements with spaces").split()))
search=int(input("enter the element to be searches"))
found=False
for i in range(len(arr)):
    if arr[i]>search:
        print("greater elements",i)
        found=True
        continue
if not found:
    print("Element not found!!!")'''

#frequency for all occurances
'''arr=list(map(int,input("enter numbers:").split()))
freq={}
for num in arr:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
for key in freq:
    print(key,":",freq[key],"times.")'''

#finding missing number
'''arr=list(map(int,input("Enter the numbers").split()))
n=int(input("Enter total number count:"))
e_sum=n*(n+1)//2
o_sum=sum(arr)
print("Missing nymber:",e_sum-o_sum)'''
