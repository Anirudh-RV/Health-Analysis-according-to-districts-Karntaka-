file = open("district.txt","r")

data = file.read()

finstr = ""
for i in data:
    if i == "\n" or i=="\'":
        finstr = finstr+","
        continue
    finstr = finstr + i

arr = finstr.split(",")

finstr = "["
for i in arr:
    finstr = finstr + i + ","


print(finstr)
output = open("districtarr.txt","w")
output.write(finstr)
