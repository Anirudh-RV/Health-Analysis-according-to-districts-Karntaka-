import pandas as pd



df = pd.read_csv("train_d1.csv",  sep='\s*,\s*', header=0, encoding='ascii', engine='python')


arr = [555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584]

for i in range(30):
    tf = df.groupby('District').filter(lambda x: any(x['District'] == arr[i]))
    tf.to_csv("dist"+str((i+1))+".csv")
