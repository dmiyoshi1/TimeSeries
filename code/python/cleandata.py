import os
import sys
import zipfile
import pandas as pd
import re

def main(): 
    myRawDataDir = "/Users/dennismiyoshi/github/TimeSeries/RawData"
    myWorkingDir = "/Users/dennismiyoshi/github/TimeSeries/Working"
    tensorDataDir = "/Users/dennismiyoshi/LabFolder/Weather"

    # Make sure our working directory exists or exit
    try:
        if not os.path.exists(myWorkingDir):
            os.makedirs(myWorkingDir)
    except:
        print("There is a problem with the working directory")
        sys.exit(1)

    # chdir to the raw data directory. if this fails then exit
    try:
        os.chdir(myRawDataDir)
    except:
        print("Could not chdir to {0}".format(myRawDataDir))
        sys.exit(1)

    # List all of the zip files in the raw data dir
    # avoid the mpi_roof.zip file because we want the static data
    dirlist = os.listdir()
    for file in dirlist:
        if '.zip' in file and file != 'mpi_roof.zip':
            zipfile.ZipFile(file, 'r').extractall(myWorkingDir)

    csvlist = []
    os.chdir(myWorkingDir)
    dirlist = os.listdir()
    for file in dirlist:
        if '.csv' in file:
            csvlist.append(file)
    csvlist.sort()

    df = pd.concat([pd.read_csv(f, encoding='iso-8859-1') for f in csvlist])
    df.to_csv(tensorDataDir + '/roof.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()