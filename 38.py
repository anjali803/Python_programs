# python programto find the number od occurrence of letters in a sentence
name=input("Enter your string")
count=dict() 
words=str.split(name)
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)
