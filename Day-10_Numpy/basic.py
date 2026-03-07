import numpy as np
arr_2d =np.array([[1,2,3],[4,5,6],[7,8,9],[65,447,58]])
# for find the demintion of the matrix 
print(arr_2d.shape)
# for find the number of elements
print(arr_2d.size)
# to finding the number of demintion in arrary
print(arr_2d.ndim)
# to check the data type are present in the array
print(arr_2d.dtype)
# for type conversion in the arrray using the numpy function
arr2 = np.array([1.54,2.15,1.45])
int_arr = arr2.astype(int)
print(arr2.dtype)
print(arr2)
print(int_arr.dtype)
print(int_arr)
