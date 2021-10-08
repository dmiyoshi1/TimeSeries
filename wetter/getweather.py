import os
from bs4 import BeautifulSoup
from getdata import GetData

def main():
    # URL = "https://www.bgc-jena.mpg.de/wetter/weather_data.html"
    URL = "http://localhost/wetter/weather_data.html"
    getdata = GetData(URL)
    if getdata.webdata_from_table(1, 1, 0) != 0:
        getdata.get_zip_files()

if __name__ == "__main__":
    main()

