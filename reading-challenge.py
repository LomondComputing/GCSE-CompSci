# 5.3 FILE HANDLING
# 5.3d

# Open file for reading
f = open('sent.txt','r')
s = ''
spaceFound = False

while not spaceFound:
    char = f.read(1)
    if char == ' ':
        spaceFound = True
    else:
        s += char
        
print(s)

f.close()
