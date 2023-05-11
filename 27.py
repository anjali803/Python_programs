# Write a Python program to remove duplicates from a list

def newlist(list):
    unique_items = set()
    dupicate_items = []
    
    for a in list:
        if a not in list:
            dupicate_items.append(a)
            unique_items.add(a)
print(newlist([12,34,10,23,12])) 