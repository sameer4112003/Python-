import math


def eucliden_dist(point1,point2):
    x1 , y1 = point1
    x2 , y2 = point2
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

point1 =(5,3)
point2 = (6,8)
distance = eucliden_dist(point1,point2)
print("Euclidean distance between two points : ",distance)