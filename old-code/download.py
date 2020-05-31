import requests
import zipfile
import sys
import os
import main_program

platform = ""


class download_functions:

    def check_internet_con(self):
        return False

    def download_files(self):
        create_directory(self)
        platform = sys.platform
        # if can_download:
        if platform == "linux" or platform == "linux2":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-linux.zip'
            main_program.platform_info.set_platform(self, "linux")
        elif platform == "darwin":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-darwin.zip'
            main_program.platform_info.set_platform(self, "darwin")
        elif platform == "win32":
            link = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
            main_program.platform_info.set_platform(self, "win32")
        else:
            pass

        r = requests.get(link)
        with open('./adb/' + platform + '.zip', 'wb') as f:
            f.write(r.content)
        self.file_extract()

    def create_directory(self):
        os.makedirs('./adb')

    def file_extract(self):
        unzip = zipfile.ZipFile('./adb/' + sys.platform + '.zip', 'r')
        unzip.extractall('./adb')
        unzip.close()
