file = open("usecode.txt","r")
secondfile = open("leftover.txt","r")

data = file.read()
secondata = secondfile.read()

secondata = secondata.split("\n")

labels = ""
count = 0
flag = 0
l = len(data)
i = 0
flag2 = 0
count = 0
j = 0
newlabel = ""
newlabelarr = []
while(i<=l-4):

    if data[i] == "[":
        i = i +1
        flag = 1

    if data[i] == "," and flag == 1:
        labels += "\n"
        flag = 0
        count = count + 1

    if flag == 1:
        labels += data[i]


    i = i +1

labels = labels.split("\n")

j =0
count = 0
neededindex = []
for i,val in enumerate(labels):
    if val == secondata[j]:
        neededindex.append(i)
        j = j +1

j = 0
dataarr = data.split("\n")

finarr = []
for i,val in enumerate(dataarr):

    if i == neededindex[j]:
        finarr.append(val)
        j = j +1


print(len(finarr))
finstr= ""
for i in finarr:
    finstr += i +"\n"

print(finstr)

output = open("fin.txt","w")

output.write(finstr)
