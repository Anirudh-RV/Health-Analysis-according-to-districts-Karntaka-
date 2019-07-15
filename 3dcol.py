from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# graph : 1
csvfilestr = ""
csvlist = []
with open('plotfin.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                csvfilestr = csvfilestr + i + ","
                csvlist.append(i)

            csvfilestr = csvfilestr + "\r\n"

xs1 = []
ys1 = []
zs1 = []

count =0
for i,val in enumerate(csvlist):
    if i%3 == 0:
        xs1.append(float(val))
    elif i%3 == 1:
        ys1.append(float(val))
    elif i%3 == 2:
        zs1.append(float(val))


# end : 1

# graph : 2
csvfilestr = ""
csvlist = []
with open('plotfin.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                csvfilestr = csvfilestr + i + ","
                csvlist.append(i)

            csvfilestr = csvfilestr + "\r\n"

xs2 = []
ys2 = []
zs2 = []

count =0
for i,val in enumerate(csvlist):
    if i%3 == 0:
        xs2.append(float(val))
    elif i%3 == 1:
        ys2.append(float(val))
    elif i%3 == 2:
        zs2.append(float(val))


# end : 2


# graph : 3
csvfilestr = ""
csvlist = []
with open('plotfin.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                csvfilestr = csvfilestr + i + ","
                csvlist.append(i)

            csvfilestr = csvfilestr + "\r\n"

xs3 = []
ys3 = []
zs3 = []

count =0
for i,val in enumerate(csvlist):
    if i%3 == 0:
        xs3.append(float(val))
    elif i%3 == 1:
        ys3.append(float(val))
    elif i%3 == 2:
        zs3.append(float(val))


# end : 3



# graph : 4
csvfilestr = ""
csvlist = []
with open('plotfin.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                csvfilestr = csvfilestr + i + ","
                csvlist.append(i)

            csvfilestr = csvfilestr + "\r\n"

xs4 = []
ys4 = []
zs4 = []

count =0
for i,val in enumerate(csvlist):
    if i%3 == 0:
        xs4.append(float(val))
    elif i%3 == 1:
        ys4.append(float(val))
    elif i%3 == 2:
        zs4.append(float(val))


# end : 4




ax.scatter(xs1, ys1, zs1, c='r', marker='o')
ax.scatter(xs2, ys2, zs2, c='b', marker='o')
ax.scatter(xs3, ys3, zs3, c='o', marker='o')
ax.scatter(xs4, ys4, zs4, c='g', marker='o')



ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
