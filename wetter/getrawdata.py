import os

class GetRawData:
    def __init__(self):
        self.rawdata_dir = self.set_rawdata_dir()
        self.zipfiles = []

    def set_rawdata_dir(self):
        rawdata_dir = os.getcwd() + '/RawData'
        if not os.path.exists(rawdata_dir):
            os.makedirs(rawdata_dir)
        return rawdata_dir

    def list_rawdata_files(self):
        # Get the list of downloaded zipped data files
        files = os.listdir(self.rawdata_dir)
        self.zipfiles = [file for file in files
            if file.endswith(".zip")]
        
        return self.zipfiles