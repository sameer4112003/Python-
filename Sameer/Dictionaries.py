#Dictionaries in Python

dict = {
  70 : "Sameer",
  71 : "Rahul",
  72 : "Athrava",
  73 : "Soham",
  74 : "Mary",
  75 : "Om",

}
print(dict[72])

info = {'Name': "Sameer",
       'Age': 19,
       'Eligible': "No"}
print(info)
print(info['Name'])
print(info.keys())
print(info.values())

for key in info.keys():
  print(f"  The values corresponding to the key {key} is {info[key]}")

#Dictionaries methods in Python

Employee1 = {101 : "Sameer", 
            102 : "Sankalp",
            103 : "Harry",
            104 : "Ranjan",
            105 : "Swapnil",
            }
Employee2 = {106 : "A", 
            107 : "B",
            108 : "C",
            109 : "D",
            110 : "E",
            }
Employee1.update(Employee2)
Employee1.pop(105)
#Employee1.clear()
Employee1.popitem()
del Employee1[106]
print(Employee1)
