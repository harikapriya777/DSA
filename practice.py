#find missing number
arr=list(map(int,input("Enter the numbers").split()))
n=int(input("Enter total number count:"))
e_sum=n*(n+1)//2
o_sum=sum(arr)
print("Missing nymber:",e_sum-o_sum)