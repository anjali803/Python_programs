# python program to find the frequence in a given string
test_string="anjali"
all_freq={}
for i in test_string:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
print("Count of all characters in anjali is :\n "
      + str(all_freq))
        