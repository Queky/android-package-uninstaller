import sys
from abc import ABC
from typing import Final, List
from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.adb_accessor import AdbAccessor
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.environment.darwin_adb_accessor \
    import DarwinAdbAccessor
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.environment.linux_adb_accessor \
    import LinuxAdbAccessor
from androidpackageuninstaller.infrastructure.adapter.terminal_accessor.environment.windows_adb_accessor \
    import WindowsAdbAccessor
from androidpackageuninstaller.domain.android_package import AndroidPackage


class TerminalPackageAccess(AndroidPackages, ABC):

    adb_accessor: Final[AdbAccessor]

    def __init__(self):
        environment: str = sys.platform
        if environment == "linux" or environment == "linux2":
            self.adb_accessor = LinuxAdbAccessor()
        elif environment == "darwin":
            self.adb_accessor = DarwinAdbAccessor()
        elif environment == "win32":
            self.adb_accessor = WindowsAdbAccessor()
        else:
            raise ValueError('Provided environment doesnt have any download URL.')

    def get_package_information(self):
        pass

    def get_package_list(self):
        android_package_list: List[AndroidPackage] = []
        packages: List[str] = self.adb_accessor.get_package_list()
        for index, value in enumerate(packages):
            if packages[index]:
                package_directory: str = value.split('=')[0].rstrip()
                package_name: str = value.split('=')[len(value.split('='))-1].rstrip()
                package_apk = ''
                if any('.apk' in apk_name for apk_name in value.split('=')):
                    package_apk = value.split('=')[0].split('/')[len(value.split('=')[0].split('/'))-1]
                android_package_list.append(AndroidPackage(package_directory, package_name, package_apk))
        return android_package_list

    def uninstall_package(self, package_name: str):
        self.adb_accessor.uninstall_package(package_name)
