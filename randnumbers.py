
import random
learndata = open("lerningdataindex.txt","w")
validatedata = open("validationindex.txt","w")
testdata = open("testdataindex.txt","w")
totnum = []

learn = []
validate = []
for i in range(1,26292):
    totnum.append(i)

for i in range(1,13147):
    s = random.choice(totnum)
    totnum.remove(s)
    learn.append(s)


for i in range(1,6573):
    s = random.choice(totnum)
    totnum.remove(s)
    validate.append(s)

print(len(totnum))
print(len(learn))
print(learn==totnum)
print(totnum == validate)
print(validate == learn)


finstr = ""
for i in learn:
    finstr += str(i) +"\n"
learndata.write(finstr)



finstr = ""
for i in validate:
    finstr += str(i) +"\n"
validatedata.write(finstr)


finstr = ""
for i in totnum:
    finstr += str(i) +"\n"
testdata.write(finstr)
