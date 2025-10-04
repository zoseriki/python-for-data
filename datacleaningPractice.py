#Using the arguments of the np.genfromtxt() function, perform the following data cleaning
# steps:
#1. Set the data type to string.
#2. Skip the first row of the dataset.
#3. Skip the last 15 rows of the dataset.
#4. Load only the 2nd, 3rd, and 5th columns.

import numpy as np

lending_co_TP = np.genfromtxt("Lending-Company-Total-Price-100.csv",
                              delimiter = ',', dtype = str, skip_header = 1, skip_footer = 15, usecols = (1, 2, 4))

print(lending_co_TP)