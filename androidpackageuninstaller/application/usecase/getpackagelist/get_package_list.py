from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
from androidpackageuninstaller.infrastructure.adapter.terminal.terminal_android_packages import TerminalPackageAccess
from typing import Final


class GetPackageList:

    androidServices: Final[AndroidPackages]

    def __init__(self):
        self.androidServices = TerminalPackageAccess()

    def execute(self):
        print('use-case')
        self.androidServices.get_package_list()
