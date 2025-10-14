#Store the data from lending_co_saving and lending_co_total_price in separate *.npy files named
# "Saving-Exercise-1" and "Saving-Exercise-2", respectively.
import numpy as np

np.set_printoptions(suppress=True, linewidth=150)

lending_co_saving = np.genfromtxt("Lending-Company-Saving-100.csv",
                                  delimiter=',',
                                  dtype=str)

lending_co_total_price = np.genfromtxt("Lending-Company-Total-Price-100.csv",
                                       delimiter=',',
                                       dtype=str)

np.save("Saving-Exercise-1", lending_co_saving)
np.save("Saving-Exercise-2", lending_co_total_price)
print(lending_co_saving)
print(lending_co_total_price)
