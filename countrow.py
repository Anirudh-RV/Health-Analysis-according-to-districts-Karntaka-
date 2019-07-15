# Reading Data
"""
# 23/02/19
Data from the sas7bat is being read.

DONE :
    1. Match the column names to the attribute values and get the records in an excel sheet.
    2. Read the values and made sense of data


TO-DO:
    1. Run python to learn the data.

"""
from sas7bdat import SAS7BDAT

count = 0
print("Count : "+str(count))

with SAS7BDAT('big10.sas7bdat', skip_header=False) as reader:
    for row in reader:
            count = count + 1
            if count%10000 == 0:
                print("count : "+str(count))



print("Count : "+str(count))
