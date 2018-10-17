thelist = [5,6,7,6,7,8,7,8,9,1,2,3,2,3,4,3,4,5]

count=0
highestFreq=0
mostFreqItem=0

print(thelist)

for i in range(0,len(thelist)):

    for j in range(i,len(thelist)):
        if count == 0 and thelist[j] != 0:
            item = thelist[j]
            count += 1
        elif thelist[j] == item:
            thelist[j] = 0
            count += 1

    if count > 1:
        print('Item:',item,'Frequency:',count)
        
    if count > highestFreq:
        highestFreq = count
        mostFreqItem = item
        
    count = 0
    
print(thelist)
print('Most frequent item:',mostFreqItem,'Frequency:',highestFreq)
              
              
    
