#This code is a practice on how to create a pandas DataFrames from scratch. There are 4 ways
# 1. Constructing a DataFrame from a dictionary of lists.

import pandas as pd
data = {'ProductName':['Product A', 'Product B', 'Product C'],'ProductPrice': [22250, 16600, 12500]}
df = pd.DataFrame(data)
print(df)