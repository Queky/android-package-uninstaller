import subprocess
from typing import Final
from androidpackageuninstaller.application.dataaccess.android_packages import AndroidPackages


class TerminalServiceAccess(AndroidPackages):
    LIST_ALL_PACKAGES: Final[str] = "adb shell 'pm list packages -f'"

    def get_service_information(self):
        pass

    def get_services_list(self):
        print('implementation')
        print(subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')[1].split(' '))

    def uninstall_service(self):
        pass
