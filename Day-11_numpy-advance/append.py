import numpy as np
arr = np.array([10,20,30])
new_arr = np.append(arr,[40,50,60,70])
print(arr)
print(new_arr)
# concate
new_arr_con=np.concatenate((arr,new_arr),axis=0)
print(new_arr_con)
# removeing the eleent from array
"""
np.delet(array,index,axis =0)
flattern array
"""
del_arr = np.array([10,20,30,40,50])
print(del_arr)
new_arr_del = np.delete(del_arr,0)
print(new_arr_del)
# For 2d array
del_arr_2d =np.array([[1,2,3],[4,5,6]])
print(del_arr_2d)
new_arr_del_2d = np.delete(del_arr_2d,0,axis=0)
print(new_arr_del_2d)