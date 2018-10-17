import random

numQs = 5
score = 0
maxNum = 10

print('Welcome to Mr Gordon\'s Maths Quiz\n-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-')
numQs = int(input('How many questions do you want? ))
print('Maximum number is: ',maxNum)

for q in range(numQs):
        n1 = random.randint(1,maxNum)
        n2 = random.randint(1,maxNum)
        op = random.randint(0,1)
        if op == 0:
            sign = '+'
            ans = n1+n2
        else:
            sign = '-'
            ans = n1-n2
        print('Question',q+1)
        print('What is',n1,sign,n2,' ?')
        response = int(input())
        if response == ans:
            print('Yes, that is correct ...')
            score += 1
        else:
            print('Sorry, that is the wrong answer.')
            print('The correct answer is',ans)

percent = (score/numQs)*100
print('Quiz over\nYour final score was',score,'out of',numQs,'or',percent,'%')
if score == numQs:
    print('Congratulations. You have achieved the maximum score!')
