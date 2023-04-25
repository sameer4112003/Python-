Marks = [50,60,70,80,90,45,25]
print(Marks)
print(Marks[0])
print(Marks[1])
print(Marks[2])
print(Marks[7-4])
print(Marks[7-3])
print(Marks[7-2])
print(Marks[7-1])

if 35 in Marks:
  print("Yes")
else:
  print("WAP")

print(Marks[1:5])

lst = [i for i in range(50) if i%2==0]
print(lst)