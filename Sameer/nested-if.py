a = int(input("Enter a number : "))
print("Your number is :", a)

if(a<0):
  print("The number is -ve")
elif(a>0):
  if(a<=10):
    print("The number lies between 1-10")
  elif(a>10 and a<=20):
    print("The number lies between 11-20")
  else:
    print("The number is greater than 20")
else:
  print("The number is equal to zero")