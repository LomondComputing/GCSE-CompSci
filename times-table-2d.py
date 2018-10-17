# Ten times table stored as a two-dimensional list

table = [[r*c for r in range(1,11)] for c in range(1,11) ]

print('\t',end='')
for h in range(1,11):
    print(h,'\t',end='')
print('\n')

for row in table:
    print(row[0],'\t',end='')
    for col in row:
        print(col,'\t',end='')
        

              

