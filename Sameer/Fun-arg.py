#Required Arguments
#def CalculateAverage(a=12,b=14,c=1):
  #print("Average value is :", (a+b+c)/3)

#CalculateAverage(a=12 ,b=13)

#Arbitary
#def Average(*numbers):
# sum = 0
# for i  in numbers:
#  sum = sum + i
# print("Average :",sum/len(numbers))

#Average(5, 6,7,1)

#Return statement
def Average(*numbers):
 sum = 0
 for i  in numbers:
  sum = sum + i
 return sum/len(numbers)

c= Average(5,6,7,1)
print(c)