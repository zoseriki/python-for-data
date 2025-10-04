#This code is a practice on how to create a pandas DataFrames from scratch. There are 4 ways
# 1. Constructing a DataFrame from a dictionary of lists.

import pandas as pd
data = {'ProductName':['Product A', 'Product B', 'Product C'],'ProductPrice': [22250, 16600, 12500]}
df = pd.DataFrame(data)
print(df, "\n")

#2. Constructing a DataFrame from a dictionary of lists and  specifying  an index
data = {'ProductName': ['Product A', 'Product B', 'Product C'], 'ProductPrice': [22250, 16600, 12500]}
df = pd.DataFrame(data, index = ['A', 'B', 'C'])
print(df, "\n")
#or we can also do it this way by passing a variable name to the index
data = {'ProductName': ['Product A', 'Product B', 'Product C'], 'ProductPrice': [22250, 16600, 12500]}
product_IDs = ['A', 'B', 'C']
df = pd.DataFrame(data, index = product_IDs)
print(df, "\n")
#3. Constructing a DataFrame from a list of dictionaries
data = [{'ProductName': 'Product A', 'ProductPrice': 22250},
        {'ProductName': 'Product B', 'ProductPrice': 16600},
        {'ProductName':'Product C', 'ProductPrice': 12500}]
df = pd.DataFrame(data)
print(df, "\n")