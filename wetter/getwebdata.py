import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

class GetWebData:
    def __init__(self, url):
        self.url = url
        self.zip_files_list = {}

    def list_zip_files(self, href_list):
        # Move the check for already downloaded data to the main script
        # use: res = [x for x in webdata if x not in rawdata]

        for link in href_list:
            file_name = link['href'].rsplit('/', 1)[-1]
            self.zip_files_list[file_name] = urllib.parse.urljoin(self.url, link['href'])
            # if the href begins with a '/' then it is an absolute path
            # if the href does not begin with a '/' then it is a relative path

    def download_zip_files(self, rawdata_files):
        if len(name_of_zip_files) == 0:
            print("Nothing new to download")
        else:
            for place in range(len(ziplinks)):
                print("Attempting to download {0}".format(name_of_zip_files[place].rsplit('/', 1)[-1]))
                content = requests.get(ziplinks[place]).content
                with open(name_of_zip_files[place], 'wb') as f:
                    f.write(content)
                f.close()
                print("Successfully downloaded {0}".format(name_of_zip_files[place].rsplit('/', 1)[-1]))
    
    def webdata_from_table(self, tablenum, rownum, cellnum):
        try:
            page = requests.get(self.url)
        except requests.ConnectionError:
            print("Cannot connect. Check the URL")
            return 0

        soup = BeautifulSoup(page.content, "html.parser")
        tables = soup.findAll(lambda tag: tag.name=='table')

        rows = tables[tablenum].findChildren('tr')
        cells = rows[rownum].findChildren('td')
        self. list_zip_files(cells[cellnum].findChildren('a'))

