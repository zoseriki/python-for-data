#Store the data from lending_co_saving and lending_co_total_price as separate  named saving and total_price,
# respectively, in a *.npz file named "Saving-Exercise-3".

import numpy as np

np.set_printoptions(suppress=True, linewidth=150)

lending_co_saving = np.genfromtxt("Lending-Company-Saving-100.csv",
                                  delimiter=',',
                                  dtype=str)

lending_co_total_price = np.genfromtxt("Lending-Company-Total-Price-100.csv",
                                       delimiter=',',
                                       dtype=str)
#np.savez("Lending-Company-Saving-100", saving=lending_co_saving)
#np.savez("Lending-Company-Total-Price-100", total_price=lending_co_total_price)

np.savez("Saving-Exercise-3",
         saving = lending_co_saving,
         total_price = lending_co_total_price)



