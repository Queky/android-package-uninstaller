from typing import Final


class UninstallServiceCommand:

    package_name: Final[str]

    def __init__(self, package_name: str):
        self.package_name = package_name
