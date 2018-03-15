import os
import urllib.request
import sys
import zipfile
import subprocess
import window
import download

class adb_download:

    def __init__(self):
        if not os.path.exists('./adb'):
            os.makedirs('./adb')
        download.download_files()

class adb_connection:

    def device_info(self):
        #print(subprocess.call(os.getcwd()+'/adb/platform-tools/adb.exe devices', shell=True))
        path = str(os.getcwd())+ '\\adb\\platform-tools\\adb devices'
        print(path)
        p = subprocess.Popen(path, stdout=subprocess.PIPE)
        text = p.communicate()[0]
        return text.decode('utf-8')

class exit:

    def __init__(self):
        subprocess.call(os.getcwd() + '/adb/platform-tools/adb kill-server', shell=True)
        sys.exit()