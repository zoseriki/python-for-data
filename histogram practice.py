import numpy as np
import matplotlib.pyplot as plt

matrix_A = np.array([[1,0,0,3,1], [3,6,6,2,9], [4,5,3,8,0]])
np.sort(matrix_A, axis = None)

plt.hist(matrix_A.flat, bins=np.histogram(matrix_A)[1])
plt.show()

#matrix_A = np.array([[1,0,0,3,1], [3,6,6,2,9], [4,5,3,8,6]])
#np.sort(matrix_A, axis = None)

np.histogram(matrix_A)
