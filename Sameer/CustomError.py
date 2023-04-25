#Raising custom error

a = (input("Enter a value between 1 to 10 :"))

if(a=="quit"):
  print("You've entered the quantum realm")
elif(int(a)<1 or int(a)>10):
  raise ValueError("Invalid input")
