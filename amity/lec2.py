#wap to sum all the integer valuies of a list using a function
def sum(numbers):
 sum = 0
 for i  in numbers:
  sum = sum + i
 return (sum)

c= [5,6,7,1]
print("The sum is :",sum(c))

c= sum(5,6,7,1)
print(c)

#wap in python to check whether the no. is amstrong no. or not
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")