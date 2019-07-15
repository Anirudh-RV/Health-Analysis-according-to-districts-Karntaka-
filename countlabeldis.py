import pandas as pd



df = pd.read_csv("train_d1.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')


arr = [555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584]
tt = []
for i in range(30):
    df = pd.read_csv("dist"+str((i+1))+".csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')
    t=[]
    for j in range(6):
        tf = df.groupby('Cluster').filter(lambda x: any(x['Cluster'] == j))
        t.append(tf.shape[0])
    tt.append(t)


file = open("finaldistcount.txt","a")

for i in tt:
    print(i)
    file.write(str(i))
    file.write("\n")
