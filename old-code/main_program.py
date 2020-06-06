import os
import sys
import subprocess

operative_system = ""


class adb_connection:

    def device_show_info(self):
        path = str(os.getcwd()) + '\\adb\\platform-tools\\adb devices'
        p = subprocess.Popen(path, stdout=subprocess.PIPE)
        text = p.communicate()[0]
        return text.decode('utf-8')


class platform_info:

    def set_platform(self, platform):
        operative_system = platform


class exit:

    def __init__(self):
        subprocess.call(os.getcwd() + '/adb/platform-tools/adb kill-server', shell=True)
        sys.exit()
