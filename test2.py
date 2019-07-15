import pandas as pd

import numpy as np

df = pd.read_csv("evalcsv.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')

df['S251'] = df['S251'].apply(lambda VAL: (VAL+7)*0.1)



df.to_csv("evalcsv2.csv")
