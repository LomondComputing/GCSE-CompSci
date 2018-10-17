def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    print("Quick sorting..",alist)
    if first<last:

       splitpoint = partition(alist,first,last)
    # This is a recursive call to the function
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
           print("Now swapping..",alist[leftmark],'with',alist[rightmark])

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   print("Now swapping..",alist[first],'with',alist[rightmark])


   return rightmark

alist = [54,26,93,17,77,31,44,55,20]
print('QUICKSORT...\nUnsorted list:',alist)
quickSort(alist)
print('Sorted list:',alist)
