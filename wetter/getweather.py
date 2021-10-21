import os
from bs4 import BeautifulSoup
from getrawdata import GetRawData
from getwebdata import GetWebData

def main():
    URL = "https://www.bgc-jena.mpg.de/wetter/weather_data.html"
    '''
    # URL = "http://localhost/wetter/weather_data.html"
    '''
    rdata = GetRawData()
    rawdata = rdata.list_rawdata_files()
    wdata = GetWebData(URL)
    wdata.webdata_from_table(1,1,0)
    wdata.download_zip_files(rawdata)
    print("Done")

if __name__ == "__main__":
    main()

