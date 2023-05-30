

#Q1. Write a program that reads in a list of student records, where each item in the list is a tuple
# containing the student's name, age, and grades in three subjects. The program should then calculate
# the average grade for each student and print out a report showing the student's name, age, and average
# grade sorted by average grade.

student_records = [
    ("Sameer",19,(70,80,90)),
    ("Himansu",19,(50,60,70)),
    ("Sankalp",19,(40,50,60))
]

student_grade = []

for records in student_records:
    name , age , grade = records
    avg_grade = sum(grade)/len(grade)
    student_grade.append((name , age, avg_grade))

sorted_grade = sorted(student_grade,key=lambda x: x[2])

for grade in sorted_grade:
    name, age , avg_grade = grade
    print(f"Name:{name} , Age:{age} , Average Score:{avg_grade}")

#Write a program that checks whether a given string is a palindrome or not.
# Use strings and loops to implement the palindrome check.

def palindrome(string):
    string = string.lower()
    reversed_str = string[::-1]
    if reversed_str == string:
        return  True
    else:
        return False

User_input = str(input("Enter a string : "))

if palindrome(User_input):
    print(f"{User_input} is palindrome")
else:
    print(f"{User_input} is not palindrome")



#Q3. Write a program that takes two sets of numbers as input and returns a new set containing only the
# elements that are present in one of the input sets, but not both.

set1 = {10,20,30,40,50,60,70}
set2 = {30,40,50,90,88,3,3,4,233}

unique = set1.symmetric_difference(set2)
print(unique)


#Q4. Write a function to convert a given decimal number to binary and binary to decimal.

def decimal_to_binary(decimal):
    binary = bin(decimal).replace("0b" , "")
    return binary

def binary_to_decimal(binary):
    decimal = int(binary , 2)
    return decimal

decimal_number = 20
binary_number = "1011"
converted_decimal = binary_to_decimal(binary_number)
converted_binary = decimal_to_binary(decimal_number)
print("Decimal to Binary : ", converted_binary)
print("Binary to Decimal : ", converted_decimal)


#Q1. Python program to generate a random number and let the user guess it:

#import random

#def guess_number():
#    random_number = random.randint(1,10)
#    guess = 0

#    while True:
#        User_input = int(input("Enter a number : "))
#        guess += 1

#        if guess < random_number:
#            print("Too Low!")
#        elif guess > random_number:
#            print("Too High!")
#        else:
  #          print("Congratulations! You've won")
#
#    print("Number of guesses",guess)

#guess_number()

#Q2. Python program to split a string into tokens (words) based on whitespace:

def split_string(input_string):
    token = input_string.split()
    return token

input_string = str(input("Enter a string : "))
result = split_string(input_string)
print("Tokens:",result)

# Python program to filter out even numbers from a list:

def filter(numbers):
    filter_number = []
    for num in numbers:
        if num %2 != 0 :
            filter_number.append(num)
    return filter_number

user_inp = [1,2,3,4,5,6,7,8,9,10]
result_even = filter(user_inp)
print("The filtered out list : ",result_even)

#Python program to create a new list containing only the even numbers using list comprehension:

def filter(numbers):
    filter_number = []
    for num in numbers:
        if num %2 == 0 :
            filter_number.append(num)
    return filter_number

user_inp = [1,2,3,4,5,6,7,8,9,10]
result_even = filter(user_inp)
print("The filtered out list : ",result_even)

#Q1. Python program for managing shopping lists:

def create_shopping_list():
    shopping_list = []
    while True:
       item = input("Enter a item to add (or 'q' to quit) :")
       if item == 'q':
          break
       shopping_list.append(item)
       print("Shopping list :",shopping_list)
    return shopping_list

def remove_shopping_item(shopping_list):
    item = input("Enter the item you want to remove :")
    if item == shopping_list:
        shopping_list.remove(item)
        print("The item has been sucessfully removed")
    else:
        print("The item is not in shopping list")
    print("Shopping list :",shopping_list)

def update_shopping_list(shopping_list):
    item = input("Enter a item which you want to update :")
    if item == shopping_list:
        index = shopping_list.index(item)
        quantity = input("Enter the new quantity :")
        shopping_list[index] = (item,quantity)
        print("The list has been updated successfully")
    else:
        print("The item is not in list")
    print("Shopping list :",shopping_list)

def merge_list(list1,list2):
    merged_list = list1 + list2
    merged_list = list(set(merged_list))
    return merged_list


shopping_list1 = (create_shopping_list())
remove_shopping_item(shopping_list1)
update_shopping_list(shopping_list1)

shopping_list2 = create_shopping_list()
merged_list = merge_list(shopping_list1,shopping_list2)
print("Merged list :",merged_list)

# Python program to find common elements in multiple sets:

def find_comman_elements(sets):
    comman_elements = sets[0]
    for s in set[1:]:
        common_elements = common_elements.intersection(s)
    return comman_elements

set1 = {1,2,3,4,5}
set2 = {6,7,88,9,5}
set3 = {99,00,77,5}

common = find_comman_elements([set1,set2,set3])
print("Enter common elements :",common)








