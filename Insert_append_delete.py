# *Inserting in array using np.insert()

import numpy as np

# Insertion in 1-D array
var = np.array([1,2,3,4,5,6,8,9,10]) # 1-D
insert_var = np.insert(var,6,7) # np.insert(array,position,value)
print(insert_var) # [ 1  2  3  4  5  6  7  8  9 10]

var1 = np.array([10,20,30,40,50])
v1 = np.insert(var1,(1,3,5),90) # inserting multiple 90 -> in 1st 3rd and 5th position
print(v1) # [10 90 20 30 90 40 50 90]

var2 = np.array([1,3,5,7,9,11,13])
v2 = np.insert(var2,(1,3,5),(2,4,6)) # # inserting multiple values 2 4 6 -> in 1st 3rd and 5th position
print(v2) # [ 1  2  3  5  4  7  9  6 11 13]
print(type(v2)) # <class 'numpy.ndarray'>

# Insertion in 2-D array
var33 = np.array([[1,2,3],[4,5,6]]) # 2-D
v33 = np.insert(var33,1,[7,8,9],axis=0) # np.insert(array,position,value,axis)
print(v33)
'''
axis = 0 -> row wise
[[1 2 3]
 [7 8 9] -> 1st position
 [4 5 6]]
 '''

var44 = np.array([[2,4,6],[8,10,12]]) # 2-D
v44 = np.insert(var44,1,[14,16],axis=1) # axis = 1 -> column wise
print(v44)
'''
[[ 2 14  4  6]
 [ 8 16 10 12]]
 '''

# *Appending array using np.append()

# Appending in 1-D array

var3 = np.array([2,4,6,8,10,12,14,16])
v3 = np.append(var3,18) # will append 8 at the end of the array
print(v3) # [ 2  4  6  8 10 12 14 16 18]

var4 = np.array([1,2,3,4])
v4 = np.append(var4,[5,6,7,8]) # will append all the values at the end of the array
print(v4) # [1 2 3 4 5 6 7 8]

# Appending in 2-D array
var77 = np.array([[1,2,3],[4,5,6]]) # 2-D
v7 = np.append(var77,[[7,8,9]],axis=0) # row wise
print(v7)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

var88 = np.array([[2,4,6],[1,3,5]]) # 2-D
v8 = np.append(var88,[[8,10],[7,9]],axis=1) # column wise
print(v8)
'''
[[ 2  4  6  8 10]
 [ 1  3  5  7  9]]
'''

v99 = np.array([[2,3],[4,5]])
v9 = np.append(v99,[[6,7]]) # didn't specify the axis parameter
# the output is flattened into a 1D array
print(v9) # [2 3 4 5 6 7]

# *Deleting array using np.delete()

# Deletion in 1-D array 
var = np.array([1,2,3,4,5,6])
# index  ->     0 1 2 3 4 5
del_v = np.delete(var,3) # will delete 3rd index's value 4
print(del_v) # [1 2 3 5 6]

# np.delete(array,position_to_delete)

var1 = np.array([2,3,4,5,7])
x1 = np.delete(var1,[1,3]) # passing a list of indices
# will delete 1st and 3rd index's value 2 and 5 respectively
print(x1) # [2 4 7]

var2 = np.array([2,3,4,5,7])
x2 = np.delete(var1,(1,3)) # passing a tuple of indices
# will delete 1st and 3rd index's value 2 and 5 respectively
print(x2) # [2 4 7]

# Deletion in 2-D array
var98 = np.array([[1,3,5],[7,8,9]])
v98 = np.delete(var98,(0,1)) # will delete the 0th and 1st index's value
# didn't specify the axis parameter
# the output is flattened into a 1D array
print(v98) # [5 7 8 9]

var55 = np.array([[1,2,3],[4,5,6],[7,8,9]])
v55 = np.delete(var55,0,axis=0) # will delete the 0th index -> 1st column -> row wise
print(v55)
'''
[[4 5 6]
 [7 8 9]]
'''

var67 = np.array([[10,20,30],[40,50,60]])
v67 = np.delete(var67,2,axis=1) # will delete the 2nd index -> means the 3rd column -> column wise
print(v67)
'''
[[10 20]
 [40 50]]
'''
