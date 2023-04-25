
#NUMPY
#1
import numpy as np
a= np.array([1,2,3])
b= np.array([4,5,6])
c=b+a
d=a-b
e=a*b
print(c)
print(d)
print(e)

#2
import numpy as np
arr = np.eye(3)
print(arr)

#3
import numpy as no

matrix1 = no.array([[12,13] , [15,16]])
matrix2 = no.array([[24,25] , [26,27]])

result = no.dot(matrix1 , matrix2)
print(result)

#4
import numpy as np
arr =np.arange(10)
print(arr)

#5
import numpy as np
arr =np.arange(10,20)
print(arr)

#6
import numpy as np
arr =np.random.rand(5,5)
print(arr)
print("Mininmum value :", arr.min())
print("Maximum value :", arr.max())

#7
import numpy as np
arr =np.random.rand(5,5)
print("Before normalization :")
print(arr)
arr = (arr - np.min(arr))/ (np.max(arr) - np.min(arr))
print("After normalization :")
print(arr)

#8
import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,2])
print(arr[1,1:4])
print(arr[0:3,2])
print(arr[::2,1::2])

#9
import numpy
arr = numpy.array([[3,6,9,12],[15,18,21,24],[27,30,33,36],[39,42,45,48],[51,54,57,60]])
print("printing input array")
print(arr)
print("\n Printing array of odd rows and even columns") 
newArray = arr[::2, 1::2]
print(newArray)

#10
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)

#11
import numpy as np
arr = np.array([1,2,3,4,5],dtype='S')
print(arr)
print(arr.dtype)

#12
import numpy as np
arr = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#13
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
newArray = arr[2:8]
print(newArray)

#14
import numpy as np
arr = np.arange(1, 16)
new_arr = arr[arr % 3 == 0]
print(new_arr)

# create a dictionary with student names and their marks in 5 subjects
student_marks = {"Alice": [80, 85, 90, 75, 70], 
                 "Bob": [90, 75, 80, 85, 90], 
                 "Charlie": [70, 80, 75, 90, 85]}

# iterate over each student and calculate their total and average marks
for student, marks in student_marks.items():
    total_marks = sum(marks)
    avg_marks = total_marks / len(marks)
    print(student, "got a total of", total_marks, "marks and an average of", avg_marks, "marks.")

