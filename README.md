# Health-Analysis-according-to-districts-Karntaka-
A machine learning project using K-means algorithm to find metrics to rank districts according to health.

*** 1/26 CODE - 3dcol.py ***

plotfin.csv is being read.

for the first category of people,
The 3 attributes are being split into
xs1 = []
ys1 = []
zs1 = []

similarly, this has been done for all the 4 categories of people in the dataset.

ax.scatter(xs1, ys1, zs1, c='r', marker='o')
ax.scatter(xs2, ys2, zs2, c='b', marker='o')
ax.scatter(xs3, ys3, zs3, c='o', marker='o')
ax.scatter(xs4, ys4, zs4, c='g', marker='o')

is being used to make the graph.

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

is being used to set the 'X label', 'Y label' and 'Z label'

plt.show()

is being used to plot the graph.


*** 2/26 CODE - checkattrib.py ***

res = set(chk).intersection(bharr)

res = list(res)
print(len(res))
output = open("finhealth.txt","w")
output.write(str(res))

is being used to only store the values from 'chr' which intersects with 'bharr' which are the column names for health attribute.


*** 3/26 CODE - countlabeldis.py ***

Pandas program to cluster by a attribute name from the main dataset and store those in separate csv files.


*** 4/26CODE - countrow.py ***

**VERY IMPORTANT FILE : Counts the .sas7bdat file , big10.sas7bdat for the number of rows in it.


*** 5/26 CODE - csvplot.py ***

Used to plot graph for plotfin.csv


*** 6/26 CODE - dataframe.py ***

df = pd.read_csv("evalcsv.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')

Reads the evalcsv.csv files into a pandas dataframe,
weigharr= [1,1,1,1,1,1,0.1,1,0.3,0.01,1,1,1,1,1,1,1,0.01,1,1,1,0.1,0.02,0.02,0.1,0.01,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0.4,0.4,1,1,0.3,0.02,0.3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

applies the weights to the dataframe,

df.to_csv("evalcsv2.csv")

saves it as evalcsv2.csv after the transformation


*** 7/26 CODE - doelliework.py ***

reads ka_imp_1.csv' csv file, transforms it to csvfilestr.

*** 8/26 CODE - get3arr.py ***
file = open("azeroarr.txt","w")
file.write(str(zeroarr))

coverts the variabel 'a' in the program, to 4 [0,1,2,3] different .txt files

*** 9/26 CODE - get3arr2.py ***

zeroarr = [0, 1, 2, 3, 7, 13]
onearr = [5, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 21, 22, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 48, 50, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 83, 85, 94, 99, 101, 102, 115, 116, 127, 128, 129, 130, 153]
twoarr = [37, 38, 41, 42, 43, 47, 49, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 82, 84, 86, 88, 90, 91, 92, 93, 95, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 131, 132, 133, 134, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]
threearr = [4, 20, 23, 24, 25, 36, 44, 45, 46, 81, 87, 89, 96, 97, 98, 100, 103, 135, 136, 137]


here, the [0,1,2,3] were separate atributes and they are being divided.


*** 10/26 CODE - getalltog.py ***

reads district.txt, applies transformation accordingly and saves it to districtarr.txt

*** 11/26 CODE - getchild2.py ***

reads fin.txt, applies transformation accordingly and saves it to notchildattrib.txt

*** 12/26 CODE - getcolumns.py ***

reads notchildattrib.txt, applies transformation accordingly and saves it to notchildcol.txt

*** 13/26 CODE - getcsvdata.py ***

reads checkcsv.csv,
xs = []
ys = []
zs = []

separates into xs,ys,zs and saves them

*** 14/26 CODE - getlabel.py ***

reads usecode.txt, applies tranformation accordingly and saves it to assignweight.txt

*** 15/26 CODE - getleftover.py ***

reads usecode.txt, leftover.txt and tranformation is applied and saved to fin.txt

*** 16/26 CODE - getnewcol.py ***

uses arr to make difchildcol3.txt

*** 17/26 CODE - getsamecol.py ***

uses arr to make difchildcol2.txt

*** 18/26 CODE - groupbydis.py ***

uses arr to group by District attribute

*** 19/26 CODE - kmeans.py ***

uses train_v1.csv to train a K-means algorithm and cluster the algorithm

*** 20/26 CODE - partinto.py ***

uses notchildattrib.txt and BehaviouralChoices.txt(can choose anything) to make weights.txt

*** 21/26 CODE - proto3d.py ***

test code for 3dcol.py

*** 22/26 CODE - randnumbers.py ***

to create textfiles with random numbers.

*** 23/26 CODE - readdata.py ***

same as countrow.py, reads big10.sas7bdat file.

*** 24/26 CODE - test.py ***

testing for applying dataframe transformations.

*** 25/26 CODE - test2.py ***

applying transformations to dataframe.

*** 26/26 CODE - wordparse.py ***

to parse through words in a text file.
