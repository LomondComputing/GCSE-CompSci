names = [ "Robert", "Boris", "Brad", "George", "David"]

n = 5
k = 0

print(names)

while k < n//2:
    temp = names[k]
    names[k] = names[n-k-1]
    names[n-k-1] = temp
    k += 1
    print(names)
    
