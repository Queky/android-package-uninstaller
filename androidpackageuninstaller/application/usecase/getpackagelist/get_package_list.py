from .get_package_list_command import GetServiceListCommand
from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
from androidpackageuninstaller.infrastructure.adapter.terminal.terminal_android_packages import TerminalServiceAccess
from typing import Final


class GetServiceList:

    androidServices: Final[AndroidPackages]

    def __init__(self):
        self.androidServices = TerminalServiceAccess()

    def execute(self, command: GetServiceListCommand = None):
        print('use-case')
        self.androidServices.get_package_list()
