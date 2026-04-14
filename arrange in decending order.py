'''n=int(input("Enter the size of array"))
a=[]
for i in range(n):
    ele=int(input("Enter the elements"))
    a.append(ele)
print("unsorted array",a)
for i in range(n):
    for j in range(i,n-1):
        if a[i]<a[j+1]:
            a[i],a[j+1]=a[j+1],a[i]
print("sorted array",a)'''
        
#arrange strings according to their len in decending order
'''n=int(input("Enter the value:"))
a=[]
for i in range(n):
    ele=(input("Enter the elements:"))
    a.append(ele)
print("unsorted array",a)
a.sort(key=lambda x: len(x),reverse=True)
print("sorted array",a)'''

