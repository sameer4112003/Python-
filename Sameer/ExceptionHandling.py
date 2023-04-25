#Exceptiion handling in python

a = input("Enter a number :")
print(f"The multiplication table of {a} is:")

try:
 for i in range (1,11):
  print(f"{int (a)} * {i} = {int(a)*i}")
except:
  print("Invalid input")

print("Hey you entered the quantum realm")
9

try:
  num = int(input("Enter a value : "))
  a = [4,5]
  print(a[num])
except ValueError:
  print("The value entered is not an integer")
except IndexError:
  print("Please enter valid input")