import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as pl

df = pd.read_csv("train_v1.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')


kmeans = KMeans(n_clusters=6)
# Fitting with inputs
kmeans = kmeans.fit(df)
# Predicting the clusters
labels = kmeans.predict(df)
# Getting the cluster centers
C = kmeans.cluster_centers_
Label = kmeans.labels_


file = open("centroids.txt","w")
file.write(str(C))

"""
count =0
finstr = ""
for i in Label:
    finstr = finstr + str(i) + "\n"
print(count)

file = open("cluster4.txt","w")
file.write(finstr)
print(C)
"""
