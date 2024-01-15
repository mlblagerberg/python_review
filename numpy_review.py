"""
General NumPy Review
January 14th, 2024
Madeleine Lagerberg
"""

### Description: NumPy is a multidimensional array library. Primary objects are matrices and arrays
# Arrays are faster than lists. This is because Numpy uses Fixed Types, whereas lists use int types 
# which store a lot more information. Numpy uses contiguous memory, which is a consolidated form of
# memory. This consolidated approach allows for faster compute and lookup. (SIMD Vector Processing,
# and Effective Cache Utilization). Similar to lists, NumPy arrays support insertion, deletion, 
# appending, concatenation, etc. NumPy arrays are more flexible and support more operations.

### Application of NumPy:
# 1. Replacement of MATLAB (check out SciPy for more math)
# 2. Supports plotting
# 3. Backend of Pandas
# 4. Machine Learning applications

import numpy as np

### Array basics
# Initialize an array
a = np.array([1,2,3])
print(a)

# Two-dimensional array
b = np.array([[0.,2.,4.,8.,16.],[0.,1.,2.,3.,4.]])
print(b)

# Three-dimensional array
c = np.array([[[1,2,3],[2,4,6]],[[3,6,9],[1,2,3]]])
print(c)

# Get dimension of array
shapeA = a.shape
ndimA = a.ndim
print(f'Shape of array B is {shapeA} which has {ndimA} dimension(s)')

shapeB = b.shape
ndimB = b.ndim
print(f'Shape of array B is {shapeB} which has {ndimB} dimension(s)')

shapeC = c.shape
ndimC = c.ndim
print(f'Shape of array C is {shapeC} which has {ndimC} dimension(s)')

# Check what the type of array is
print(a.dtype)

# We know that there won't be any large numbers in this array so lets assign its type as int16 instead
a = np.array([1,2,3], dtype = 'int16')
print(a.dtype)

# Get Size: Check how much memory our array is taking up
print(a.itemsize)

# Check how many items are in the array
print(a.size)

# Total size is then the product of the two
print(a.itemsize * a.size)

# Simplar way to get total size
print(a.nbytes)

### Accessing/Changing specific elements, rows, columns, etc
a = np.array([[0,1,2,3,4,5,6],[7,8,9,0,1,2,3]])
print(a)
print(a.shape)





 
