def reverse(a):
    length = len(a);
    halfLength = length//2
    for i in range(0,halfLength):
        swap(a,i,length-1-i)
    return a

def swap(a,x,y):
    temp = a[x]
    a[x] = a[y]
    a[y] = temp
