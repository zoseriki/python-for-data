#Instructions: The NumPy library has been imported using the conventional alias,
# and a one-dimensional NumPy array has been created containing the
# following values in order:4, 5, 7, 10
# 1. Create a two-dimensional array using two lists - one with the values 4 and 5, and the other - with 7 and 10.
# For simplicity, call this array array_2.
# 2. Print the contents of array_2.
# 3. Compute and display the mean of array_1 and the overall mean of array_2.
# 4. Compute and display the row-wise mean of array_2.
# 5. Compute and display the column-wise mean of array_2.

import numpy as np
#creating array 1
array_1 = np.array([4,5,7,10])
#creating array 2
array_2 = np.array([[4,5], [7,10]])
#displaying array 2
print(array_2)
#calculatin the overall mean of array 1 and displaying it
print(np.mean(array_1))
#callculating the overall mean of array 2 and displaying it
print(np.mean(array_2))
#calculating and displaying the column wise mean
print(np.mean(array_2, axis = 0))
##calculating and displaying the row wise mean
print(np.mean(array_2, axis = 1))
#casting the mean result as an integer
print(np.mean(array_2, axis = 0, dtype = int))