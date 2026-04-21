#operations insert
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def delete(value):
    global head
    temp=head
    if temp and temp.data==value:
        head=temp.next
        return
    prev=None
    while temp and temp.data!=value:
        prev=temp
        temp=temp.next
    if temp is None:
        print("Value not in linkedlist......😑")
        return
    prev.next=temp.next
    print("Deleted value:",value)
def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("Inserted linkedlist:")
display()
key=int(input("Enter the value of node to be deleted"))
delete(key)
print("\n Updated Linkedlist:")
display()'''

#search key
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def search(key):
    temp=head
    position=1
    while temp:
        if temp.data==key:
            print("Element found in node:",position)
            return
        temp=temp.next
        position+=1
    print("No node reflects they key......")
def display():
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("Inserted linkedlist:")
display()
key=int(input("Enter the value of node to be deleted"))
print("\n Updated Linkedlist:")
display()'''

#reverse
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode

def delete(value):
    global head
    temp=head
    if temp and temp.data==value:
        head=temp.next
        return
    prev=None
    while temp and temp.data!=value:
        prev=temp
        temp=temp.next
    if temp is None:
        print("Value not in linkedlist......😭")
        return
    prev.next=temp.next
    print("Deleted value:",value)

def display():
    temp=head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("None") 
def reverse():
    global head
    prev=None
    curr=head
    while curr:
        nextnode=curr.next
        curr.next=prev
        prev=curr
        curr=nextnode
    head=prev    
n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)

print("Inserted linkedlist:")
display()
reverse()
print("\n Updated Linkedlist:")
display()'''

#replace element in a single linked list

'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def replace(old,new):
    temp=head
    found=False
    while temp:
        if temp.data==old:
            temp.data=new
            found-True
        temp=temp.next
    if found:
        print("Replaced",old,"with",new)
    else:
        print("Vlue not found in SLL")
def display():
    temp= head
    while temp:
        print(temp.data,end ="->")
        temp=temp.next
    print("Tail") 
n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("\n Linked list: ")
display()
old=int(input("Enter value to replace:"))
new=int(input("Enter new value:"))
replace(old, new)
print("\n Updated list")
display()'''

#testing(create cycle)
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
head=None
def insert(data):
    global head
    newnode=node(data)
    if head is None:
        head=newnode
        return
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=newnode
def createcycle(pos):
    global head
    if pos==-1:
       return
    temp=head
    cyclenode=None
    index=0
    while temp.next:
        if index==pos:
            cyclenode=temp
        temp=temp.next
        index+=1
    if cyclenode:
        temp.next=cyclenode
def detectcycle():
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            print("Cycle detected")
            return
    print("no cycle")
def display(limit=15):
    temp=head
    count=0
    while temp and count<limit:
        print(temp.data, end="->")
        temp=temp.next
        count+=1
    print("..." if temp else "None")
n=int(input("Enter number of nodes:"))
for _ in range(n):
    val=int(input("Enter value:"))
    insert(val)
print("\n Linked list:")
display()
pos= int(input("Enter a position"))
createcycle(pos)
detectcycle()


