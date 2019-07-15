file = open("fin.txt","r")
data = file.read()


labels = ""
count = 0
flag = 0
l = len(data)
i = 0
flag2 = 0
count = 0
finindex = []
while(i<=l-4):

    if data[i] == "l" and data[i+1] == "a" and data[i+2] == "b"  and data[i+3] == "e"  and data[i+4] == "l":
        i = i + 7
        flag = 1

    if data[i] == "\"" and flag == 1:
        if data[i-2].isalpha():
            finindex.append(count)
        labels += "\n"
        flag = 0
        count = count + 1

    if flag == 1:
        labels += data[i]

    i = i +1

print(finindex)
print(len(finindex))
dataarr = data.split("\n")

finarr = []
j = 0
for i,val in enumerate(dataarr):

    if j == 95:
        break
    if i == finindex[j]:
        finarr.append(val)
        j = j +1


finstr = ""
for i in finarr:
    finstr += i +"\n"
output = open("notchildattrib.txt","w")
output.write(finstr)
