"""
np.insert(array , index,  valuse, asix=none)
array - original array
index - 
value - 
axis - 
axis = 0,row-wise
"""
import numpy as np
arr  = np.array([10,20,30,40,50,60,70])
new_arr = np.insert(arr,2,300)
print(arr)
print(new_arr)
# for 2d array
arr_2d = np.array([[10,20,30],[40,50,60]])
# insert a new row at index 1 
new_arr_2d = np.insert(arr_2d,1,[5,6,7],axis=0)
print(arr_2d)
print(new_arr_2d)

