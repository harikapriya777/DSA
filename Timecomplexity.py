# Time complexity
'''n-> n/2-> n/4->
O(logn)

def expo(a,b):
    if b==0:
        return 1
    elif b%2==0:
        return expo(a,b//2)**2
    else:
        return a*expo(a,b-1)
    expo(2,10) -> 1024
    O(n2)'''

#space complexity

'''a=10
print("A address:",id(a))
b=20
print("B address:",id(b))
c=a+b
print(c)
print("c address:",id(c))'''

#number manipulations

'''num=int(input("Enter a number:"))
copy=num
s=0
while num!=0:
    r=num%10
    s+=r*r*r
    num//=10
if copy==s:
    print(copy,"is an arm strong number")
else:
    print(copy,"is not an arm strong number")'''

#task
'''num=int(input("Enter a number:"))
copy=num
s=0
while num!=0:
    r=num%10
    s+=r
    num//=10

if copy%s==0:
    print(copy,"is an niven's number")
else:
    print(copy,"is not an niven's number")'''

#factorial

'''num=int(input("Enter a number:"))
fact=1
i=1
while i<=num: #1<=3#2<=3 #3<=3 #4<=3
    fact*=i #fact=1*1=1,fact=1*2=2, fact=1*2*3=6
    i+=1 #i=2 i=3 i=4
print(fact)'''

#strong number
'''num=int(input("Enter a number:"))
temp=num
sum=0
while temp>0:
    r=temp%10
    fact=1
    i=1
    while i<=r:
        fact*=i
        i+=1
    sum+=fact
    temp//=10
if sum==num:
    print("Strong number")
else:
    print("not")'''
