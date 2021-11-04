import os
import sys
import zipfile
import pandas as pd
import re

def main(): 
    myRawDataDir = "/Users/dennismiyoshi/github/TimeSeries/RawData"
    myWorkingDir = "/Users/dennismiyoshi/github/TimeSeries/Working"
    tensorDataDir = "/Users/dennismiyoshi/github/TimeSeries/wetter"

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
            my_filtered_csv = pd.read_csv(file, encoding="iso-8859-1", usecols=["Date Time","p (mbar)","T (degC)","Tpot (K)","Tdew (degC)","rh (%)","VPmax (mbar)","VPact (mbar)","VPdef (mbar)","sh (g/kg)","H2OC (mmol/mol)","rho (g/m**3)","wv (m/s)","max. wv (m/s)","wd (deg)"])
            os.unlink(file)
            my_filtered_csv.replace(to_replace=-9999.99, value=0, inplace=True)
            my_filtered_csv.replace(to_replace=-9999.0, value=0, inplace=True)
            my_filtered_csv.to_csv(file, index=False, encoding="utf-8")
    
    csvlist.sort()
    
    '''
    # This is the pandas concat method. However this is slower than the direct
    # Python method of concatenating a list of files.
    df = pd.concat([pd.read_csv(f, encoding='iso-8859-1') for f in csvlist])
    df.to_csv(tensorDataDir + '/roof.csv', index=False, encoding='utf-8')
    '''

    count = 0
    with open(tensorDataDir + "/roof.csv","w") as fout:
        for file in csvlist:
            if count == 0:
                count = 1
                with open(file, "r") as f:
                    fout.write(f.read())
            else:
                # now the rest:    
                with open(file, "r") as f:
                    next(f) # skip the header
                    fout.write(f.read())

if __name__ == "__main__":
    main()