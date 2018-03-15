import requests
import zipfile
import sys
import os

class download_functions:

    def download_files(self):
        print('crea carpeta')
        os.makedirs('./adb')
        print('carpeta creada')
        platform = sys.platform
        if platform == "linux" or platform == "linux2":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
        elif platform == "darwin":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-darwin.zip'
        elif platform == "win32":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'

        r = requests.get(link)
        with open('./adb/' + platform +'.zip', 'wb') as f:
            f.write(r.content)
        self.file_extract()


    def file_extract(self):
        unzip = zipfile.ZipFile('./adb/' + sys.platform + '.zip', 'r')
        unzip.extractall('./adb')
        unzip.close()