import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

class GetData:
    def __init__(self, url):
        self.url = url
        data_dir = ""
        links = []

    def get_rawdata_files(self):
        self.data_dir = os.getcwd() + '/RawData'

        # Get the list of downloaded zipped data files
        files = os.listdir(self.data_dir)
        zip_files = [file for file in files
            if file.endswith(".zip")]

        return zip_files

    def get_zip_files(self):
        ziplinks = []
        name_of_zip_files = []

        zip_files = self.get_rawdata_files()

        for link in self.links:
            file_name = link['href'].rsplit('/', 1)[-1]
            if file_name not in zip_files:
                name_of_zip_files.append(self.data_dir + '/' + file_name)
                # if the href begins with a '/' then it is an absolute path
                # if the href does not begin with a '/' then it is a relative path
                ziplinks.append(urllib.parse.urljoin(self.url, link['href']))

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
        self.links = cells[cellnum].findChildren('a')

