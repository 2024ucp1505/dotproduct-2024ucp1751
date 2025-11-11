import numpy as np

n = int(input("Enter the number of elements in vec 1\n"))
m = int(input("Enter the number of elements in vec 2\n"))
list1 = []
list2 = []
print("Enter elements of vector 1 : \n")
for i in range(0,n):
	ele = int(input("Enter the element please-> "))
	list1.append(ele)
print("Enter elements of vector 2 : \n")
for i in range(0,m):
	ele = int(input("Enter the element please -> "))
	list2.append(ele)
vec1 = np.array(list1)
vec2 = np.array(list2)

vecDot = 0
for i in range (0,n):
	vecDot += (list1[i] * list2[j])
print("Dot product : ",vecDot,"\n")

########################################
#this is from lokesh's side
