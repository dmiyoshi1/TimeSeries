import os

class GetRawData:
    def __init__(self, rawdatadir):
        self.rawdata_dir = rawdatadir
        self.zipfiles = []

    def list_rawdata_files(self):
        # Get the list of downloaded zipped data files
        files = os.listdir(self.rawdata_dir)
        self.zipfiles = [file for file in files
            if file.endswith(".zip")]
        
        return self.zipfiles