import subprocess
from typing import Final


class TerminalServiceAccess:


    LIST_ALL_PACKAGES: Final[str] = "adb shell 'pm list packages -f'"

    def get_service_information(self):
        result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)

    def get_services_list(self):
        pass

    def uninstall_service(self):
        pass
