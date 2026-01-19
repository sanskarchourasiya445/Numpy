import numpy as np
# A NumPy array is a fast, efficient data structure
# used for numerical and scientific computing.
x = np.array([1,2,3,4,5])
print(x)
print(type(x))
print(x.ndim)

arr = []
for i in range(1,6):
    arr.append(int(input("Enter a number :")))
print(np.array(arr))    


arr2 = np.array([['A','B','C'],['D','E','F'],['G','H','I']])
print(arr2)
print(arr2.ndim)

ar3 = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(arr3)
print(arr3.ndim)

arrN = np.array([1,2,3,4], ndimn = 10)
print(arrN)
print(arrN.ndim)

