#You are provided with a CSV file named 'Lending-company-single-column-data.csv'.
#Assume that the file may contain formatting irregularities that require more flexible parsing.
#The engine parameter of pandas’ .read_csv() method allows you to specify the parsing engine, which can help handle such cases.
#Your task is to read the file without errors by specifying the appropriate separator and using the Python engine.
#Store the resulting data in a variable named my_csv_data.
#Use the print() function to display the first 5 rows of the data for a quick overview.

import pandas as pd

filename = 'Lending-company-single-column-data.csv'
my_csv_data = pd.read_csv(filename, sep = ',', engine = 'python')

print(my_csv_data.head())

