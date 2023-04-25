#1. Write a python program to reverse a list in Python.

Fruits = ['apple','mango','banana','strawberry','pineapple']
reversed_list = Fruits[::-1]
print(reversed_list)

#2. Write a python program to concatenate two lists index-wise.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = [list1[i] + list2[i]
for i in range(len(list1))]
print(concatenated_list)


#3. Write a python program to turn every item on a list into its square

List = [ 5 , 7 , 9 , 11, 13]
squared_list = [i**2 for i in List]
print(squared_list)

#4. Write a python program to iterate both lists simultaneously.

L1 = [10 ,20 , 30]
L2 = [40, 50 ,60]
for a , b in zip(L1,L2):
  print(a,b)
  

#5. Write a python program to remove empty strings from the list of strings.
list1 = ["Sameer", "", "Ramesh", "", "Bekawade", ""]
list1 = list(filter(lambda x: x != "",list1))
print(list1)

  
#6.Write a python program to add a new item to the list after a specified item.

Students = ['John','Harry','Scott']
Insert_after = 'Harry'
Insert_student = 'Samuel'
Index = Students.index(Insert_after)
Students.insert(Index + 1,Insert_student)
print(Students)


#7. Write a python program to extend the nested list by adding the sublist

Numbered_list = [[24,34], [54,64]]
sublist = [44,64], [77,88]
Numbered_list.extend([sublist])
print(Numbered_list)

#8. Write a python program to replace the list’s item with a new value if found.

Employee = ['John','Harry','Scott']
replace = 'John'
New_employee = 'Sam'
if replace in  Employee:
  Index = Employee.index(replace)
  Employee[Index] = New_employee
print(Employee)

#9. Write a python program to remove all occurrences of a specific item from a list.

my_list = [1, 2, 3, 4, 3, 5, 3]
item_to_remove = 3
my_list = list(filter(lambda x: x != item_to_remove, my_list))
print(my_list)

#WAP to check the password strength by the user using function whetehr the password consist min 8 characters i.e uppercase,lowercas,special character

password = input("Enter a password :")

if len(password) >=8:
  if any(char.isdigit() for char in password):
    if any(char.isupper() for char in password):
      print("Password meets all criteria")
    else:
      print("Password must contains atleast One uppercase needed")
  else:
    print("Password must contains atleast one digit needed")
else:
  print("Password must contains atleast 8 characters long")

#WAP that determines wheteher entered number is amstring number or not using while Loop
def amstrong_number(n):
  num_str = str(n)
  num_len = len(num_str)

total = 0
for digit in str:
  total += int(digit) 