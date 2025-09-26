#This code is a practice for importing numpy and pandas and to learn how rto
#declare scalars, vectors and matrices

import numpy as np
#declaring a scalar
s = 5
print(s)

#declaring a vector. This is a 1-dimensional array.
v = np.array([5, -2, 4])
print(v)

#declaring matrices. This is a 2-dimensional array.
m = np.array([[5,12,6], [-3, 0, 14]])
print(m)

#checking the data types of the above code
print(type(s))
print(type(v))
print(type(m))

#redeclaring scalar as an array
s_array = np.array(5)
print(s_array)

#using data shapes. This helps to tell the nuber of row and columns each matrice have or vector
m.shape
print(m.shape)

#using the reshape function to change the shape of an array.
v.reshape(1,3)
print(v)
v.reshape(3,1)
print(v)