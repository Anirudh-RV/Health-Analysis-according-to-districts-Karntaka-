

file = open('meaning.txt',"r+")

F = file.readlines()

for i in F:
    j = i.split(':')
    print(j)

    break
