import os
import zipfile
import pandas as pd
import re

dirlist = os.listdir()
ziplist = []
for file in dirlist:
    if '.zip' in file and file != 'mpi_roof.zip':
        ziplist.append(file)

# print(ziplist)
ziplist.sort()
# print(ziplist)
path_to_files = os.getcwd()
for f in ziplist:
    with zipfile.ZipFile(path_to_files + '/' + f, 'r') as zip_ref:
        zip_ref.extractall(path_to_files)

dirlist = os.listdir()
csvlist = []

for file in dirlist:
    if '.csv' in file and re.match(r'.*_2....\.zip', file):
        csvlist.append(file)
csvlist.sort()

df = pd.concat([pd.read_csv(f, encoding='iso-8859-1') for f in csvlist])
df.to_csv('roof.csv', index=False, encoding='utf-8')
