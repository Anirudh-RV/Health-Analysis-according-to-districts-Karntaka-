
# Reading Data
"""
# 23/02/19
Data from the sas7bat is being read.

TO-DO:
    1. Match the column names to the attribute values and get the records in an excel sheet.
    2. Run python to learn the data.

"""
from sas7bdat import SAS7BDAT

count = 0
with SAS7BDAT('big10.sas7bdat', skip_header=False) as reader:
    for row in reader:
        if count == 2:
            break
        else:
            print (row)
            count = count + 1
