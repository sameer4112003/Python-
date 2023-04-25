#Sets in Python

#s = {1,2,3,4}
#print(s)

#Ariana = {"Thank you,next" , 28 , 6.5 , False}
#print(Ariana)

#Sameer = set()
#print(type(Sameer))

#for value in Ariana:
 # print(value)

#Names1= {"Sameer", "Aryan", "john", "Kevin"}
#Names2= {"Sameer", "BOB", "Happy","Kevin"}
#print(Names1,Names2)

#print(Names1.union(Names2))
#print(Names1.intersection(Names2))
#Names1.intersection_update(Names2)

Names1= {"Sameer", "Aryan", "john", "Kevin"}
Names2= {"Sameer", "BOB", "Happy","Kevin"}
Names4={"Sameer","Aryan","john"}
Names3= Names1.symmetric_difference(Names2)
print(Names3)
print(Names1.isdisjoint(Names2))
print(Names1.issuperset(Names4))

Names1.remove("Sameer")
print(Names1)

info = Names2.pop()
print(Names2)
print(info)