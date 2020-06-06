import subprocess
from abc import ABC
from typing import Final, List
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.adb_accessor import AdbAccessor


class WindowsAdbAccessor(AdbAccessor, ABC):

    ADB_DIRECTORY: Final[str] = ".\\adb\\platform-tools\\"
    UNINSTALL_PACKAGE: Final[str] = "adb shell pm uninstall --user 0 "
    LIST_ALL_PACKAGES: Final[str] = "adb.exe shell pm list packages -f"

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
