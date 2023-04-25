#wap to get the fourth element in a tuple  from the last 

a = (1,2,3,4,5,'red','yellow','blue')
print(a)
i = a[3]
print("The fourth element:",i)
j = a[-3]
print("The fourth last element:",j)

#wap to unpack a tuple where the no. of values are more than the no. of variables.

#create a function in python where the local and global variable have the same name but having different value

#reverse  a string
txt = "technicia"[::-1] 
print(txt)

def multiply(numbers):
  total = 1
  for x in numbers:
    total *= x
  return total
print(multiply((8,2,7,-1,7)))


#wap  a program in python to swap two tuples
a = 50 
b = 60
print("before swap",a)
print("before swap",b)

t=a
a=b
b=a
print("after swap",a)
print("after swap",b)

#create a tuple with single item 50
#sort the tuple of tuples by second item
#change the last element of tuples in the list with 100


