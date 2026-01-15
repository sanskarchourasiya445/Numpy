import numpy as np

zero = np.zeros(5)
print(zero)
#[0. 0. 0. 0. 0.]

one = np.ones((3,4))
print(one)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

emp = np.empty(4)
print(emp)
#[0.00000000e+000 3.56035244e-307 3.22646744e-307 4.05133830e-322]

range = np.arange(4)
print(range)
#[0 1 2 3]

diag = np.eye(3)
print(diag)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

linspace = np.linspace(1,10,num =5)
print(linspace)
# [ 1.    3.25  5.5   7.75 10.  ]