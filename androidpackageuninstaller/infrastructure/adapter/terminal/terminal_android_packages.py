import subprocess
from abc import ABC
from typing import Final
from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
import os


class TerminalServiceAccess(AndroidPackages, ABC):

    # FOR LINUX
    ADB_DIRECTORY = "./adb/platform-tools/"
    LIST_ALL_PACKAGES: Final[str] = "adb shell \"pm list packages -f\""
    UNINSTALL_PACKAGE: str = "adb shell pm uninstall --user 0 com.android.chrome"

    def get_package_information(self):
        pass

    def get_package_list(self):
        print('implementation')
        ex_ = self.ADB_DIRECTORY + self.LIST_ALL_PACKAGES
        print(ex_)
        print(subprocess.check_output(ex_).decode('utf-8').split('package:')[1].replace('\\r\\n', '').split('='))

    def uninstall_package(self):
        ex_ = self.ADB_DIRECTORY + self.UNINSTALL_PACKAGE
        print(subprocess.check_output(ex_))
