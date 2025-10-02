#This is a practice code on how to use index in pandas series

import pandas as pd

workers_age = {'Amy White':50, 'Jack Stewart':53, 'Richard Lauderdale':35, 'Sara Johnson':43}
workers_age = pd.Series(workers_age)
print(pd.Series(workers_age).index)