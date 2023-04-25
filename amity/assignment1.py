#Write a python program to find the GCD of two numbers.

def gcd(a,b):
  
  if(b==0):
    return a
  else:
    return gcd(b, a%b)

print(gcd(12,24))
print(gcd(18,36))


#Write a python program to check whether the entered number is a palindrome or not.

num = int(input("Enter a number :"))

reverse_num = str(num) [::-1]

if(str(num)==reverse_num):
  print("The number is palindrome")
else:
  print("The number is not palindrome")


#Write a python program using the function to perform the multiplication of two matrices.

import numpy as no

matrix1 = no.array([[12,13] , [15,16]])
matrix2 = no.array([[24,25] , [26,27]])

result = no.dot(matrix1 , matrix2)
print(result)

#Write a python program to design a function to calculate the sum of a list's integer elements.

Integers = [10,20,30]
total = sum(Integers)
print(total)

