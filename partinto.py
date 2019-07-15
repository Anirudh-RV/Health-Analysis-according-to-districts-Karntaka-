file = open("BehaviouralChoices.txt","r")
data = file.read()

seconddata = open("notchildattrib.txt","r")
seconddata = seconddata.read()
seconddata = seconddata.split("\n")


print(data)
labels = ""
count = 0
flag = 0
l = len(data)
i = 0
flag2 = 0
count = 0
finarr = []
while(i<=l-4):

    if data[i] == "[":
        flag = 1

    if data[i] == "]" and flag == 1:
        labels +="]"
        finarr.append(labels)
        labels = ""
        flag = 0
        count = count + 1

    if flag == 1:
        labels += data[i]

    i = i +1

finstr = ""
for i in finarr:
    if i in seconddata:
        finstr += i + " B"+"\n"


print(finstr)
output = open("weights.txt","w")
output.write(finstr)
