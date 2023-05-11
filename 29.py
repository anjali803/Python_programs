# Write a Python program to find the list of words that are longer than n from a given list of words. 


def word_length(n,str):
    word_len=[]
    txt = str.split(" ")
    for x in txt:
        if (len(x)>n):
            word_len.append(x)
    return word_len
print(word_length(3,"hello how are you"))