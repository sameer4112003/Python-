#Tuples are used to store multiple items in a single variable
#unchangeble or immutable
#to change tuple convert tuple to list and then list to tuple


tup = (10,20,30,40,50, 'Red','Blue','Green') 
y = ("orange")
tup += y
print(tup)
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[5-3])
print(tup[5-4])
if 'baby' in tup:
  print("Yup! it exist")
else:
  print("Nope! it doesn't exist")
tup2 = tup[2:7]
print(tup2)


tup = (10,20,30,40,50, 'Red','Blue','Green') 
y = list(tup)
y.remove("red")
tup=tuple(y)
print(tup)

#loop through tuple

thistuple = ("apple" , "banana" ,"cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

words = tuple(input("enter a tuple :"))

if all(x == word[0] for x in words):
  print("same")
else:
  print("not same")