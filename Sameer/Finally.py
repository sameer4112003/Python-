# Finally
def func():
 try:
  l = [ 1,2,3,4,5]
  i = int(input("Enter a value:"))
  print(l[i])
  return 1
 except:
  print("Invalid input")
  return 0
 finally:
  print("You've entered the quantum realm")

x= func()
print(x)