import os
from bs4 import BeautifulSoup
from getrawdata import GetRawData
from getwebdata import GetWebData

def main():
    URL = "https://www.bgc-jena.mpg.de/wetter/weather_data.html"
    # URL = "http://localhost:8080/wetter/weather_data.html"

    myRawDataDir = "/Users/dennismiyoshi/github/TimeSeries/RawData"
    rdata = GetRawData(myRawDataDir)
    rawdata = rdata.list_rawdata_files()
    wdata = GetWebData(URL)
    wdata.get_hrefs(myRawDataDir, rawdata)
    print("Done")

if __name__ == "__main__":
    main()

