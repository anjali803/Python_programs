
names = ("anjali","kp","akshi")
newnames = list(names)
newnames[2]="aswathi"
names=tuple(newnames)
print(names)

fruits = ("apple","orange") #tuple
newfruits = list(fruits) #converting to list
newfruits[1] = "mango" #adding to the list
fruits = tuple(newfruits) #converting back to tuple
print(fruits)

#add tuple to a tuple
names = ("anjali","anusree","vyshnav")
newnames = ("vigil","amalia")
names += newnames
print(names)

# removing items from the tuple
veg=("carrot","tomato")
newveg=list(veg)
newveg.remove("tomato")
veg=tuple(newveg)
print(veg)


person = ("anjali","kp")
(female,male)=person 
print(female)
print(male)