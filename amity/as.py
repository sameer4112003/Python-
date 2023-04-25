#1. Add a list of elements to a set

New_set = set()
Elements = [10,20,30,40,50,60,70,80,90,100]
New_set.update(Elements)
print(Elements)


#2. Return a new set of identical items from two sets

set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
Identical = set1.intersection(set2)
print(Identical)

#3. Get Only unique items from two sets
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
unique = set1.symmetric_difference(set2)
print(unique)

#4. Update the first set with items that don’t exist in the second set
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
set1.update(set2 - set1)
print(set1)

#5. Remove items from the set at once
set1 = {1,2,3,4,5,6,7,8}
set1.difference_update({4,5,6})
print(set1)

#6. Return a set of elements present in Set A or B, but not both
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
unique = set1.symmetric_difference(set2)
print(unique)


#7. Check if two sets have any elements in common. If yes, display the common elements
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
x = set1.intersection(set2)
print(x)

#8. Update set1 by adding items from set2, except common items
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
set1.update(set2 - set1)
print(set1)

#9. Remove items from set1 that are not common to both set1 and set2
set1 = {1,2,3,4,5,6,7,8}
set2 = {3,4,5,6,9,10,11,12}
x = set1.intersection_update(set2)
print(x)

#1. Write a Python program to concatenate the following dic7onaries to create a new one: dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50, 6:60}

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

new_dict = {}
for d in [dic1, dic2, dic3]:
    new_dict.update(d)

print(new_dict)

#2. Write a Python program to remove a key from a dic7onary.
Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
Dict.pop('Ashutosh')
print(Dict)

#3. Write a Python program to get a dic7onary's maximum and minimum values.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
Maximum_value =max(Dict.values())
Minimum_value = min(Dict.values())

print("Maximum values :",{Maximum_value})
print("Minimum values :",{Minimum_value})




#4. Write a Python program to find the sum of all items in a dic7onary.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
Sum = sum(Dict.values())
print(Sum)

#5. Write a Python program to sort a dic7onary by value.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
sorted = {k: v for k, v in sorted(Dict.items(), key=lambda item: item[1])}
print(sorted)


#6. Write a Python program to check whether a given key already exists in a dic7onary.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
key = 'Ashutosh'

if key in Dict:
  print("Exist")
else:
  print("doesn't exist")

#7. Write a Python program to count the number of items in a dic7onary.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230
}
count = len(Dict)
print(count)

#8. Write a Python program to print all unique values in a dic7onary.

Dict = {
  'Sam': 100,
  'Ashutosh' : 200,
  'Sankalp' : 230,
  'Weekend' : 200
}

unique_values = set(Dict.values())

print(unique_values)