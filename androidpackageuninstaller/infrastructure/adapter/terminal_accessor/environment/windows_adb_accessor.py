import subprocess
from abc import ABC
from typing import Final, List
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.adb_accessor import AdbAccessor


class WindowsAdbAccessor(AdbAccessor, ABC):

    ADB_DIRECTORY: Final[str] = ".\\adb\\platform-tools\\"
    UNINSTALL_PACKAGE: Final[str] = "adb shell pm uninstall --user 0 "
    LIST_ALL_PACKAGES: Final[str] = "adb.exe shell \"pm list packages -f\""

    def get_package_information(self, package_name: str):
        pass

    def get_package_list(self) -> List[str]:
        print('implementation')
        ex_ = self.ADB_DIRECTORY + self.LIST_ALL_PACKAGES
        print(ex_)
        # print(subprocess.check_output(ex_).decode('utf-8').split('package:')[1].replace('\\r\\n', '').split('='))
        output: List[str] = subprocess.check_output(ex_).decode('utf-8').split('package:')
        return output

    def uninstall_package(self, package_name: str):
        print('implementation')
        ex_ = self.ADB_DIRECTORY + self.UNINSTALL_PACKAGE + package_name
        print(ex_)
        # print(subprocess.check_output(ex_).decode('utf-8').split('package:')[1].replace('\\r\\n', '').split('='))
        output: str = subprocess.check_output(ex_).decode('utf-8').split('package:')[1]
        return output
