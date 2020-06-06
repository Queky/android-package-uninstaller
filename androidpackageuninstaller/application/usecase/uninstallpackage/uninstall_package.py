from .uninstall_package_command import UninstallServiceCommand
from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
from androidpackageuninstaller.infrastructure.adapter.terminal.terminal_android_packages import TerminalPackageAccess
from typing import Final


class UninstallPackage:

    android_services: Final[AndroidPackages]

    def __init__(self):
        self.android_services = TerminalPackageAccess()

    def execute(self, command: UninstallServiceCommand):
        self.android_services.uninstall_package(command.package_name)
