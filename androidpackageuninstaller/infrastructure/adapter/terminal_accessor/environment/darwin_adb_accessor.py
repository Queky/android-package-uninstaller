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
        shell_command: str = self.ADB_DIRECTORY + self.LIST_ALL_PACKAGES
        output: List[str] = subprocess.check_output(shell_command).decode('utf-8').split('package:')
        return output

    def uninstall_package(self, package_name: str):
        shell_command = self.ADB_DIRECTORY + str(self.UNINSTALL_PACKAGE) + str(package_name)
        output: str = subprocess.check_output(shell_command).decode('utf-8')
        return output
