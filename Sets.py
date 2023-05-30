#1. Add a list of elements to a set

New = set()
Elements = [10,20,30,40,50]
New.update(Elements)
print(Elements)


#2. Return a new set of identical items from two sets

set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
new_set = set1.intersection(set2)
print(new_set)


#3. Get Only unique items from two sets

set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
unique = set1.symmetric_difference(set2)
print(unique)


#4. Update the first set with items that don’t exist in the second set
set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
set1.update(set2-set1)
print(set1)


#5. Remove items from the set at once
set1 = {10,20,30,40,50}
set1.difference_update({20,30})
print(set1)


#6. Return a set of elements present in Set A or B, but not both

set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
unique = set1.symmetric_difference(set2)
print(unique)

#7. Check if two sets have any elements in common. If yes, display the common elements

set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
new_set = set1.intersection(set2)
print(new_set)



#8. Update set1 by adding items from set2, except common items

set1 = {10,20,30,40,50}
set2 = {10,20,30,70,80}
set1.update(set2 - set1)
print(set1)
