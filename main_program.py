import os
import urllib.request
import sys
import zipfile
import subprocess

class adb_download:

    def __init__(self):
        if not os.path.exists('./adb'):
            os.makedirs('./adb')
        self.download_files()

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

class adb_connection:

    def __init__(self):
        print(subprocess.call(os.getcwd()+'/adb/platform-tools/adb.exe devices', shell=True))

class exit:

    def __init__(self):
        subprocess.call(os.getcwd() + '/adb/platform-tools/adb.exe kill-server', shell=True)
        sys.exit()