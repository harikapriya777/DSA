#Hallowsquare pattern
'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==j or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''


'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or j==i or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if j==i or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''n= int(input("enter the value of n:"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==j or (i+j)==n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()'''