import pandas as pd

work_experience_years = pd.Series([5,8,3,10])

#converting  the work_experience_years object from a Pandas Series into a NumPy array.
#Accomplish this task without overwriting the contents of work_experience_years.
print(work_experience_years.to_numpy())
