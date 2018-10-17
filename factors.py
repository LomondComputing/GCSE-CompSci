# FACTORS

# recall that
# 30 div 7 = 4 (30 // 7)
# 30 mod 7 = 2 (30 % 7)

num = int(input('Which number? '))
f = 1           # the factor to try
factors = 0     # the number of factors
factorList = []

while f*f <= num:       # as long as we haven't got to square root
    if num % f == 0:    # if num is divisible by f
        d = num // f    # work out how many times it goes in
        print(num,'=',f,'*',d) # f and d are both factors
        if f not in factorList:
            factorList.append(f)
        if d not in factorList:
            factorList.append(d)

        if f == 1:      # if it's 1 then no increase in factors
            factors += 0 
        elif f == d:    # 
            factors += 1
        else:           # if must be two more factors 
            factors += 2

    f += 1      # go and try the next number

print(num,'has',factors,'factors')
factorList.sort()
print(factorList)
