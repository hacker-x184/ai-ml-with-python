import numpy as np

arr = np.array([10,20,30,40,50,60])

print(arr[[0,2,4]])
# Bollen masking
print(arr[arr >20])
# for reshaping the arrow

# reshape(row,colums) specify new shape
'''They doesn't copy the data it is just for the view'''
reshaped_arr = arr.reshape(2,3)
print(reshaped_arr)
'''
.ravel() -> view
.flatten -> copy

'''
arr_2d = np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel)
print(arr_2d.flatten())
