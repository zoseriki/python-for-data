#this is a practice on how to use pandas

import pandas as pd
employee_names = ['Amy White', 'Jack Stewart', 'Richard Lauderdale', 'Sara Johnson']
employee_names_Series = pd.Series(employee_names)
print(employee_names_Series)
print(type(employee_names_Series))