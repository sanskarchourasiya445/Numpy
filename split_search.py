# Split Array - Splitting breaks one array into multiple
import numpy as np

# *Spiting in 1-D arrays
x = np.array([1,2,3,4,5,6]) # 1-D
arr = np.array_split(x,3) # will split the array into three parts
print(arr) # [array([1, 2]), array([3, 4]), array([5, 6])]
print(type(arr)) # <class 'list'>
print(arr[0]) # [1 2]

# *Spiting in 2-D arrays
y = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2-D
print(np.shape(y)) # (3,3)
arr1 = np.array_split(y,3) # will split the array into three parts
print(arr1) # [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]
print(type(arr1)) # <class 'list'>
print(arr1[0]) #  [[1 2 3]]

# *Spiting in 2-D arrays with axis wise
z = np.array([[11,22,33],[44,55,66],[77,88,99]]) # 2-D
print(np.shape(z)) # (3,3)
arr11 = np.array_split(z,3,axis=1) # will split the array into two parts -> row wise
print(arr11)
'''
[array([[11],
       [44],
       [77]]), array([[22],
       [55],
       [88]]), array([[33],
       [66],
       [99]])]
'''

# Search Array: Search an array for a certain value and return the indexes that get a match
# *Searching array -> np.where()
var = np.array([1,2,3,4,2,5,6,2,7]) # 1-D
# index   ->    0 1 2 3 4 5 6 7 8
x = np.where(var==2) # will find all the index number of '2' 
print(x) # (array([1, 4, 7], dtype=int64),)
y = np.where((var%2)==0) # will find all the index number of all elements that are divisible by '2'
print(y) # (array([1, 3, 4, 6, 7], dtype=int64),)

# *Search Sorted Array: which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order -> np.searchsorted()
var1 = np.array([1,2,3,4,6,7,8]) # Sorted array
# index   ->     0 1 2 3 4 5 6
x1 = np.searchsorted(var1,5) # will display the particular index position where to set the element in that sorted array
print(x1) # 4
x2 = np.searchsorted(var1,5,side="right") # will display the particular index position where to set the element from the 'right' side in that sorted array
print(x2) # 4
x3 = np.searchsorted(var1,[3,4,5]) # will display the array of index position where to set the element in that sorted array
print(x3) # [2 3 4]
