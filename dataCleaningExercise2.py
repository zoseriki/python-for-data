#Now that you understand how the np.genfromtext() function works, set its parameters with
# the following arguments in the given code (lines 4 to 15 inclusive):
#1. Use a comma as the delimiter for the dataset.
#2. Set the data type of the values to string.
#3. Skip the first row of the dataset.
#4. Skip the last fifteen rows of the dataset.
#5. Load only the second, third, and fifth columns from "Lending-Company-Total-Price-100.csv".
#6. Use # to indicate the start of a comment.
#7. Indicate that no data conversions are required (i.e., leave converters=None).
#8. Ensure that only empty fields are treated as missing data.
#9. Ensure that no field names are excluded from the retrieved dataset.
#10. Remove the following characters from field names: ()*+,-./:;<=>?@[\\]^{|}~
#11. Replace whitespaces in field names with underscores.
#12. Automatically strip leading and trailing whitespaces from field names.

import numpy as np

lending_co_TP = np.genfromtxt("Lending-Company-Total-Price-100.csv",
                              delimiter=',',
                              dtype=str,
                              skip_header=1,
                              skip_footer=15,
                              usecols=(1, 2, 4),
                              comments="#",
                              converters=None,
                              missing_values=None,
                              excludelist=None,
                              deletechars=" ()*+,-./:;<=>?@[\\]^{|}~",
                              replace_space='_',
                              autostrip=True)

print(lending_co_TP)