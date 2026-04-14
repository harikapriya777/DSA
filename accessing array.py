#accessing an array element using index
'''arr=list(map(int,input("Enter the elements of the array:").split()))
print(arr[2])
print(arr[-2])'''

#travel of an array
'''arr=list(map(int,input("Enter the elements of the array:").split()))
for i in range(len(arr)):
    print(arr[i], end="->")'''

'''arr=list(map(int,input("Enter the elements of the array:").split()))
for i in range(len(arr)):
    print(arr[i]+1, end="->")'''

#program to find the minimum value in a user defined array
'''arr=list(map(int,input("Enter the elements of the array:").split()))
min_value= arr[0]
for i in arr:
    if i<min_value:
        min_value=i
print(min_value)'''

#program to find the maximum value in a user defined array
'''arr=list(map(int,input("Enter the elements of the array:").split()))
max_value= arr[0]
for i in arr:
    if i>max_value:
        max_value=i
print(max_value)'''

#program to reverse the words in a string
'''words= input("Enter the words:").split()
for word in words:
    print(word[::-1],end=" ")'''

#program to find the smallest word lexcographically from the given list of words
'''words= input("Enter the words:").split()
min_word= words[0]
for word in words:
    if word<min_word:
        min_word=word
print("Smallest word is:",min_word)'''

#Encrypt the word using ceaser cipher
'''word=input("Enter a word:")
key=int(input("Enter a key:"))
result= ""
for ch in word:
    if ch.isalpha():
        if ch.lower():
            new= chr(ord(ch)+key)
            result+= new
        else:
            new=chr(ord(ch)+key)
            result+= new
print(result)'''




