# First way
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)
# With default values
# np.zeroes(shape) (3) fir 1d,(3,3) 2d
zeroes_array = np.zeros(3)
print(zeroes_array)
# Ones (shape
ones_array = np.ones((2,3))
print(ones_array)
# full function(value)
filled_array = np.full((2,2),7)
print(filled_array)
# Creatg the sequences of number in numpy
arange_arr = np.arange(1,10,2)
print(arange_arr)
# for creating the identity matrix 
Identity = np.eye(3)
print(Identity)