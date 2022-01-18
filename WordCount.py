introduction=input('introduce yourslef')
characterCount=0
wordCount=1
for i in introduction:
    characterCount+=1
    if(i==' '):
        wordCount+=1
print("number of words in the string",wordCount)
print("number of letters in the string",characterCount)