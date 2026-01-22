# Sort Array: Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending
import numpy as np 

# *Sorting 1-D array (ascending) -> np.sort()
var = np.array([3,2,2,4,3,7,6,4,5]) # 1-D
# index   ->    0 1 2 3 4 5 6 7 8
sort_arr = np.sort(var) # will sort the array ascending to descending
print(sort_arr) # [2 2 3 3 4 4 5 6 7]

# *Sorting 1-D array (alphabetical) -> np.sort()
var1 = np.array(['w','a','m','c','y','t'])
sort_arr1 = np.sort(var1) # will sort the array alphabetically
print(sort_arr1) # ['a' 'c' 'm' 't' 'w' 'y']

# *Sorting 2-D array (ascending) -> np.sort()
var22 = np.array([[2,1,4],[8,4,3],[7,6,2]]) # 2-D
sort_arr22 = np.sort(var22)
print(sort_arr22)
'''
[[1 2 4]
 [3 4 8]
 [2 6 7]]
'''

# Filter Array: Getting some elements out of an existing array and creating a new array out of them

arr = np.array([1,2,3,4]) # 1-D
filter_arr = [True,False,False,True]
new_arr = arr[filter_arr] # compare the corresponding indexes of both arrays and will filter only the 'True' values
print(new_arr) # [1 4]
print(type(new_arr)) # <class 'numpy.ndarray'>

'''
Arithmetic Functions:
-Shuffle
-Unique
-Resize
-Flatten
-Ravel
'''
# *Shuffle array -> np.random.shuffle()
var = np.array([1,3,2,4,7])
np.random.shuffle(var)
print(var) # [2 3 4 1 7] -> will vary

# *Unique array -> np.unique()
var1 = np.array([1,2,3,3,2,5])
x = np.unique(var1) # there will be no repeated element
print(x) # [1 2 3 5]

# will also show the index value 
y = np.unique(var1,return_index=True)
print(y) # (array([1, 2, 3, 5]), array([0, 1, 2, 5], dtype=int64))

# will also count the number of elements
z = np.unique(var1,return_index=True,return_counts=True)
print(z) # (array([1, 2, 3, 5]), array([0, 1, 2, 5], dtype=int64), array([1, 2, 2, 1], dtype=int64))

# * Resize array -> np.resize()
var3 = np.array([1,2,3,4,5,6])
r = np.resize(var3,(2,3)) # two rows & three columns
print(r)
'''
[[1 2 3]
 [4 5 6]]
'''
r1 = np.resize(var3,(3,2)) # three rows & two columns
print(r1)
'''
[[1 2]
 [3 4]
 [5 6]]
'''

# *Flatten array
var7 = np.array([[1,2],[3,4],[5,6]])
print(var7.flatten()) # [1 2 3 4 5 6]
print(var7.flatten(order="F")) # [1 3 5 2 4 6]

# *Ravel array
print(np.ravel(var7)) # [1 2 3 4 5 6]
print(np.ravel(var7,order="K")) # [1 2 3 4 5 6]

'''
Order: {'C', 'F', 'A', 'K'}, Optional
*'C' means to flatten in row-major (C-style) order.
*'F' means to flatten in column-major (Fortran-style) order.
*'A' means to flatten in column-major order if `a` is Fortran *contiguous* in memory, row-major order otherwise.
*'K' means to flatten `a` in the order the elements occur in memory
The default is 'C'.
'''
