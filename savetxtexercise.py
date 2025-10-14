#Store the data from lending_co_saving as a *.csv file named "Saving-Exercise-4".
#Then print the new file saved.


import numpy as np
np.set_printoptions(suppress = True, linewidth = 150)

lending_co_saving = np.genfromtxt("Lending-Company-Saving-100.csv",
                                    delimiter = ',',
                                    dtype = str)

np.savetxt("Saving-Exercise-4.csv", lending_co_saving, fmt = "%s", delimiter = ',')

saving_exercisetxt = np.genfromtxt("Saving-Exercise-4.csv", delimiter = ',', dtype = str)
print(saving_exercisetxt)
print(saving_exercisetxt.shape, "\n")
print("First 10 Rows:\n", saving_exercisetxt[:10], "\n")
print("Last 10 Rows:\n", saving_exercisetxt[-10:])
