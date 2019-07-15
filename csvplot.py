import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


csvfilestr = ""
csvlist = []
with open('plotfin.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                csvfilestr = csvfilestr + i + ","
                csvlist.append(i)

            csvfilestr = csvfilestr + "\r\n"

xs = []
ys = []
zs = []

count =0
for i,val in enumerate(csvlist):
    if i%3 == 0:
        xs.append(float(val))
    elif i%3 == 1:
        ys.append(float(val))
    elif i%3 == 2:
        zs.append(float(val))

ax.scatter(xs, ys, zs, zdir='z', s=20, c=None, depthshade=True)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
