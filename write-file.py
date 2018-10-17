# 5.3 FILE HANDLING
# 5.3a

# Open new file for writing
f = open('temp','w')
for n in range(1,11):
    msg = 'This is test number ' + str(n) + '\n'
    f.write(msg)
f.close()

# Open file for reading
f = open('temp','r')
for line in f:
    print(line, end='')
f.close()
