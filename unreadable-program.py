# Apply the Python style guide to this program to make it more readable
# What is the program actually doing?
def whatDoesThisDo(cheese,spam):
    peter=0                                         
    fred=False                                   
    lolly=len(spam)
    while (peter<lolly)and(not fred):
        if spam[peter]==cheese:fred=True                             
        else:peter+=1
    if not fred:peter=-1
    return peter
n=[]
x=input()
while x!='xxx':
    n.append(x)
    x=input()                              
y = input()
z = whatDoesThisDo(y,n)
print(z)
