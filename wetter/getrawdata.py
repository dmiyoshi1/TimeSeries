import os
import requests
from bs4 import BeautifulSoup
import urllib.parse

class GetRawData:
    def __init__(self):
        self.rawdata_dir = self.set_rawdata_dir()
        self.zipfiles = []

    def set_rawdata_dir(self):
        self.rawdata_dir = os.getcwd() + '/RawData'
        if not os.path.exists(self.rawdata_dir):
            os.makedirs(self.rawdata_dir)

    def list_rawdata_files(self):
        # Get the list of downloaded zipped data files
        files = os.listdir(self.rawdata_dir)
        self.zipfiles = [file for file in files
            if file.endswith(".zip")]

    def return_zipfiles(self):
        return self.zipfiles

