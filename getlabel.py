file = open("usecode.txt","r")

data = file.read()


labels = ""
count = 0
flag = 0
l = len(data)
i = 0
flag2 = 0
while(i<=l-4):

    if data[i] == "l" and data[i+1] == "a" and data[i+2] == "b"  and data[i+3] == "e"  and data[i+4] == "l":
        i = i + 7
        flag = 1

    if data[i] == "\"" and flag == 1:
        labels += "\n"
        flag = 0

    if flag == 1:
        print(data[i])
        labels += data[i]

    i = i +1



print(labels)

filewrite = open("assignweight.txt","w")

filewrite.write(labels)
