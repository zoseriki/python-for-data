#This is a practice code on how to use the .head() and the .tail() method in pandas.

import pandas as pd

employees_work_exp = pd.Series({
'Amy White'   : 3,
'Jack Stewart'   : 5,
'Richard Lauderdale'  : 4.5,
'Sara Johnson'  : 22,
'Patrick Adams' : 28,
'Jessica Baker'  : 14,
'Peter Hunt'   : 4,
'Daniel Lloyd'  : 6,
'John Owen'   : 1.5,
'Jennifer Phillips'  : 10,
'Courtney Rogers'   : 4.5,
'Anne Robinson'  : 2,
})


print(employees_work_exp.head(), "\n")

print(employees_work_exp.tail())
