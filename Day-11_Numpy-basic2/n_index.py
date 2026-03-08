"""
arrray[index] #1d array
array[row,column] #2d 
"""
import numpy as np
arr1 = np.array([10,20,30,40,50,60])
print(arr1[0])
print(arr1[2])
print(arr1[-1])
arr2 = np.array([[40,10,20,30],[60,70,10,20],[50,40,60,90]])
print(arr2[0,2])
print(arr2[1,3])
print(arr2[-1,0])