import numpy as np
arr = np.array([[-1, 2, 0, 4],[4, -0.5, 6, 0],[2.6, 0, 7, 8],[3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)
sliced_arr=arr[:2,::2]
sliced_arr1=arr[:3,1::2]
print("Array with first 2 rows and alternate columns(0 and 2):\n",sliced_arr)
print("Array with first 3 rows and alternate columns(1 and 3):\n",sliced_arr1)
Index_arr=arr[[1,1,0,3],[3,2,1,0]]
print("\nElements at indices(1,3),(1,2),(0,1),(3,0):\n",Index_arr)
