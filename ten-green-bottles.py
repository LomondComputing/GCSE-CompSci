# This program will print the words of "Ten Green Bottles"

bottles = 10
line1 = "green bottles hanging on the wall\n"
line3 = "and if one green bottle should accidentally fall\n"
line4 = "there'll be"

print(bottles,line1,bottles,line1,line3,line4)

for bottles in range(9,-1,-1):
    print(bottles,line1)
    print(bottles,line1,bottles,line1,line3,line4)
    
