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

#creating a tensor
m1 = np.array([[3, 4, 5], [6, 7, 8]])
m2 = np.array([[1, 2, 3], [4, 5, 6]])
t = np.array([m1, m2])

print(t.shape)

#adding matrices
x = m1 + m2
print(x)

#transposing a matrice
A = np.array([[5, 12, 6], [-3, 0, 14]])
print(A)
print(A.T)

B = np.array([[5, -2], [-3, 4]])
print(B)
print(B.T)

#using the dot product, Example 1
o = np.array([2, 8, -4])
p = np.array([1, -7, 3])
np.dot(o, p)
print(np.dot(o, p))

#Exaple 2
u = np.array([0, 2, 5, 8])
v = np.array([20, 3, 4, -1])
np.dot(u,v)
print(np.dot(u, v))

#multiplying a scalar times scalar
print(np.dot(8, 5))
print(np.dot(7, -10))

#multiplying scalar by a vector
print(np.dot(8, -10))

#multiplying scalar and matrix
A = np.array([[5, 12, 6], [-3, 0, 14]])
print(3 * A)

#multiplying matrix with another matrix
#condition: we can only multiply an m x n with an n x k matrix.
A = np.array([[5, 12, 6], [-3, 0, 14]])
B = np.array([[2, -1], [-8, 0], [3, 0]])
#np.dot(A, B)
print(np.dot(A, B))