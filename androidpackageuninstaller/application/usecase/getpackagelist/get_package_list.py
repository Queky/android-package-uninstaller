from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
from androidpackageuninstaller.infrastructure.adapter.terminal.terminal_android_packages import TerminalPackageAccess
from typing import Final


class GetPackageList:

    android_services: Final[AndroidPackages]

    def __init__(self):
        self.android_services = TerminalPackageAccess()

    def execute(self):
        return self.android_services.get_package_list()
