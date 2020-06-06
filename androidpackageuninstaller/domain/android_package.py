from typing import Final


class AndroidPackage:

    package_directory: Final[str]
    package_name: Final[str]
    package_apk: Final[str]

    def __init__(self, package_directory: str, package_name: str, package_apk):
        self.package_directory = package_directory
        self.package_name = package_name
        self.package_apk = package_apk
