file = open("notchildattrib.txt","r")

data = file.read()

labels = ""
count = 0
flag = 0
l = len(data)
i = 0
flag2 = 0

labels += "["
while(i<=l-4):

    if data[i] == "[":
        i = i +1
        flag = 1
        labels +="' "

    if data[i] == "," and flag == 1:
        labels += "',"
        flag = 0

    if flag == 1:
        labels += data[i]

    i = i +1



labels += "]"
filewrite = open("notchildcol.txt","w")
filewrite.write(labels)
