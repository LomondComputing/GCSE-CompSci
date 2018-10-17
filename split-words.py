# Program to split an input sentence into all available substrings


def countWords(s):
    newS = s.strip()
    wordList = newS.split(' ')
    return len(wordList)

def findSubstrings(s):
    numWords = countWords(s)
    wordList = s.split(' ')
    substringList = []

    for i in range(numWords):
        substring = wordList[i]
        substringList.append(substring)
        for j in range(i+1,numWords):
            substring = substring + " " + wordList[j]
            substringList.append(substring)       
    return substringList

phrase = input('Enter a phrase or sentence: ')
print('Number of words: ',countWords(phrase))
substrings = findSubstrings(phrase)
print('Number of substrings: ', len(substrings))
print('Substrings: ',substrings)


    
        
     

    

