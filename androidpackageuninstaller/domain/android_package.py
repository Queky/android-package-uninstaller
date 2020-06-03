from typing import Final


class AndroidPackage:

    package_directory: Final[str]
    package_name: Final[str]

    def __init__(self, package_directory: str, package_name: str):
        self.package_directory = package_directory
        self.package_name = package_name
