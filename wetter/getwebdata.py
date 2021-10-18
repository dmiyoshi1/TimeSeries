import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

class GetWebData:
    def __init__(self, url):
        self.url = url
        self.zip_files_dict = {}

    def list_zip_files(self, href_list):
        href_dict = {}        

        for link in href_list:
            file_name = link['href'].rsplit('/', 1)[-1]
            href_dict[file_name] = urllib.parse.urljoin(self.url, link['href'])
            # if the href begins with a '/' then it is an absolute path
            # if the href does not begin with a '/' then it is a relative path

        return href_dict

    def download_zip_files(self, rawdata_files):
        for rfile in rawdata_files:
            if rfile in self.zip_files_dict:
                self.zip_files_dict.pop(rfile)

        if len(self.zip_files_dict) == 0:
            print("Nothing new to download")
        else:
            ddir = os.getcwd() + '/RawData'
            for dfile in self.zip_files_dict:
                fname = dfile.rsplit('/', 1)[-1]
                print("Attempting to download {0}".format(fname))
                '''
                content = requests.get(self.zip_files_dict[dfile]).content
                with open(ddir + '/' + fname, 'wb') as f:
                    f.write(content)
                f.close()
                print("Successfully downloaded {0}".format(fname))
                '''
    
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
        self.zip_files_dict = self.list_zip_files(cells[cellnum].findChildren('a'))

