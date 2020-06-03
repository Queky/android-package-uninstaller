import subprocess
from abc import ABC
from typing import Final, List

from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.adb_accessor import AdbAccessor


class DarwinAdbAccessor(AdbAccessor, ABC):
    ADB_DIRECTORY: Final[str] = ""
    UNINSTALL_PACKAGE: Final[str] = ""
    LIST_ALL_PACKAGES: Final[str] = ""

    def get_package_information(self, package_name: str):
        pass

    def get_package_list(self) -> List[str]:
        print('implementation')
        ex_ = self.ADB_DIRECTORY + self.LIST_ALL_PACKAGES
        print(ex_)
        # print(subprocess.check_output(ex_).decode('utf-8').split('package:')[1].replace('\\r\\n', '').split('='))
        output: List[str] = subprocess.check_output(ex_).decode('utf-8').split('package:')
        return output

    def uninstall_package(self, package_name: str) -> str:
        print('implementation')
        ex_ = self.ADB_DIRECTORY + self.UNINSTALL_PACKAGE + package_name
        print(ex_)
        # print(subprocess.check_output(ex_).decode('utf-8').split('package:')[1].replace('\\r\\n', '').split('='))
        output: str = subprocess.check_output(ex_).decode('utf-8').split('package:')[1]
        return output
