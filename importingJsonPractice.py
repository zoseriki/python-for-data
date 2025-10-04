#You are provided with a dictionary named data containing product names and their respective prices.
#Additionally, you are given a list named product_IDs representing product IDs.
#Convert this data into a DataFrame named df using the pandas library, setting product_IDs as the index.
import pandas as pd

data = {'ProductName':['Product A', 'Product B', 'Product C'], 'ProductPrice':[22250, 16600, 12500]}
product_IDs = ['A', 'B', 'C']
df = pd.DataFrame(data, index = product_IDs)
print(df, '\n')

prices_per_product = '{"Product A": 22250, "Product B" : 16600, "Product C":15600}'
#parsed_string = json.loads(prices_per_product)
print(prices_per_product, '\n')

import pandas as pd
new_file = pd.read_json("Lending-company-100.json")
print(new_file)