import pandas as pd
import numpy
#from RetrieveAff import Author_ID
df = pd.read_csv('Data/Scopus-Author.csv', names=['Author Name', 'Auth-ID', 'Number of Documents', 'Subject Area', 'Orc_ID'], encoding='cp1252')
#print(df['Auth-ID'])
arr = df["Auth-ID"].to_numpy()
#print(arr[1])
sizearr = arr.size
#print(sizearr)
for i in range(1, sizearr):
    defi = "ID="+str(arr[i])
    file_object = open('strt.txt', 'a')
    file_object.write(defi)
    file_object.write('\n')
    file_object.close()
    #print(defi)