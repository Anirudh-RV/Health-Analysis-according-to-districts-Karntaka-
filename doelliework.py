import csv

csvfilestr = ""
count = 0
with open('ka_imp_1.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in row:
                if i == 'None':
                    print("--w--")
                    i = " "
                    break
                csvfilestr = csvfilestr + str(type(i)) + ","


            csvfilestr = csvfilestr + "\r\n"
            count = count + 1
            if count == 2 :
                break



print(csvfilestr)
