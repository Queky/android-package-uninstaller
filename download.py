import urllib.request
import zipfile
import sys

class download:

    def download_files(self):
        platform = sys.platform
        if platform == "linux" or platform == "linux2":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
        elif platform == "darwin":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-darwin.zip'
        elif platform == "win32":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'

        urllib.request.urlretrieve(link, './adb/' + platform +'.zip')
        self.file_extract()


    def file_extract(self):
        unzip = zipfile.ZipFile('./adb/' + sys.platform + '.zip', 'r')
        unzip.extractall('./adb')
        unzip.close()