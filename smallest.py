lst = [1,2,3,4,5,6,7,8,9,10,-1]

smallest = lst[0]
biggest = lst[0]

for i in lst:
    if i < smallest:
        smallest = i
    if i > biggest:
        biggest = i

print(smallest)
print(biggest)
