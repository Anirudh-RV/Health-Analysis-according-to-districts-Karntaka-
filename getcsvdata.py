import csv


csvfilestr = ""
csvlist = []

with open('checkcsv.csv') as csvfile:
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
        xs.append(val)
    elif i%3 == 1:
        ys.append(val)
    elif i%3 == 2:
        zs.append(val)
