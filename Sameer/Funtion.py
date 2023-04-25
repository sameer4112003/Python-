def calculateGmean(a,b):
  Mean = (a*b)/(a+b)
  print(Mean)

def isGreater(a,b):
  if(a>b):
    print("The value of a is greater")
  elif(a<b):
    print("The value of b is greater")
  else:
    print("The value of a and b are equal")

def subtraction(a,b):
  pass

a = 15
b = 13 
isGreater(a,b)
calculateGmean(a,b)

c = 12
d = 15
isGreater(c,d)
calculateGmean(c,d)

def calculate_factorial(number):
  if number == 0:
    return 1
  else:
    return number * calculate_factorial(number - 1)

number = int(input("Enter a number :"))
factorial = calculate_factorial(number)
print(number, "!=", factorial)


 