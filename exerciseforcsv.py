#You are provided with a CSV file named 'Lending-company-single-column-data.csv'.
# The data it contains is nearly identical to what you used in the previous coding exercises; however, this time,
# it has been stored in a single column.
#Your task is to extract only the columns StringID, Location, and Region, and set StringID as the index of the resulting DataFrame.
#Store this filtered data in a variable named location_data.
#Finally, use the print() function to display the first 5 rows of location_data for a quick overview.

import pandas as pd

location_data = pd.read_csv("Lending-company-single-column-data.csv", usecols = ["StringID", "Location",                            "Region"], index_col = "StringID")
print(location_data.head())

