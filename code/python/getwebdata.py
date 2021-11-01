import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

from requests.api import get

class GetWebData:
    def __init__(self, url):
        self.url = url
        self.zip_files_dict = {}

    def get_hrefs(self, rawdatadir, rawdata):
        try:
            page = requests.get(self.url)
        except requests.ConnectionError:
            print("Cannot connect. Check the URL")
            return 0

        soup = BeautifulSoup(page.content, "html.parser")
        for t in soup.findAll(lambda tag: tag.name == 'a' and tag.get('href') and tag.text):
            fname = t['href'].rsplit('/', 1)[-1]
            if fname.startswith('mpi_roof_') and fname.endswith('.zip') and fname not in rawdata:
                uri = urllib.parse.urljoin(self.url, t['href'])
                print("Downloading {0}".format(fname))
                zippy = requests.get(uri).content
                with open(rawdatadir + '/' + fname, 'wb') as f:
                    f.write(zippy)
                f.close()

