#1
set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

print("set1 U set2 :",set1.union(set2))
print("Intersection :",set1.intersection(set2))

#2
List = [1,2,3,4,5,5,4,6,7,8]
Set = set(List)
New_list = list(Set)
print(New_list)

#3
prime_numbers = {2,3,5,7,11}

User_input = int(input("Enter a value :"))

if User_input in prime_numbers:
  print(User_input,"The entered value is a prime number")
else:
  print(User_input,"The entered value is not a part of set")

#4

Fruits = {
  'Apple': 500,
  'Mango': 1000,
  'Banana': 250,
  'Watermelon': 300,
  'Chickoo': 450
}

user_input = input("Enter the fruits name: ")

if user_input in Fruits:
  fruit_price = Fruits[user_input]
  print("The price for the fruit",user_input,"is" ,fruit_price)
else:
  print("The fruit is not available",User_input)

#5

sentence = input("Enter a sentence: ")
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word frequencies:")
for word, freq in word_freq.items():
    print(word, ":", freq)

#6
students = {
  'Sameer':[70,80,90,100,50],
  'Himansu':[40,50,60,70,80],
  'Sankalp':[30,40,50,60,70],
  'Srushti': [100,80,90,70,30],
  'Nilanjan':[60,70,80,90,50]
}

for student_name , marks in students.items():
  total_marks = sum(marks)
  avg = total_marks/len(marks)
  print( "got a total of", total_marks, "marks and an average of", avg, "marks.")


