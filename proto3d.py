# plot different colors :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xs1 = []
ys1 = []
zs1 = []

xs2 = []
ys2 = []
zs2 = []

xs3 = []
ys3 = []
zs3 = []

xs4 = []
ys4 = []
zs4 = []

xs5 = []
ys5 = []
zs5 = []

xs6 = []
ys6 = []
zs6 = []



df = pd.read_csv("train_c6.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')

n = df.shape[0]

for i in range(n):
    if df['Cluster'][i] == 0:
        # put it in xs1,ys1,zs1
        xs1.append(df['BC'][i])
        ys1.append(df['HC'][i])
        zs1.append(df['GE'][i])

    elif df['Cluster'][i] == 1:
        # put it in xs1,ys1,zs1
        xs2.append(df['BC'][i])
        ys2.append(df['HC'][i])
        zs2.append(df['GE'][i])

    elif df['Cluster'][i] == 2:
        # put it in xs1,ys1,zs1
        xs3.append(df['BC'][i])
        ys3.append(df['HC'][i])
        zs3.append(df['GE'][i])

    elif df['Cluster'][i] == 3:
        # put it in xs1,ys1,zs1
        xs4.append(df['BC'][i])
        ys4.append(df['HC'][i])
        zs4.append(df['GE'][i])

    elif df['Cluster'][i] == 4:
        # put it in xs1,ys1,zs1
        xs5.append(df['BC'][i])
        ys5.append(df['HC'][i])
        zs5.append(df['GE'][i])

    elif df['Cluster'][i] == 5:
        # put it in xs1,ys1,zs1
        xs6.append(df['BC'][i])
        ys6.append(df['HC'][i])
        zs6.append(df['GE'][i])




print(len(xs1))
print(len(xs2))
print(len(xs3))
print(len(xs4))
print(len(xs5))
print(len(xs6))

"""
cardinality :
5609
1419
1279
79
883
5519

centroids :
(0.29129069,0.05256325,0.2293614,
 (0.3220194 ,0.05160453,0.29341137,
 (0.29822095, 0.04701677, 0.4425367,
 (0.297993 ,  0.04737894 ,0.66951237,
 (0.31474281, 0.05302901 ,0.34563014,
 (0.29174218, 0.04728443, 0.25389475,
 """

#centroids :
"""
ax.scatter(0.29129069,0.05256325,0.2293614, color='blue', marker='X',s=1000)
ax.scatter(0.3220194 ,0.05160453,0.29341137,color='cyan', marker='X',s=1000)
ax.scatter(0.29822095, 0.04701677, 0.4425367,color='orange', marker='X',s=1000)
ax.scatter(0.297993 ,  0.04737894 ,0.66951237,color='green', marker='X',s=1000)
ax.scatter(0.31474281, 0.05302901 ,0.34563014,color='yellow', marker='X',s=1000)
ax.scatter(0.29174218, 0.04728443, 0.25389475,color='magenta', marker='X',s=1000)
"""
# values:

#ax.scatter(xs1, ys1, zs1, color='blue', marker='o',s=0.2)
#ax.scatter(xs2, ys2, zs2, color='cyan', marker='o')
#ax.scatter(xs3, ys3, zs3, color='orange', marker='o')
#ax.scatter(xs4, ys4, zs4, color='green', marker='o')
#ax.scatter(xs5, ys5, zs5, color='yellow', marker='o')
ax.scatter(xs6, ys6, zs6, color='magenta', marker='^',s=1)


ax.set_xlabel('Behavioral Choices')
ax.set_ylabel('Health Care')
ax.set_zlabel('Genetics')

plt.show()
